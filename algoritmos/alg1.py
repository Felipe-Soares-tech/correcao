from itertools import combinations


combustiveis = [
    {
        'nome' : 'gasolina',
        'valor' : 5.0,
    },
    {
        'nome' : 'diesel',
        'valor': 4.75       
    },
    {
        'nome' : 'etanol',
        'valor' : 3.45
    }
]

for i, combustivel in enumerate(combustiveis):
    print(f'{i+1} - {combustivel["nome"]}')

escolha = int(input('escolhe um numero: '))

print(f'o valor por litro do(a) {combustiveis[escolha-1]["nome"]} é: {combustiveis[escolha-1]["valor"]}')
