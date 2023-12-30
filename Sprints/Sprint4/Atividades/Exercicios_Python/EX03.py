from functools import reduce

def calcula_saldo(lancamentos) -> float:
    
    saldos = map(lambda l: l[0] if l[1] == 'C' else -l[0], lancamentos)
    
    saldo_total = reduce(lambda soma, valor: soma + valor, saldos, 0)
    
    return saldo_total