import names
import random
import os 
import time


random.seed(40)

qtd_nomes_unicos = 3000
qtd_nomes_aleatorios = 10000000

aux = []

# Gerar uma lista de nomes únicos
for i in range(qtd_nomes_unicos):
    aux.append(names.get_full_name())

# Gerar uma lista de nomes aleatórios usando a lista de nomes únicos
dados = []
for i in range(qtd_nomes_aleatorios):
    dados.append(random.choice(aux))

# Imprimir os primeiros 10 elementos da lista para fins de demonstração
print("Gerando {} nomes aleatórios".format(qtd_nomes_aleatorios))
print(dados[:10])

# Gravar os resultados em um arquivo de texto
with open('nomes_aleatorios.txt', 'w') as file:
    for nome in dados:
        file.write(nome + '\n')
