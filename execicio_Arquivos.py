# Cria o arquivo "Alunos.txt"
with open("Alunos.txt", "w") as arquivo_alunos:
    arquivo_alunos.write("Vitor,8.0\n")
    arquivo_alunos.write("Clara,5.0\n")
    arquivo_alunos.write("Pedro,9.0\n")
    arquivo_alunos.write("Ana,3.5\n")
    arquivo_alunos.write("Marques,9.9\n")
    arquivo_alunos.write("Golias,4.5\n")
    arquivo_alunos.write("Pereira,7.5\n")
    arquivo_alunos.write("Alice,7.78\n")
    arquivo_alunos.write("Rick,10.0\n")
    arquivo_alunos.write("Morty,1.5\n")
    arquivo_alunos.write("Frodo,3.0\n")

# Abre o arquivo "Alunos.txt"
with open("Alunos.txt", "rt") as arquivo_alunos:
    # Cria os arquivos "Aprovados.txt" e "Reprovados.txt"
    with open("Aprovados.txt", "w") as arquivo_Aprovados, open("Reprovados.txt", "w") as arquivo_Reprovados:
        for linha in arquivo_alunos:
            aluno, nota = linha.strip().split(',')
            nota = float(nota)
            #ver se o aluno foi ou não aprovado
            if nota >= 6.0:
                arquivo_Aprovados.write(f"{aluno} : {nota}\n")
            else:
                arquivo_Reprovados.write(f"{aluno} : {nota}\n")

print("Arquivos Aprovados.txt e Reprovados.txt foram armazenados com sucesso no seu computador.")



