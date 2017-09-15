#-*- encoding:utf-8 -*-

pessoas = {}

while (True):
    nome = input("Digite o seu nome ou s para sair: ")

    if nome == 's':
        break

    idade = input('Digite a sua idade %s :' % nome)
    idade = int(idade)

    pessoas[nome] = idade

maiores = (nome for nome, idade in pessoas.items() if idade > 25)
print("\n".join(maiores))

