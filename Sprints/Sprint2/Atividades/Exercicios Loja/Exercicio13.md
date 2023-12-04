Enunciado:

Apresente a query para listar os 10 produtos menos vendidos pelos canais de E-Commerce ou Matriz (Considerar apenas vendas concluídas).  As colunas presentes no resultado devem ser cdpro, nmcanalvendas, nmpro e quantidade_vendas.

Query:

SELECT 
  cdpro,
  nmcanalvendas,
  nmpro,
  SUM(TBVENDAS.qtd) AS quantidade_vendas
FROM 
  TBVENDAS
WHERE 
  TBVENDAS.status = 'Concluído'
GROUP BY 
  cdpro, nmcanalvendas, nmpro
ORDER BY 
  quantidade_vendas ASC
LIMIT 10;