
def calcular_media(ListaNotas):
    media = sum(ListaNotas)/len(ListaNotas)
    return media

def verificacao(media):
    if media >= 7:
        print("Esse aluno foi aprovado")
    elif media <= 6.9 and media == 5:
        print("Recuperação!!!")
    elif media < 5:
        print("Você está Reprovado!!!")


    