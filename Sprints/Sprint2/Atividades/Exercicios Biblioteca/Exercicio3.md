Enunciado:

 Apresente a query para listar as 5 editoras com mais livros na biblioteca. O resultado deve conter apenas as colunas quantidade, nome, estado e cidade. Ordenar as linhas pela coluna que representa a quantidade de livros em ordem decrescente.

Query: 

SELECT
  COUNT(livro.cod) AS quantidade,
  editora.nome,
  endereco.estado,
  endereco.cidade
FROM
  livro
INNER JOIN editora ON livro.editora = editora.codeditora
INNER JOIN endereco ON editora.endereco = endereco.codendereco
GROUP BY
  editora.codeditora
ORDER BY
  quantidade DESC
LIMIT 5;