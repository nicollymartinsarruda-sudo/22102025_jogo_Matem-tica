import random
import time

print("bem vindo ao jogo de matematica")
print("responda o maximo que puder. digite 'sair' para encerar.\n")

pontos = 0
rodada = 1

while true 
#Gera dois numeros e uma operação aleatoria
n1 = random.randint(1, 10)
n2 = random.randint(1, 10)
operacao = random.choice(["+","-","*"])

#calcule
if operacao =="+":
    resultado_certo = n1 + n2
elif operacao =="-":
    resultado_certo = n1 - n2
else:
    resultado_ = n1 * n2
    
    print(f"pergunta {rodada}: quando é {n1}{operacao}{operacao}{n2}?")
    resposta = input("->")
    
    if resposta.liwer() == "sair":
        break
    
    #verifica se é numero
    (resposta.isdigit() and not (resposta.startswith("-" and resposta [1:].isdigit()):print("porfavor, digite um numero ou 'sair'."))
    
