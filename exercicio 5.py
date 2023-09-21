pergunta1  = "Qual o melhor jogo de todos os tempos?"
pergunta2  = "Qual o melhor serviço de assinatura?"
pergunta3  = "L ou Kira?"
pergunta4  = "Playstation ou Xbox?"
pergunta5  = "Lasanha ou strogonnoff?"
pergunta6  = "qual o melhor anime?"
pergunta7  = "Qual o melhor filme de romance?"
pergunta8  = "Qual o melhor amigo do homem?"
pergunta9  = "Barbie Sereia ou Barbie Princesa?"
pergunta10 = "BK ou MC?"

resposta_certa_1 = "The last of Us"
resposta_certa_2 = "GamePass"
resposta_certa_3 = "Kira"
resposta_certa_4 = "Playstation"
resposta_certa_5 = "Lasanha"
resposta_certa_6 = "Sailor Moon"
resposta_certa_7 = "Your name"
resposta_certa_8 = "Gato"
resposta_certa_9 = "Barbie Sereia"
resposta_certa_10 = "BK"

resposta_usuario_1 = input(pergunta1)
resposta_usuario_2 = input(pergunta2)
resposta_usuario_3 = input(pergunta3)
resposta_usuario_4 = input(pergunta4)
resposta_usuario_5 = input(pergunta5)
resposta_usuario_6 = input(pergunta6)
resposta_usuario_7 = input(pergunta7)
resposta_usuario_8 = input(pergunta8)
resposta_usuario_9 = input(pergunta9)
resposta_usuario_10 = input(pergunta10)

nota = 0
if (resposta_usuario_1 == resposta_certa_1): print("Acertou"); nota = nota + 1
if (resposta_usuario_2 == resposta_certa_2): print("Acertou"); nota = nota + 1
if (resposta_usuario_3 == resposta_certa_3): print("Acertou"); nota = nota + 1
if (resposta_usuario_4 == resposta_certa_4): print("Acertou"); nota = nota + 1
if (resposta_usuario_5 == resposta_certa_5): print("Acertou"); nota = nota + 1
if (resposta_usuario_6 == resposta_certa_6): print("Acertou"); nota = nota + 1
if (resposta_usuario_7 == resposta_certa_7): print("Acertou"); nota = nota + 1
if (resposta_usuario_8 == resposta_certa_8): print("Acertou"); nota = nota + 1
if (resposta_usuario_9 == resposta_certa_9): print("Acertou"); nota = nota + 1
if (resposta_usuario_10 == resposta_certa_10): print("Acertou"); nota = nota + 1

if(nota == 0):
    print("parabens, nota dó...")
else:
    print(f"sua nota foi: {nota}")

input("Pressione Enter para continuar...")