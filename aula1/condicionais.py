# Aplicação de média

# Calcule a média de um aluno:
#   média = n1 + n2 + n3 + n4 / 4
#   Se a média for maior que 7: Aprovado
#   Se a média for menor que 7 e maior que 4: Recuperação
#   menor que 4: Reprovado
s = 0 
for c in range(1,5):
    x = float(input(f'Nota da NP{c}: '))
    s += x
print(s/4)
