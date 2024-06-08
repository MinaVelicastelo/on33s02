
n1 = int(input ('Digite o primeiro número: '))
n2 = int(input ('Digite o segundo número: '))

soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2
divisao_inteira = n1 // n2
modulo = n1 % n2
potencia = n1 ** n2

print('\n Resultados das operações aritméticas: ')
print('Soma: ', soma)
print('Subtração: ', subtracao)
print('Multiplicação: ', multiplicacao)
print('Divisão: ', divisao)
print('Divisão inteira: ', divisao_inteira)
print('Módulo: ', modulo)
print('Potência: ', potencia)

print('\n Resultados dessas operações de comparação')
print('Igualdade:', n1 == n2)
print('Diferenca:', n1 != n2)
print('Maior:', n1 > n2)
print('Maior ou igual:', n1 >= n2)
print('Menor:', n1 < n2)
print('Menor ou igual:', n1 <= n2)

print('\n Resultado dos operadores de atribuição:')
n1 += 5
print('n1 += 5:',n1)
n2 /= 2
print('n2 /= 2:', n2)

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
if n1 in lista_numeros:
    print(f'O número {n1} está na lista de números')
else:
    print(f'O numero {n1} não está na lista de números')

x = [1, 2, 3]
y = [1, 2, 3]
z = x

print('\n Resultado das operações de identificação de objetos')
print('x is z:', x is z)
print('x is y:', x is y)
print('x is not y:', x is not y)

