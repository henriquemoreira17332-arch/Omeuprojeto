class Animal:
    def __init__(self, tipo, cor, velMax):
        self.tipo = tipo
        self.cor = cor
        self.velMax = velMax
        self.velocidadeAtual = 0

    def velocidade_deslocamento(self):
        self.velocidadeAtual += 10

        if self.velocidadeAtual > self.velMax:
            self.velocidadeAtual = self.velMax
            print(f"O animal atingiu a velocidade máxima ({self.velMax}km/h)")


raposa = Animal("mamífero", "laranja", 30)
passaro = Animal("ave", "azul", 25)
elefante = Animal("mamífero", "cinzento", 15)

print(raposa.cor)
raposa.velocidade_deslocamento()
raposa.velocidade_deslocamento()
raposa.velocidade_deslocamento()
print(raposa.velocidadeAtual)