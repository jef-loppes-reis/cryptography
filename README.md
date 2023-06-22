# Cryptography

## Descrição do projeto

O Cryptography(Criptografia) tem o objetivo em criptografar um determinado "Texto", e gerar uma chave para descriptografar o texto posteriormente.
O projeto foi hospedado no Google App Engine, tendo o objetivo em executar por "endpoint" para apresentação na Universidade Católica de Brasília, matéria de 
Serviços Computacionais em Nuvem.

## Fluxograma

```mermaid
graph LR;

A{Ambiente Google App Engine}-->B[Instancia do projeto]
B-->C[Comunicação com Endpoint]
C-->D[(Apresentação dos Dados)]
```

## Execução

- Script: [main.py](./main.py)
- Comunicação: https://snappy-tine-389700.uc.r.appspot.com + Métodos

-> Exemplos:

```sh
https://snappy-tine-389700.uc.r.appspot.com/?str=Carro&descp=true
```

-> Métodos:

```sh
str=Carro #String (Texto) digitado.
```

```sh
descp=true #Descript Paramento que determinar se o código deve ou não apresentar o texto descriptografado.
```
