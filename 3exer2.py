'''
2.
Faça um Programa que leia um vetor de 10 números reais e mostre os na ordem inversa
'''

numeros = []
print("Informe os 10 numeros reais")
for i in range(10):
    numeros.append(float(input("Numero " + str(i+1) + ": ")))
numeros.reverse()
print(numeros)
