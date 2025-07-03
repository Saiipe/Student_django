def primo(numero: int):
    cont = 0
    for n in range(2, (numero // 2) + 1):
        if (numero % n == 0):
            cont += 1
    if (cont > 2):
        return print("nao é primo")
    else:
        return print("é primo")


primo(2)
