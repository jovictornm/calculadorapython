import sys

# Variaveis
operacao = None
numero1 = None
numero2 = None
resultado = None

# Funcionamento do Programa
operacao = input("Qual a operação a ser executada? +, -, * ou / \n")

# Criando erro de Operação inválida 
if operacao not in ['+', '-', '*', '/']:
    print("Operação inválida. \n")
    sys.exit()

# Funcionamento correto
numero1 = float(input("Qual o primeiro número? \n"))
numero2 = float(input("Qual o segundo número? \n"))
if operacao == '+':
    resultado = numero1 + numero2
    print(f"O resultado da operação é: {resultado}")
elif operacao == '-':
    resultado = numero1 - numero2
    print(f"O resultado da operação é: {resultado}")
elif operacao == '*':
    resultado = numero1 * numero2
    print(f"O resultado da operação é: {resultado}")
elif operacao == '/':
    resultado = numero1 / numero2
    print(f"O resultado da operação é: {resultado}")

# Criando pausa proposital do programas
input("Pressione Enter para sair...")

