Enunciado:

Apresente a query para listar código, nome e data de nascimento dos dependentes do vendedor com menor valor total bruto em vendas (não sendo zero). As colunas presentes no resultado devem ser cddep, nmdep, dtnasc e valor_total_vendas.


Observação: Apenas vendas com status concluído.

Query:

SELECT 
TBDEPENDENTE.cddep,
TBDEPENDENTE.nmdep,
TBDEPENDENTE.dtnasc,
SUM (TBVENDAS.qtd * TBVENDAS.vrunt) as valor_total_vendas
FROM 
TBDEPENDENTE 
LEFT JOIN 
TBVENDEDOR ON TBDEPENDENTE.cdvdd = TBVENDEDOR.cdvdd 
LEFT JOIN 
TBVENDAS ON TBVENDEDOR.cdvdd = TBVENDAS.cdvdd AND TBVENDAS.status LIKE 'Concluído'
GROUP BY 
TBDEPENDENTE.cddep, TBDEPENDENTE.nmdep, TBDEPENDENTE.dtnasc
HAVING 
SUM(TBVENDAS.qtd * TBVENDAS.vrunt) != 0
ORDER BY 
valor_total_vendas ASC 
LIMIT 1;