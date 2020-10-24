#!/usr/bin/python3


estados = {
    'estados': {
        'sp': {
            'nome': 'São Paulo',
            'municipios': 645,
            'populacao': 4404
        },
        'rj': {
            'nome': 'Rio de Janeiro',
            'municipios': 92,
            'populacao': 16.72
        },
        'mg': {
            'nome': 'Minas Gerais',
            'municipios': 31,
            'populacao': 20.87
        }
    }
}

print(f"O nome que corresponde a sigla MG é {estados['estados']['mg']['nome']}")
print(f"A quantidade de municipios de MG é {estados['estados']['mg']['municipios']}")
print(f"A populacão de Minas Gerais é de {estados['estados']['mg']['populacao']} pessoas ")

print(f"A populacão do Rio de Janeiro é de {estados['estados']['rj']['populacao']} pessoas")