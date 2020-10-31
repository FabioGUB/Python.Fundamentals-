from behave import step

def soma(x: int, y: int) -> int:
    return x + y




@step('somar "{num1}" com "{num2}"')
def test_soma(context, num1, num2):
    context.r_soma = soma(int(num1), int(num2))


@step('o resultado deve ser "{esperado}"')
def test_soma_result(context, esperado):
    assert context.r_soma == int(esperado), "Erro de soma"
