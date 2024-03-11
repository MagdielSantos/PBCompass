## Camada Refined

Nessa etapa eu usei jobs do AWS Glue para processar os dados no parquet da minha camada trusted, de acordo com a minha modelagem, de forma que cada tabela 
será um diretório no meu datalake, e terá o seu arquivo parquet com os respectivos dados de cada tabela, além de separar os dados fiz alguns processamentos
como usar a função explode no array onde ficam os ids e nomes das tags de cada filme, e extrair os ids e nomes do array, para poder usar o id e o nome separadamente.
Na dimensão filmes também eu deixei as tags apenas dos filmes que tem a tag 818 (baseado em livro) que é a única tag que será usada na minha análise.

Utilizei apenas um job para a criação de todas as tabelas, porém disponibilizei no github o código divido da criação de cada tabela, pra facilitar a compreensão
