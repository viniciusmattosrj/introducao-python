#-*- encoding:utf-8 -*-

pessoas = {}

csv_file = open('nomes.csv','r')

for linha in csv_file.readlines():
    data = linha.split(',')
    nome = data[0]
    idade = data[1]
    pessoas[nome] = idade
    
print(pessoas)