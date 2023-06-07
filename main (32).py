import random
palavras = []
palavra = "1"

#Adicionar palavras
def add(palavra, palavras):
    while palavra != "":
        palavra = input("Palavra: ")
        if palavra != "":
            palavras.append(palavra)
        
    return palavra, palavras

#Embaralhar palavras
def embaralhar(palavras):
    return random.choice(palavras)

#Dicas da palavra
def dicas(escolhido):
    vogal = 0
    consoante = 0
    
    for t in escolhido:
        if t == 'a' or t == 'e' or t == 'i' or t == 'o' or t == 'u':
            vogal += 1
        else:
            consoante += 1
    print(f"A palavra tem {vogal} vogais e {consoante} consoantes")
            
        

def forca(escolhido, tentativa = 1):
    #Tamanho maximo da palavra
    palavra = ["_ ", "_ ", "_ ", "_ ", "_ ", "_ ", "_ ", "_ ", "_ ", "_ ", "_ ", "_ ", "_ ", "_ ", "_ "]
    chute = ""
    chutes = []
    contador = 0
    contadori = 0
    ganhar = 0
    caracteres = 0
    
    #Espaçamento de letras na impressão, definir quantos caracteres a palavra tem
    for i in escolhido:
            print('_ ', end="")
            caracteres += 1
            
    #Forca
    while tentativa != 11:
        print("\n")
        chute = input()
        
        #Evitar repetição da mesma letra
        if tentativa > 1:
            while contadori <= len(chutes) - 1:
                if chute == chutes[contadori]:
                    chute = input()
                    contadori = -1
                contadori += 1

        contadori = 0
        chutes.append(chute)
        #Posicionar a letra no espaçamento correto, contar acertos para vencer o jogo
        for i in escolhido:
            if palavra[contador] == "_ ":
                if i == chute:
                    palavra[contador] = i
                    print(f"{palavra[contador]} ", end="")
                    ganhar += 1
                else:
                    print(palavra[contador], end="")
            else:
                print(f"{palavra[contador]} ", end="")
                ganhar += 1
            contador += 1
        
        #Imprimir chutes
        print("\nLetras usadas: ", end="")
        for i in chutes:
            print(f"{i} ", end="")
        
        print(f"\nRestam {10 - tentativa} tentativas")
        if ganhar == caracteres:
            print("\nVoce venceu!!!")
            break
        
        tentativa += 1   
        contador = 0
        ganhar = 0
        
    if tentativa == 10:
        print("\nVoce perdeu :(")
    
add(palavra, palavras)     
escolhido = embaralhar(palavras)
dicas(escolhido)
forca(escolhido)