# -*- coding: utf-8 -*-
print '1.Cadastrar aluno.'
print '2.Fazer trancamento de aluno pela matricula.'
print '3.Informações de cada aluno.'
print '4.Informações de todos os alunos.'
print '5.Informações de alunos acima da Média.'
print '6.Informações de alunos abaixo da Média.'
print '7.Media total e Media Indiviadual.'
print '8.Alterar a nota de um aluno.'
print '9.Informações dos Disciplina acima da Média Total.'
print '10.Sair do programa.'


def Acima(Materia, lin, coll):  # Função que retorna alunos com media acima
    A = []
    for h in range(lin):
        la = []
        for t in range(coll - 1, coll):
            if Materia[h][t] >= 7:
                la.append(Materia[h][t])
        A.append(la)
    return A


def Baixo(Materia, lin, coll):  # Função que retorna alunos com media abaixo
    B = []
    for w in range(lin):
        lb = []
        for q in range(coll - 1, coll):
            if Materia[w][q] < 7:
                lb.append(Materia[w][q])
        B.append(lb)
    return B


def Mtotal(Materia, lin, coll):  # Função que retorna média total
    total = 0
    for w in range(lin):
        for m in range(coll - 1, coll):
            total += Materia[w][m]
    Mt = total / lin
    return Mt


def Total(Materia, lin, coll):  # Função que retorna alunos com media acima da total
    total = Mtotal(Materia, lin, coll)
    T = []
    for w in range(lin):
        lt = []
        for q in range(coll - 1, coll):
            if Materia[w][q] >= total:
                lt.append(Materia[w][q])
        T.append(lt)
    return T


