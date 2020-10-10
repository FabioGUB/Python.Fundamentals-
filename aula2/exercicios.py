#!/usr/bin/python3

# Usuarios


# criar um sistema de login
# usuarios que estão usuarios podem entrar
# usuarios bloqueados não serão permitidos
# é necessário criacão de excecoes

# usuario bloqueados
# Paloma, paulo, leo 

usuarios = ['Renato', 'Caio', 'Camila', 'Paloma', 'Patricia', 'Paulo', 'Joao', 'Sebastião', 'Leo']


# usuarios_bloqueados = [usuarios[3], usuarios[5], usuarios[-1]]
usuarios_bloqueados = []

def adiciona_usuario(user):
    global usuarios
    return usuarios.append(user)



def bloquea_usuario(user):
    if user in usuarios:
        global usuarios_bloqueados
        usuarios_bloqueados.append(user)
    else:
        print('Usuario não encontrado')

def remove_usuario(user):
    global usuarios
    usuarios.remove(user)

def desbloqueia_usuario(user):
    if user in usuarios_bloqueados:
        global usuarios_bloqueados
        usuarios_bloqueados.remove(user)
    pass

while True: 

    try:
        susuario = str(input('Seu usuario: ')).capitalize()
        if susuario in usuarios_bloqueados:
            raise NameError('Usuario Bloaqueado, procure assitencia')
            break
        elif susuario in usuarios:
            print ('Acesso permitido')
            break
        elif susuario == '000':
                print('Programa Finalizado.')
                break
        else:
            raise ValueError ('Usuario inexistente, faca seu registro ou tente novamente. Digite 000 para sair.')
        continue
    except ValueError as ferr:
        print(ferr)
    except NameError as verr:
        print(verr)
