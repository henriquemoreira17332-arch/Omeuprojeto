class animal:
    def __init__(self, tipo, cor):
        self.tipo = tipo
        self.cor = cor
        

class cao(animal):
    def __init__(self, tipo, cor, raca):
        super().__init__(tipo, cor)
        self.raca = raca
        
        
bobi=cao("canideo","preta","pincher")

print(bobi.raca)
print(bobi.cor)
        

