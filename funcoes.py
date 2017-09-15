#-*- encoding:utf-8 -*-

idades = []
idade = ""
while (True):
    idade = input('Informe sua idade ou para sair: ')
    
    if idade == 's':
        print("Saindo do loop")
        break

    idade = int(idade)
    idades.append(idade)

maiorces = [ str(i) for i in idades if i > 25]

print(", ".join(maiores))
print ("Total de pessoas maiores que 25 é : %s" % len(maiores)) 