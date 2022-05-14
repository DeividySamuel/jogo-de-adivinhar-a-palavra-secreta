import random
lista_vazia = []
chances = 5
lista_palavras = ['cachorro', 'gato', 'coelho', 'passaro', 'cobra', 'tigre', 'coruja','rato','barata','tatu','urso','aguia','elefante','jumento',
                  'burro','boi','galinha','galo','sapo','porco']

animal = random.choice(lista_palavras)

while True:
    if chances <=0:
        print("voçê perdeu")
        break

    letra = str(input("digite uma letra:"))
    lista_vazia.append(letra)
    #print(lista_vazia)
    secreto_temporario =''
    for letra_secreta in animal:
        if letra_secreta in lista_vazia:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == animal:
        print(f'voçe ganhou a palavra secreta era {secreto_temporario}')
        break

    if letra in animal:
        print(f'essa letra {letra} existe na palavra secreta {secreto_temporario}')
    else:
        print(f"voçê errou, a palavra secreta esta assim {secreto_temporario}")
        lista_vazia.pop()

    if letra not in animal:
        chances -= 1
        print(f"voçê ainda tem {chances} chance")
        print()

