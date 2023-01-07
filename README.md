# GINCOLLI

Algoritmo **funcional** criado para simular o teletransporte de pacotes usando o "conceito dos QuBit" para troca de textos entre os nós(A, B e C). Esta é uma simulação criada para compreender a mecânica dos spins em seus diferentes estados.

## Mensagem

> **the darkness that you fear** ( *a escuridão que você teme* )

### Enunciado

No experimento, o envelope "MENSAGEM" é caracterizado como elétron e para este propósito dividimos este elétron("MENSAGEM") em vetores a serem armazenados nos spins 1 e 2. Neste ponto desconhecemos em que posição ou lados se encontram os pares da mensagem, ou conjunto de vetores compostos por uma 1 mensagem dividida em dois pares. Este estado é definido como superposição da mensagem, não sendo possível definir com exatidão a posição ou ordem dos pares que compõem o envelope. A distribuição de probabilidades cria os spins compondo vetores ou arranjos para a transmissão dos pacotes entre os nós A, B e C, processo este denominado de entrelaçamento das pontas.

![alt text](https://raw.githubusercontent.com/rodrigmars/gincolli/main/doc/diagrama.png)

### Execução

Python **3.11.1** necessário para o pad de lançamento

Baixando depedências:

```bash
pip install -r requirements.txt
```

Lançando módulo de teste

```bash
pytest -s -v tests/test_async.py
```
