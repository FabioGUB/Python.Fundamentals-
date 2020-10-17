from _pagamento import Salario

vph = float(input('Qual seu valor por hora de trabalho: '))
ht = float(input('Quantas horas você trabalhou nesse mês: '))
sb = vph * ht
Sal1 = Salario(vph, ht)

print(f'Valor da hora: R${vph}')
print(f'Horas Trabalhadas: {ht}')
print(f'Salário Bruto R${Sal1.sab:.2f}')
Sal1.imr()
print(f'(-)Sindicato 3%: {Sal1.sindicato():.2f}')
print(f'FGTS (11%): {Sal1.fgts():.2f}')
print(f'Total de Descontos: R${Sal1.dct():.2f}')
print(f'Salário Liquido: R${Sal1.sl():.2f}')
