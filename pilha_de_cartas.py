import random
#Cria um baralho com algumas cartas
def criar_baralho():
    #vetor de naipes
    naipes= ["♠️","♥️","♦️","♣️"]
    #vetor de valores
    valores = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    #cria cartas para o baralho
    baralho=[f"{v}{n}" for n in naipes for v in valores]
    #embaralhar
    random.shuffle(baralho)
    return baralho

def empilhar(pilha,carta):
    pilha.append(carta)

def desempilha(pilha):
    if esta_vazia(pilha):
        raise IndexError("Não é possivel remover da pilha vazia.")
    return pilha.pop()
def esta_vazia(pilha):
    return len(pilha)==0
def topo(pilha):
    return None if esta_vazia(pilha) else pilha[-1]
def tamanho(pilha):
    return len(pilha)
# simulação
baralho = criar_baralho()
#print(baralho)
monte_descarte=[]
#lista 
mao_jogador=[]

