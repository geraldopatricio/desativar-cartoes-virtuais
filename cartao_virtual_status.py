import os
import csv
import requests
import json
import smtplib
import sys

from datetime import datetime, timedelta
from dotenv import load_dotenv
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential
load_dotenv()

def getSecret(key):
    try:
        vaulturi = f"https://{os.getenv('KEY_VAULT_NAME')}.vault.azure.net/"
        credential = DefaultAzureCredential()
        client = SecretClient(vault_url=vaulturi, credential=credential)
        return client.get_secret(key).value
    except:
        print("Chave não encontrada: ", key)
        return None


pier = {
    "base_url": getSecret("API-PIER-URL"),
    "headers": {
        "access_token": getSecret("API-PIER-TOKEN"),
        "client_id": getSecret("API-PIER-CLIENTID"),
        "Content-Type": "application/json"
    }
}

   

date = None
try:
    date = sys.argv[1]
    print(date)
except:
    print("NÃO PASSOU ARGUMENTO")

now = datetime.now()  # current date and time
date_time = now.strftime("%d/%m/%Y %H:%M:%S")
print("RUN CRON JOB")
print(date_time)

if date == None:
    date = datetime.now() - timedelta(days=1)
    date = date.strftime("%Y-%m-%d")

try:
    totalCartoesVirtuaisEmitidos = 0
    totalCartoesVirtuaisAlterados = 0
    datas = 'dataAlteracao;id;idPessoa;idConta;dataGeracao;nomeImpresso\n'
    url_cartoes = pier["base_url"] + "/cartoes?flagProvisorio=1&dataGeracao=" + date
    print(url_cartoes)
    response_cartoes = requests.get(url=url_cartoes,
                                            headers=pier["headers"])
    if response_cartoes.status_code == 200:
        cards = json.loads(response_cartoes.text)
        totalPaginas = cards['totalPages']
        print(cards['totalElements'], cards['totalPages'])
        i = 0
        while i < int(cards['totalPages']):
            try:
                if i > 0:
                    url_cartoes = pier["base_url"] + "cartoes?flagProvisorio=1&dataGeracao="+date+"&page=" + str(i)
                    print(url_cartoes)
                    response_cartoes = requests.get(url=url_cartoes,
                                                headers=pier["headers"])
                    if response_cartoes.status_code == 200:
                        cards = json.loads(response_cartoes.text)
                        print(cards['totalElements'], cards['totalPages'])

                for card in cards['content']:
                    numeroInicial = card["numeroCartao"][0:4]
                    if numeroInicial == '9099':
                        id_cartao = card["id"]
                        estagio_body ={
                            "id": 4
                        }

                        url_bloquear = pier["base_url"] + '/cartoes/'+ str(id_cartao)+'/bloquear?id_status=2&observacao=status para nao embossing'
                        print(url_bloquear)
                        url_estagio = pier["base_url"]  + '/cartoes/'+str(id_cartao)+'/alterar-estagio'
                        response_block = requests.post(url=url_bloquear,headers=pier["headers"])
                        if response_block.status_code == 200:
                            print(f'Bloqueado => {date_time};cartaoId: {card["id"]};idPessoa: {card["idPessoa"]};idConta: {card["idConta"]};dataGeracao: {card["dataGeracao"]};nomeImpresso: {card["nomeImpresso"]}')
                            if card['idEstagio'] != 4:
                                print(url_estagio)
                                response_estagio = requests.post(url=url_estagio, data=json.dumps(estagio_body), headers=pier["headers"])
                                if(response_estagio.status_code == 200):
                                    print(f'Estagio mudado para 4 => {date_time};cartaoId: {card["id"]};idPessoa: {card["idPessoa"]};idConta: {card["idConta"]};dataGeracao: {card["dataGeracao"]};nomeImpresso: {card["nomeImpresso"]}')    
                i += 1
            except Exception as e:
                print(e)

    
except Exception as e:
    print(e)
