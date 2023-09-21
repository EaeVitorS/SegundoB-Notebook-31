perguntas = ["Burguer King é o melhor fast food?",
             "Santa é melhor que Sport?",
             "Sorvete de Baunilha é o melhor?",
             "Jesus é Bom?",
             "Giva é o melhor Prof?"
             "O pintinho Amarelinho...",
             "Arsenal é?",
             "Tlou melhor que Rd2",
             "Praia de noite é melhor?",
             "Vamos Roubar a lua?"]

Respostas = ["sim",
             "sim",
             "claro",
             "sim",
             "obvio",
             "cabe aqui na minha mão",
             "pequeno",
             "sim",
             "com certeza",
             "sim"]

nota = 0

for i in range(10):
    x = input(perguntas[i])
    if x == Respostas[i]:
        print("Tá ótimo")
        nota = nota + 1
    else:
        print("Errou, foi mlk")

if nota == 0:
    print(f"Sua pontuação foi de {nota}, Vamo ter bom gosto")
else:
    print(f"sua nota foi de {nota}, Bom gosto, irmão")




