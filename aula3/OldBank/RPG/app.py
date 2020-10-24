# -*- coding: UTF-8 -*-
import os
from time import sleep
from random import randint
from modules.monstro import Dementador, Orc
from modules.personagem import Mago, Guerreiro


personagem01 = Mago()
personagem02 = Guerreiro()
monstro01 = Minotauro()
monstro02 = Orc()


def seleciona_personagem():
    while True:
        print("\nSelecione o Personagem: ")
        print("1 - Mago")
        print("2 - Guerreiro")
        print("0 - Para sair")
        try:
            persona = int(input(">>> "))
            if persona == 1:
                personagem = personagem01
                os.system('clear')
            elif persona == 2:
                personagem = personagem02
                os.system('clear')
            elif persona == 0:
                exit()
            else:
                raise TypeError("Personagem não encontrado")
        except ValueError:
            os.system('clear')
            print("Digite apenas números válidos")
            sleep(2)
            continue
        except TypeError as t:
            os.system('clear')
            print(t)
            sleep(2)
            continue
        seleciona_monstro(personagem)

def seleciona_monstro(personagem):
    while True:
        print("\nSelecione o Monstro: ")
        print("1 - Minotauro")
        print("2 - Orc")
        print("0 - Para sair")
        try:
            monster = int(input(">>> "))
            if monster == 1:
                monstro = monstro01
                os.system('clear')

            elif monster == 2:
                monstro = monstro02
                os.system('clear')
            elif monster == 0:
                exit()

            else:
                raise TypeError("Monstro não encontrado")
        except ValueError:
            os.system('clear')
            print("Digite apenas números válidos")
            sleep(2)
            continue
        except TypeError as t:
            os.system('clear')
            print(t)
            sleep(2)
            continue
        principal(personagem, monstro)

def principal(personagem, monstro):
    dano_personagem = randint(1, 50)
    dano_monstro = randint(1, 60)

    if dano_monstro < dano_personagem:
        monstro.hp -= dano_personagem
        print(f"Monstro tomou dano \nHP {monstro.hp}\nDano: {dano_personagem}")
        
        if monstro.hp <= 0:
            os.system('clear')
            print("Fim de Jogo\nVocê Ganhou")
            sleep(2)
            seleciona_personagem()
    else:
        personagem.hp -= dano_monstro
        print(f"Você tomou dano  \nHP: {personagem.hp}\nDano: {dano_monstro}")
        if personagem.hp <= 0:
            os.system('clear')
            print('Você perdeu!')
            sleep(2)
            seleciona_personagem()


seleciona_personagem()
# seleciona_monstro()
# principal()
