"""
**Projeto 3 — Entrevista e Biografia Automática** 
O programa funciona como um "entrevistador". 
Ele faz pelo menos 8 perguntas pessoais ao usuário (
nome, apelido, cidade natal, comida favorita, sonho de infância, hobby, um medo, 
algo que ninguém sabe sobre você...). 
No final, gera um texto corrido em formato de mini-biografia em terceira pessoa, algo como:

```
Ana, mais conhecida como Aninha, nasceu em Curitiba.
Desde criança sonhava em ser astronauta. Hoje, nas horas
vagas, se dedica a colecionar vinis. Pouca gente sabe,
mas ela tem medo de palhaços...
```

Use f-strings para montar o texto final e `\n` para formatar os parágrafos.
"""

name = input("Nome: ")
nickname = input("Apelido: ")
homeland = input("Cidade natal: ")
favourite_food = input("Comida favorita: ")
child_dream = input("Sonho de infância: ")
hobby = input("Hobby: ")
fear = input("Medo: ")
nobody_knows = input("Algo que ninguém sabe: ")

print(f"""
      {name}, mais conhecido como {nickname}, nasceu em {homeland}.
      Desde criança sonhava em {child_dream}. Hoje, nas horas vagas, se dedica a {hobby}.
      Pouca gente sabe, mas ele tem medo de {fear}...
      """)

