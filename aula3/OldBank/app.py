#!/usr/bin/python3

class FolhaPagamento:


    def __init__(self, valorHora, quantidadeHoras):
        self.valorHora = valorHora
        self.quantidadeHoras = quantidadeHoras
        # self.salarioBruto = calculaSalarioBruto()
        # self.salarioLiquido = calculaSalarioLiquido()
        # self.contribuicaoSindical = float 0.03
        # self.impostoRenda = float
        # self.fgts = float


    def calculaSalarioBruto(self):
        salBruto = self.valorHora * self.quantidadeHoras
        return salBruto


    def taxa_aliquota(self):
        if(self.calculaSalarioBruto() <= 1900):
            self.aliquota = 0.0
        elif(self.calculaSalarioBruto() <= 2800):
            self.aliquota = 0.07
        elif(self.calculaSalarioBruto() <= 3700):
            self.aliquota = 0.15
        elif(self.calculaSalarioBruto() <= 4600):
            self.aliquota = 0.22
        else:
            self.aliquota = 0.27
        
        return self.aliquota 
    

    def calculaIr(self):
        return self.calculaSalarioBruto() * self.taxa_aliquota()


    def calculaSindicato(self):
        return self.calculaSalarioBruto() * 0.03

    
    def calculaSalarioLiquido(self):
        return self.calculaSalarioBruto() - (self.calculaIr() + self.calculaSindicato())
        # return salLiquido


    def calculaFGTS(self):
        return self.calculaSalarioBruto() * 0.11
   

    def printFolha(self):
        print(f"Salario Bruto: ({self.valorHora} * {self.quantidadeHoras}): {self.calculaSalarioBruto()} ")
        print(f"( - ) IR {self.taxa_aliquota() * 100}%: R$ {self.calculaIr()}")
        print(f"( - ) Sindicato : R$ {self.calculaSindicato()}")
        print(f"FGTS ( 11% ): R$ {self.calculaFGTS()}")
        print(f"Total de Descontos: R$ {(self.calculaIr() + self.calculaSindicato())}")
        print(f"Salario Liquido: {self.calculaSalarioLiquido()}")


valorHora = float(input("Valor da Hora: "))
quantidadeHoras = float(input("Quantidade de horas trabalhadas: "))

marcelo = FolhaPagamento( valorHora, quantidadeHoras)
marcelo.printFolha()