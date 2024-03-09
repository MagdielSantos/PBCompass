## Modelagem Dimensional

Na transformação da modelagem relacional para uma modelagem dimensional, o objetivo foi facilitar a resposta de perguntas analíticas específicas, como "Qual é a média de valor diário das locações por marca de carro?", "Qual foi o total de locações realizadas por clientes do estado de Pernambuco?" ou "Qual foi o total de locações realizadas entre os anos de 2000 a 2010?".

Para facilitar a visualização das relações entre as tabelas, foram disponibilizados dois scripts no GitHub: um com a criação das tabelas diretamente e outro com a criação de views a partir das tabelas relacionais, conforme recomendado na descrição da atividade. Isso permite uma melhor compreensão da estrutura do banco de dados e das relações entre as entidades.

Durante a transformação da modelagem relacional em dimensional, foi criada uma tabela de fatos contendo apenas medidas numéricas e identificadores das dimensões relevantes. Além disso, foram criadas dimensões que contêm os campos relacionados aos eventos registrados na tabela de fatos.


