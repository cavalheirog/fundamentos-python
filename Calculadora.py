# calculadora_simples.py
# Projeto básico para praticar lógica em Python

print('=== Calculadora Simples ===')

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
op = input('Escolha a operação (+, -, *, /): ')

resultado = None

if op == '+':
    resultado = n1 + n2
elif op == '-':
    resultado = n1 - n2
elif op == '*':
    resultado = n1 * n2
elif op == '/':
    if n2 != 0:
        resultado = n1 / n2
    else:
        print('Erro: divisão por zero.')
else:
    print('Operação inválida.')

if resultado is not None:
    print('Resultado:', resultado)
