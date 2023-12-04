Enunciado:

Apresente a query para listar o nome dos autores com nenhuma publicação. Apresentá-los em ordem crescente.

Query:

SELECT 
autor.nome
FROM
autor
LEFT JOIN
livro ON autor.codautor = livro.autor
GROUP BY 
autor.nome HAVING COUNT(livro.cod) = 0
ORDER BY
autor.nome ASC;