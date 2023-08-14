class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def informacoes(self):
        print("Nome:", self.nome)
        print("Salário:", self.salario)


funcionario1 = Funcionario("Mateus", 2500.0)
funcionario1.informacoes()
