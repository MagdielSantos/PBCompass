Enunciado:

Apresente a query para listar o nome dos autores que publicaram livros através de editoras NÃO situadas na região sul do Brasil. Ordene o resultado pela coluna nome, em ordem crescente. Não podem haver nomes repetidos em seu retorno.

Query:

SELECT Distinct autor.nome
FROM
autor 
LEFT JOIN livro ON autor.codautor = livro.autor
LEFT JOIN editora  ON livro.editora = editora.codeditora
LEFT JOIN endereco  ON editora.endereco = endereco.codendereco
WHERE endereco.estado NOT LIKE 'PARANÁ' AND endereco.estado NOT LIKE 'RIO GRANDE DO SUL'
ORDER BY autor.nome ASC;
