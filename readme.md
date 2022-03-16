<p align="center">
  <img src="./src/assets/logo-fortbrasil.png" width="320" alt="Logo FortBrasil" /></a>
</p>


## Technologias usadas neste projeto

<a href="https://www.python.org/downloads/" target="_blank"><img src="https://img.shields.io/badge/Python-4B8BBE?style=for-the-badge&logo=Python&logoColor=white" alt="Python" /></a> <a href="https://docs.docker.com/get-started/" target="_blank"><img src="https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white" alt="Docker" /></a>   <a href="https://gitlab.com/Fortbrasil/microservicos/microservice-sendmail" target="_blank"><img src="https://img.shields.io/badge/GitLab-330F63?style=for-the-badge&logo=gitlab&logoColor=white" alt="GitLab" /></a>



# Cartao Virtual - Mudanca Status - Desativação
Este Script tem por finalidade o alterar o Status do Cartão Virtual apenas, se ele estiver ativo indevidamente ele irá ser bloqueado, porém o parâmetro sempre será o dia anterior, fazendo uma varredura diária e não geral, logo é de suma importância que este job seja executado todos os dias em horário definido pelo PO da Squad de Logística.

```bash

Para isso filtra os cartoes virtuais (9099) gerados na data (yyyy-mm-dd) anterior a 
execução do script Tenta bloquear para status=2, se bloquear, então muda estágio para 4.

Printa as urls das tentativas de bloqueio e estágio. 
Saira no log caso bloqueado com sucesso => 
Bloqueado => 11/03/2022 20:40:55;
cartaoId: 6023399;
idPessoa: 4086336;
idConta: 2421129;
dataGeracao: 2022-03-10T10:42:07.623Z;
nomeImpresso: ITALO LOPES

```

```bash
Se mudar o estágio com sucesso: 
Estagio mudado para 4 => 11/03/2022 20:40:55;
cartaoId: 6023399;
idPessoa: 4086336;
idConta: 2421129;
dataGeracao: 2022-03-10T10:42:07.623Z;
nomeImpresso: ITALO LOPES


```


# Programação de Execução no Rundeck
Deverá ser executado todos os dias o Job as 8h da manhã

# Procedimento para subida e execução
Usar o Dockerfile que contempla a subida, instalaçãoes dos pre-requisitos e execução do arquivo

