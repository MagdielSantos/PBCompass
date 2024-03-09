## Modelagem Dimensional

Na transformação da modelagem relacional para uma modelagem dimensional, eu visei facilitar as respostas de perguntas como: "Qual é a média de valor diário das locações por marca de carro?", "Qual foi o total de locações realizadas por clientes do estado de Pernambuco?" ou "Qual foi o total de locações realizadas entre os anos de 2000 a 2010?".

Eu upei no GitHub um script com tabelas e um script com views a partir da tabela relacional, pois no DBeaver, que foi o SGBD que eu usei, não tem como visualizar relações entre views. Então, criei tabelas para tirar o print da modelagem, mas upei um script utilizando views também, como é recomendado na descrição da atividade.

Sobre a transformação da modelagem relacional em dimensional, a tabela de fatos eu criei contendo apenas medidas numéricas e identificadores das dimensões. E criei as dimensões que contêm os campos relacionados aos eventos registrados na tabela de fatos.
