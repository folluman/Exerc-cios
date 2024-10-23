#!python3
# fibonacci.py - Script que verificará de determinado número faz parte da sequência de Fibonacci ou não

def verificarNumFibonacci(numero):
    num = 0
    num2 = 1
    temp = 0

    listaNum = []

    for i in range(numero + 1):
        listaNum.append(num)

        temp = num
        num = num2
        num2 = temp + num

    if numero in listaNum:
        print('Número Fibonacci')
    else:
        print('O número não está na sequência Fibonacci')


numero = int(input('Verifique se é um número Fibonacci: '))
verificarNumFibonacci(numero)
