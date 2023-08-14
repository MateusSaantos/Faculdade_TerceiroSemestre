class Carro:
    def __init__(self, consumo):
        self.consumo = consumo
        self.quantidade_combustivel = 0

    def andar(self, dist):
        combustivel_necessario = dist / self.consumo

        if combustivel_necessario <= self.quantidade_combustivel:
            self.quantidade_combustivel -= combustivel_necessario
            print("Km Percorrida:", dist)
        else:
            print("Não há combustível suficiente!")

    def abastecer(self, qtde):
        self.quantidade_combustivel += qtde
        print("Abastecido:" , qtde)
        print("Total do tanque:", self.quantidade_combustivel)

meu_carro = Carro(20)  
meu_carro.abastecer(200)  
meu_carro.andar(400)  
