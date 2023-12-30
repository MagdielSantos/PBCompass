def conta_vogais(texto: str) -> int:
    vogais = set("aeiouAEIOU")
    vogais_filtrado = len(list(filter(lambda char: char in vogais, texto)))
    return(vogais_filtrado)

