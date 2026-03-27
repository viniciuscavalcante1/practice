"""
**Projeto 2 — Quiz Interativo de 5 Perguntas**
Crie um quiz sobre um tema que você goste 
(filmes, games, música, o que quiser). 
O programa faz 5 perguntas de múltipla escolha usando `print`, 
captura cada resposta com `input`, e no final exibe um resumo com o 
nome do jogador e quantas ele acertou. 
Não precisa usar `if` — armazene as respostas corretas como 
strings e compare com `==`, somando os acertos manualmente 
(ex: `acertos = (r1 == "b") + (r2 == "a") + ...`). 
Essa é uma forma criativa de contar com o que você já sabe.
"""

print("Qual é o Pokémon inicial de fogo em Kanto?")
print("A - Bulbassaur")
print("B - Charmander")
print("C - Squirtle")
print("D - Cyndaquil")

RIGHT_ANSWER_QUESTION_1 = "b"
answer = input("Digite a resposta: ").lower()
result_q1 = RIGHT_ANSWER_QUESTION_1 == answer

print("Qual é o Pokémon inicial de planta em Kanto?")
print("A - Bulbassaur")
print("B - Charmander")
print("C - Squirtle")
print("D - Cyndaquil")

RIGHT_ANSWER_QUESTION_2 = "a"
answer = input("Digite a resposta: ").lower()
result_q2 = RIGHT_ANSWER_QUESTION_2 == answer

RESULTS = result_q1 + result_q2

name = input("Seu nome: ")

print(f"{name}, você acertou {RESULTS}!")