n = 0
while n != 10 and n < 10:
    print 'Aperte um número:'
    n = input()
    if n == 1:  # Cadrastra Alunos
        print'Digite o nome da disciplina:'
        Disciplina = raw_input()
        print'Digite a quantidade de alunos:'
        qtda = input()
        print'Digite a quantidade de provas'
        provas = input()
        var = Disciplina + str(1)  # Arquivo para guarda provas e qtd
        var = open('Desktop', 'w')
        Disciplina = open('Desktop', 'w')
        soma = 0
        Mat = Disciplina  # Variável Matriz
        Mat = []
        for i in range(qtda):
            print 'Aluno' + str(i + 1)
            l = []
            for j in range(3 + provas):
                if j == 0:
                    print 'Digite o nome do Aluno:'
                    nome = raw_input()
                    l.append(nome)
                    Disciplina.write('Nome:' + str(nome))
                if j == 1:
                    print 'Digite a matricula do Aluno:'
                    if i >= 1:
                        matr = input()
                        for k in range(qtda):
                            for p in range(3 + provas):
                                if matr == Mat[k][p]:
                                    print'Matricula já registrada'
                                else:
                                    l.append(matr)
                                    Disciplina.write(' Matricula:' + str(matr))
                    else:
                        matr = input()
                        l.append(matr)
                        Disciplina.write(' Matricula:' + str(matr))
                if j >= 2 and j < 2 + provas:
                    print 'Digite a prova' + str(j - 1) + ':'
                    prova = input()
                    l.append(prova)
                    Disciplina.write(' Prova' + str(j - 1) + ':' + str(prova))
                    soma += prova
                if j == 2 + provas:
                    M = soma / provas  # Fazendo a Média
                    l.append(M)
                    Disciplina.write('Média:' + str(M) + '\n')
            Mat.append(l)
        print Mat
        qtd = qtda
        var.write(str(provas) + '\n')
        var.write(str(qtd) + '\n')
        var.close()
        Disciplina.close()
        # Ainda tem mais um IF para acrecentar Alunos

    if n == 2:  # Deletar Alunos
        print'Digite a Disciplina:'
        Disciplina = raw_input()
        print 'Digite a matricula do aluno:'
        matr = input()
        Disciplina = open('Desktop', 'w')
        var = open('Desktop', 'r')
        for k in range(2):
            if k == 0:
                provas = int(var.readline())
            if k == 1:
                qtd = int(var.readline())
        var.close()
        for i in range(qtd):
            for j in range(5):
                if matr == Mat[i][j]:
                    del Mat[i]
        qtd -= 1
        var = open('Desktop', 'w')  # Abre dnv para Atualizar
        for k in range(2):
            if k == 1:
                var.write(qtd)
        var.close()
        for l in range(qtd):
            for o in range(3 + provas):  # Reescrevendo o Arquivo
                if o == 0:
                    Disciplina.write('Nome:' + str(Mat[i][j]))
                if o == 1:
                    Disciplina.write(' Matricula:' + str(Mat[i][j]))
                if o >= 2 and o < 2 + provas:
                    Disciplina.write(' Prova' + str(j - 1) + ':' + str(Mat[i][j]))
                if o == 2 + provas:
                    Disciplina.write('Média:' + str(Mat[i][j]) + '\n')
        Disciplina.close()
    if n == 3:
        print'Digite a Disciplina:'
        Disciplina = raw_input()
        print 'Digite a matricula do aluno:'
        mat = input()
        var = open('Desktop', 'r')
        for k in range(2):
            if k == 1:
                qtd = var.readline()
        var.close()
        int(qtd)
        Disciplina = open('Desktop', 'r')
        for i in range(qtd):
            for j in range(1, 2, 1):
                if mat == Mat[i][j]:
                    print Disciplina.readline(Mat[i])
        Disciplina.close()
    if n == 4:
        print'Digite a Disciplina:'
        Disciplina = raw_input()
        var = open('Desktop', 'r')
        for k in range(2):
            if k == 1:
                qtd = int(var.readline())
        var.close()
        Disciplina = open('Desktop', 'r')
        for i in range(qtd):
            print Disciplina.readline()[0:-1]
        Disciplina.close()
    if n == 5:
        print'Digite a Disciplina:'
        Disciplina = raw_input()
        var = open('Desktop', 'r')
        for k in range(2):
            if k == 0:
                provas = int(var.readline())
            if k == 1:
                qtd = int(var.readline())
        var.close()
        Acima = Acima(Mat, qtd, 3 + provas)
        Disciplina = open('Desktop', 'r')
        for i in range(qtd):
            for j in range(3 + provas):
                print Disciplina.readline(Acima[i][j])
        Disciplina.close()
    if n == 6:
        print'Digite a Disciplina:'
        Disciplina = raw_input()
        var = open('Desktop', 'r')
        for k in range(2):
            if k == 0:
                provas = int(var.readline())
            if k == 1:
                qtd = int(var.readline())
        var.close()
        Baixo = Baixo(Disciplina, qtd, 3 + provas)
        Disciplina = open('Desktop', 'r')
        for i in range(qtd):
            for j in range(3 + provas):
                print Disciplina.readline(Baixo[i][j])
        Disciplina.close()
    if n == 7:
        print'Digite a Disciplina'
        Disciplina = raw_input()
        var = open('Desktop', 'r')
        for k in range(2):
            if k == 0:
                provas = int(var.readline())
            if k == 1:
                qtd = int(var.readline())
        var.close()
        print 'Media Total:', Mtotal(Mat, qtd, 3 + provas)
        Temp = open('Desktop', 'w')
        for i in range(qtd):
            for j in range(0, 3 + provas, 3 + provas - 1):
                if j == 0:
                    Temp.write('Nome:' + str(Mat[i][j]))
                if j == 3 + provas - 1:
                    Temp.write(' Média:' + str(Mat[i][j]) + '\n')
        Temp.close()
        Temp = open('Desktop', 'r')
        for k in range(qtd):
            print Temp.readline()[0:-1]
        Temp.close()
    if n == 8:
        print 'Digite a disciplina:'
        Disciplina = raw_input()
        var = open('Desktop', 'r')
        for k in range(2):
            if k == 0:
                provas = int(var.readline())
            if k == 1:
                qtd = int(var.readline())
        var.close()
        print 'Digite a matricula:'
        matr = input()
        for i in range(qtd):
            for j in range(2 + provas, 3 + provas, 1):  # só as médias
                if matr == Disciplina[i][j]:
                    for w in range(2, 2 + provas):  # entre as provas e as médias
                        print 'prova' + str(w + 1) + ':'
                        Disciplina.append(input())
        Disciplina = open('Desktop', 'w')
        for p in range(qtd):
            for q in range(3 + provas):
                if o == 0:
                    Disciplina.write('Nome:' + str(Mat[i][j]))
                if o == 1:
                    Disciplina.write(' Matricula:' + str(Mat[i][j]))
                if o >= 2 and o < 2 + provas:
                    Disciplina.write(' Prova' + str(j - 1) + ':' + str(Mat[i][j]))
                if o == 2 + provas:
                    Disciplina.write('Média:' + str(Mat[i][j]) + '\n')
        Disciplina.close()
    if n == 9:
        print 'Digite a disciplina:'
        Disciplina = raw_input()
        var = open('Desktop', 'r')
        for k in range(2):
            if k == 0:
                provas = int(var.readline())
            if k == 1:
                qtd = int(var.readline())
        var.close()
        Temp = open('Desktop', 'w')
        Total = Total(Disciplina, qtd, 3 + provas)
        for i in range(qtd):
            for j in range(0, 3 + provas, 3 + provas - 1):
                if j == 0:
                    Temp.write('Nome:' + str(Total[i][j]))
                if j == 3 + provas - 1:
                    Temp.write(' Média:' + str(Total[i][j]))
        Temp.close()
        Temp = open('Desktop', 'r')
        for k in range(qtd):
            print Temp.readline()[0:-1]
        Temp.close()

print 'Saiu do Programa'
