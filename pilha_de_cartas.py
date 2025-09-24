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
#comprar cartas 
for _ in range(11):
    mao_jogador.append(desempilha(baralho))
#Mostra cartas na mão do jogador    
print(mao_jogador)
#Mostra total de cartas restantes
print(tamanho(baralho))
#descartar duas cartas
empilhar(monte_descarte,mao_jogador.pop())
empilhar(monte_descarte,mao_jogador.pop())
#Mostra cartas na mão do jogador    
print("Mão do jogador: ",mao_jogador)
print("Pilha de descarte: ",monte_descarte)

