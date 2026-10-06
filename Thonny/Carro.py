class Carro:
    def __init__(self, cor, cilindrada):
        self.cor = cor
        self.cilindrada = cilindrada
        self.velocidade = 0
    def acelarar(self):
        self.velocidade += 10
    def travar(self):
        self.velocidade = 0
        
meu_carro = Carro("vermelho", 1600)
carro_do_pai = Carro("preto", 2000)
carro_do_neto = Carro("rosa", 3000)
carro_do_neto.acelarar()

print(meu_carro.cor)
print(carro_do_pai.cilindrada)
print(carro_do_neto.cor)
print(carro_do_neto.velocidade)
carro_do_neto.acelarar()
print(carro_do_neto.velocidade)