
# texto = 'Esse é um texto'

# #crio um iterador
# iterador = iter(texto)

# #retorno sempre o proximo valor
# next(iterador)


# #for i in texto
# #    print(i)

# def for_each(valor):
#     iterador = iter(valor)
#     while True:
#         try:
#             elemento = next(iterador)
#             print(elemento)
#         except StopIteration as stop:
#             break



class Numeros():
    def __iter__(self):
        self.x = 1
        return self
    
    def __next__(self):
        y = self.x
        self.x += 1
        return y


