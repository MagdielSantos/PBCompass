## Enunciado:

Apresente a query para listar o código e nome cliente com maior gasto na loja. As colunas presentes no resultado devem ser cdcli, nmcli e gasto, esta última representando o somatório das vendas (concluídas) atribuídas ao cliente.

## Query:

SELECT   
TBVENDAS.cdcli,  
TBVENDAS.nmcli,  
SUM(TBVENDAS.qtd * TBVENDAS.vrunt) as gasto  
FROM  
TBVENDAS  
WHERE TBVENDAS.status LIKE 'Concluído'  
GROUP BY TBVENDAS.cdcli, TBVENDAS.nmcli  
ORDER BY gasto DESC   
LIMIT 1;  
