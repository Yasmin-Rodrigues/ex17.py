#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos objetos separados:
from math import trunc
num =int(input('Digite um número de 0 a 9999:'))
unidade =num % 10
print(f'Unidade:', unidade)
numd =(num - unidade) / 10 % 10
print(f'Dezena', trunc(numd))
numc =(num - numd) / 100 % 10
print(f'Centena:', trunc(numc))
numm =(num - numd) / 1000 % 10
print(f'Milhar:', trunc(numm))