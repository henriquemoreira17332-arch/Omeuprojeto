import random

class Jogador:
    OPCOES = ["pedra", "papel", "tesoura"]
    
    def __init__(self, nome):
        self.nome = nomr
        self.jogada = None
    
    def escolher_jogada(self):
        self.jogada = random.choice(self.OPCOES)
        
