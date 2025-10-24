from funçoes import *
ListaNotas = []    
ListaAlunos = []
while True:
    print("Cadastrar aluno e notas - 1")
    print("Exibir Relatorio - 2")
    print("Sair do Programa - 0")
    op = input("Escolha uma opção: ")
    if op == "0":
        break
    elif op == "1":
        Aluno = input("Digite o nome do aluno")
        for i in range(3):
            ListaNotas.append(float(input("Digite uma nota: ")))
        mediaAl= calcular_media(ListaNotas)
        status = verificacao(mediaAl)
        dadosDoAluno = [ListaNotas,mediaAl,status]
        dictAluno = {
            Aluno: dadosDoAluno 
        }
        ListaAlunos.append(dictAluno)
    elif op == "2":
        print(ListaAlunos)
            
        