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
# simulação
baralho = criar_baralho()
print(baralho)
