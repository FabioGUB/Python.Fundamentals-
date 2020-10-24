# vph- Valor por Hora
# ht- Hora Trabalhada
# salsb- Salario Bruto
class Salario:

    def __init__(self, vph: float, ht: float):
        self.vph = vph
        self.ht = ht
        self.sab = self.vph * self.ht
        self.fgt = 0
        self.sindicat = 0
        self.ir = 0
        self.dt = 0

    def imr(self):

        if self.sab <= 1900:
            self.ir = 0
            print('Sem desconto de IR')
            return self.ir

        elif self.sab <= 2800:
            self.ir = self.sab * (7 / 100)
            print(f'(-) IR (7%):{self.ir:.2f}')
            return self.ir
        elif self.sab <= 3700:
            self.ir = self.sab * (15 / 100)
            print(f'(-) IR (15%):{self.ir:.2f}')
            return self.ir
        elif self.sab <= 4600:
            self.ir = self.sab * (22 / 100)
            print(f'(-) IR (22%):{self.ir:.2f}')
            return self.ir
        else:
            self.ir = self.sab * (27 / 100)
            print(f'(-) IR (27%):{self.ir:.2f}')
            return self.ir

    def sindicato(self):
        self.sindicat = self.sab * (3 / 100)
        return self.sindicat

    def fgts(self):
        self.fgt = self.sab * (11 / 100)
        return self.fgt

    def dct(self):
        self.dt = self.ir + self.sindicat
        return self.dt

    def sl(self):
        sl = self.sab - self.dt
        return sl
