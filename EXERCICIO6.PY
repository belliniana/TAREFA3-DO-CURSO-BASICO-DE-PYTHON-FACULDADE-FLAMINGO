#Curso Básico de Python
#Nome do desenvolvedor: ANA LUIZA DE MORAIS BELLINI
#Versão 1.0
#Exercício de lógica de programação
#Com a linguagem de programação Python
#Exercício: 6) Faça um programa que receba um número
# inteiro e retorne se é primo ou não.

numero=int(input("Digite um número para saber se é um número primo: "))
if numero<=1:
    print("O número",numero,"não é primo!!!")
elif numero%1 ==0 and numero%2 ==1 and numero%3 ==1 and numero%7 ==1 and numero%11 ==1:
    print("o número é primo")
else:
    print("o número não é primo")
print("OBRIGADA POR UTILIZAR O PROGRAMA >3")