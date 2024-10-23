#!python3
# letraA.py = Verifica quantas vezes a letra A ocorre em uma string

def numA(texto):
    num = 0

    for i in texto:
        if i == 'a' or i == 'a'.upper:
            num += 1
            print(num)

print('Coloque o texto e verifique quantas letras A ele possui. Obs: As letras A com unicode não serão correspondidas no código, então passe um texto sem unicode')
texto = str(input())

numA(texto)
