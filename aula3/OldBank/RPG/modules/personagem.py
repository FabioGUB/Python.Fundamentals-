#!usr/bin/python3
from random import randint

class Personagem:
    def __init__(self):
        self.hp = 100
        self.mp = 100
        self.xp = 0
        self.nivel = 1
        self.esquiva = 0

    def subirNivel(self):
        if self.xp > (20 * self.nivel)
            self.nivel += 1
            print('Level UP!')

class Mago(Personagem):
    def __init__(self):
        super().__init__()
        self.atq = 30
        self.arma = 'cajado'
        self.msg_atq = 'Magia das trevas!!!'
        self.poderEspecial = 3

    def recuperacaoMana(self):
        if self.poderEspecial > 0:
            if self.mp >= 70:
                self.mp = 100
                self.poderEspecial -= 1\
                print ('Mana Recuperada')
            else:
                self.mp += 30
                self.poderEspecial -= 1
        else:
            print('Sem cargas')

    def recuperacaoVida(self):
        if self.poderEspecial > 0:
            if self.hp >= 70:
                self.hp = 100
                self.poderEspecial -= 1
                print('Vida recuperada')
            else:
                self.hp += 30
                self.poderEspecial -= 1
        else:
            print('Sem cargas')
class Guerreiro(Personagem):
    def __init__(self):
        super().__init__()
        self.atq = 50
        self.arma = 'Espada'
        self.msg_atq = 'arrrrrrrgggggggggggg'
        self.poderEspecial = 1

    def furia(self):
        if self.poderEspecial > 0:
            self.atq += 15



