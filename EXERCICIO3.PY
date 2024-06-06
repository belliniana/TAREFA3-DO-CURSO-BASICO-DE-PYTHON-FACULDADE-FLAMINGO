#Curso Básico de Python
#Nome do desenvolvedor: ANA LUIZA DE MORAIS BELLINI
#Versão 1.0
#Exercício de lógica de programação
#Com a linguagem de programação Python
#Exercício: 3) Escreva um programa que peça ao usuário para digitar uma
# frase e conte quantas vogais (a, e, i, o, u) ela possui

frase=input("Digite uma frase: ")
total_vogais=0
for caractere in frase:
    if caractere.lower() in 'aeiou':
        total_vogais+=1
print("A frase digitada possui", total_vogais, "vogais.")
print("OBRIGADA POR UTILIZAR O PROGRAMA >3")