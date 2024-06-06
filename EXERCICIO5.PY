#Curso Básico de Python
#Nome do desenvolvedor: ANA LUIZA DE MORAIS BELLINI
#Versão 1.0
#Exercício de lógica de programação
#Com a linguagem de programação Python
#Exercício: 5) Escreva um programa que peça ao usuário para 
# digitar um número e verifique se é positivo, negativo ou zero.

numero=float(input("Digite um número: "))
if numero>0:
    print("O número", numero, "é positivo.")
elif numero<0:
    print("O número", numero, "é negativo.")
else:
    print("O número é zero.")
print("OBRIGADA POR UTILIZAR O PROGRAMA >3")