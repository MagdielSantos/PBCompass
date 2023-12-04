Enunciado:

Apresente a query para listar o autor com maior número de livros publicados. O resultado deve conter apenas as colunas codautor, nome, quantidade_publicacoes.

Query:

SELECT
autor.codautor, 
autor.nome,
COUNT(livro.cod) As quantidade_publicacoes
FROM
 autor
 LEFT JOIN
 livro ON autor.codautor = livro.autor
 GROUP BY 
 autor.codautor
 ORDER BY 
 quantidade_publicacoes DESC
 LIMIT 1;