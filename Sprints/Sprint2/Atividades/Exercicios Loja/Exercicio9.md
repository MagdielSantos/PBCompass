## Enunciado:

Apresente a query para listar o código e nome do produto mais vendido entre as datas de 2014-02-03 até 2018-02-02, e que estas vendas estejam com o status concluída. As colunas presentes no resultado devem ser cdpro e nmpro.

## Query:

SELECT   
TBESTOQUEPRODUTO.cdpro,  
TBVENDAS.nmpro  
FROM  
TBESTOQUEPRODUTO  
LEFT JOIN TBVENDAS ON TBESTOQUEPRODUTO.cdpro = TBVENDAS.cdpro WHERE dtven between   
'2014-02-03'AND '2018-02-02' AND TBVENDAS.status LIKE 'Concluído'  
GROUP BY TBESTOQUEPRODUTO.cdpro, TBVENDAS.nmpro  
ORDER BY COUNT(TBVENDAS.nmpro) DESC   
LIMIT 1;  
