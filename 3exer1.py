'''
1.
Faça um Programa que leia um vetor de 5 números inteiros e mostre-os
'''

vetor = []
print("Informe 5 numeros")
for n in range(5):
    vetor.append(int(input("Numero " + str(n+1) + ": ")))
print("vetor", vetor)
