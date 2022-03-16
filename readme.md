# Cartao Virtual Mudanca Status
Este Script tem por finalidade o Bloqueio de Cartões Indevidos na Dock.
Para isso filtra os cartoes virtuais (9099) gerados na data (yyyy-mm-dd) anterior a execução do script
Tenta bloquear para status=2, se bloquear, então muda estágio para 4.

Printa as urls das tentativas de bloqueio e estágio. Saira no log caso bloqueado com sucesso => 
Bloqueado => 11/03/2022 20:40:55;cartaoId: 6023399;idPessoa: 4086336;idConta: 2421129;dataGeracao: 2022-03-10T10:42:07.623Z;nomeImpresso: ITALO LOPES

Se mudar o estágio com sucesso: 
Estagio mudado para 4 => 11/03/2022 20:40:55;cartaoId: 6023399;idPessoa: 4086336;idConta: 2421129;dataGeracao: 2022-03-10T10:42:07.623Z;nomeImpresso: ITALO LOPES

