'''
Desafio 027
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
Ex: Ana Maria de Souza
primeiro = Ana
último = Souza
'''
nome = input('Digite seu nome completo: \n') .upper()
nome = nome.split()
print(f'O primeiro nome é {nome[0]} \nO último nome é {nome[-1]}')
