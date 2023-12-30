def calcular_valor_maximo(operadores,operandos) -> float:
 
    resultados = list(map(lambda args: eval(f"{args[0][0]} {args[1]} {args[0][1]}"), zip(operandos, operadores)))
    
    return max(resultados)

operadores = ['+','-','*','/','+']
operandos  = [(3,6), (-7,4.9), (8,-8), (10,2), (8,4)]

resultado = calcular_valor_maximo(operadores, operandos)
print(resultado)