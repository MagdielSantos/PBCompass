Enunciado:

Apresente a query para listar os códigos das vendas identificadas como deletadas. Apresente o resultado em ordem crescente.

Query:

SELECT
cdven
FROM
TBVENDAS
WHERE TBVENDAS.deletado = 1
ORDER BY cdven ASC;