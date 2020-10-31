from unittest import TestCase, main

# a = 10
# b = 20

# # assert a == b, 'a é diferende de b'
# # assert a != b, 'a é igual a b'


# def soma(x, y):
#     return x + y
    

# def subtracao(x, y):
#     return x - y

# # assert soma(20, 20) == 40, f' Obtido {soma(20, 20)} e o esperado é 40'
# # assert soma(20, 15) == 35, f' Obtido {soma(20, 15)} e o esperado é 35'


# class Testes(TestCase):
#     def test_soma(self):
#         self.assertEqual(soma(5,5), 10)
#         self.assertLess(soma(5,5), 11)
#     def test_subtracao(self):
#         self.assertEqual(subtracao(5,3), 2)
#         self.assertLessEqual(subtracao(15, 5), 10)




def validar_par(num: int)-> bool:
    ''' função para validar um número par
        Args:
        num - recebe um inteiro
        return: booleano'''
    if isinstance(num, int):
        return True if num % 2 == 0 else False
    elif isinstance(num, str):
        if num.isnumeric():
            return True if int(num) % 2 == 0 else False
    else:
        return None



        

class Testes(TestCase):
    def test_par(self):
        self.assertEqual(validar_par(4), True)
        self.assertEqual(validar_par(6), True)
    def test_impar(self):
        self.assertEqual(validar_par(5), False)
        self.assertEqual(validar_par(11), False)
    def test_string(self):
        self.assertEqual(validar_par('102'), True)
        self.assertEqual(validar_par('1059'), False)
        self.assertEqual(validar_par('string'), None) 



if __name__ == "__main__":
    main()







