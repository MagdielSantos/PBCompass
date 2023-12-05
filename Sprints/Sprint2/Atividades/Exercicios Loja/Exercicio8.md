## Enunciado:

Apresente a query para listar o código e o nome do vendedor com maior número de vendas (contagem), e que estas vendas estejam com o status concluída.  As colunas presentes no resultado devem ser, portanto, cdvdd e nmvdd.

## Query:

SELECT   
TBVENDEDOR.cdvdd,  
TBVENDEDOR.nmvdd  
FROM  
TBVENDEDOR  
LEFT JOIN TBVENDAS  
ON TBVENDEDOR.cdvdd = TBVENDAS.cdvdd AND TBVENDAS.status LIKE 'Concluído'  
GROUP BY  
TBVENDEDOR.cdvdd, TBVENDEDOR.nmvdd  
ORDER BY COUNT(TBVENDAS.cdvdd) DESC   
LIMIT 1;  
