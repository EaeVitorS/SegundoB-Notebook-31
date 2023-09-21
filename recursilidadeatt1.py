import time 

def contagem_regressiva(numero):
    print(numero)
    time.sleep(1)
    if numero == 1:
        return 1
    else:
        return contagem_regressiva(numero - 1)

numero_inicial = int(input("Digite um número inteiro: "))
contagem_regressiva(numero_inicial)

print(f"BOOOOOOOOOOOOOMMMMMMMMMM")