import hashlib as hl


texto = input("Digite um texto ou digite 'stop' para sair : ")

while texto != "stop" :

    hash_object = hl.sha1(texto.encode())

    hex_dig = hash_object.hexdigest()

    print("Hash SHA-1 do texto: ", hex_dig)