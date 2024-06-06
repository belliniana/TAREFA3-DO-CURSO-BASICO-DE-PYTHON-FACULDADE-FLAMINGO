#Curso Básico de Python
#Nome do desenvolvedor: ANA LUIZA DE MORAIS BELLINI
#Versão 1.0
#Exercício de lógica de programação
#Com a linguagem de programação Python
#Exercício: 4) Escreva um programa que peça ao usuário para digitar 
# três números e retorne o maior deles.

numero1=float(input("Digite o primeiro número: "))
numero2=float(input("Digite o segundo número: "))
numero3=float(input("Digite o terceiro número: "))
maior_numero=numero1
if numero2>maior_numero:
    maior_numero=numero2
if numero3>maior_numero:
    maior_numero=numero3
print("O maior número é:", maior_numero)
print("OBRIGADA POR UTILIZAR O PROGRAMA >3")