texto = input('digite uma frase para verificar se é um palindromo: ').lower().replace(' ','')

if texto == texto[::-1]:
    print('é um palindromo')
else:
    print('não é palindromo')