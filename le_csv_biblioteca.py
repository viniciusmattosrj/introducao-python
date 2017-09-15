#-*- encoding:utf-8 -*-

import csv

pessoas = {}

csv_file = open('nomes.csv','r')

linhas = csv.reader(csv_file, delimiter=',',quotechar='"')
    
for data in linhas:
    nome = data[0]
    idade = data[1]
    pessoas[nome] = idade
    
print(pessoas)