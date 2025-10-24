from funçoes import *
while True:
    print("Cadastrar aluno e notas - 1")
    print("Exibir Relatorio - 2")
    print("Sair do Programa - 0")
    op = input("Escolha uma opção: ")
    if op == "1":
        ListaNotas = []    
        Aluno = input("Digite o nome do aluno")
        for i in range(3):
            ListaNotas.append(float(input("Digite uma nota: ")))
            notadict = {Aluno : [ListaNotas]}
            