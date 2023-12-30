with open('number.txt') as arquivo:
    numeros = list(map(int, arquivo.readlines()))

    numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))

    top_5 = sorted(numeros_pares, reverse=True)[:5]

    soma = sum(top_5)

print(top_5)
print(soma)