'''
3.
Crie uma lista com os 20 primeiros colocados do Campeonato Brasileiro de Futebol
a)
Faça um programa que mostre os 5 primeiros colocados
b)
Os últimos 4 colocados (zona de rebaixamento)
c)
Mostre a posição em que se encontra a Chapecoense
d)
Exiba a lista dos times em ordem alfabética
'''

time = ["Palmeiras", "Santos", "Atletico-MG", "Botafogo", "Flamengo", "Bahia", "Internacional", "São Paulo", "Goias",
        "Corinthians", "Athelico-PR", "Ceara", "Gremio", "Cruzeiro", "Fluminense", "Chapecoense", "Fortaleza", "Vasco",
        "CSA", "Avai"]

#a
print("Os cinco primeiros colocados da tabela são:", time[0:5])
print("")
#b
print("Os Times na Zona de Rebaixamento são:", time[16:20])
print("")
#c
print("A Posição da Chapecoense é:", time.index("Chapecoense"))
print("")
#d
time.sort()
print(time)