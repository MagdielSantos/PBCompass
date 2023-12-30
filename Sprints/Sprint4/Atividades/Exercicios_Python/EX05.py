import csv


def processar_notas(arquivo):

    with open(arquivo, 'r') as file:
        reader = csv.reader(file)
        
        resultados = []

        for linha in reader:
            nome = linha[0]
            notas = list(map(int, linha[1:])) 
            tres_maiores_notas = sorted(notas, reverse=True)[:3]  
            media_tres_maiores = round(sum(tres_maiores_notas) / 3, 2)  

            
            resultados.append((nome, tres_maiores_notas, media_tres_maiores))

       
        resultados_ordenados = sorted(resultados, key=lambda x: x[0])

        
        for resultado in resultados_ordenados:
            print(f"Nome: {resultado[0]} Notas: {resultado[1]} Média: {resultado[2]}")


processar_notas('estudantes.csv')
