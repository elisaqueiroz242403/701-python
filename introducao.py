# print ('OII')

import statistics as es

historia_nota1 = float(input('Digite sua nota: '))
historia_nota2 = float(input('Digite sua nota: '))

lista_notas = [historia_nota1, historia_nota2]

# soma = sum(historia_nota1, historia_nota2)

media = es.mean(lista_notas)
print('sua média é' + str(media))

if media >= 7: 
    print('aprovado')

elif media >= 5 or media < 7:
    print('aprovado')

else:
    print('reprovado')