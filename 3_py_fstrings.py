"""
**Exercício 3 — Cartão de apresentação** 
Peça ao usuário o nome, a idade e a cidade onde mora. 
Depois, exiba todas as informações em uma única mensagem formatada,
 usando f-strings. Exemplo de saída:

```
Meu nome é Ana, tenho 25 anos e moro em São Paulo.
```

"""

print("Oh, hello!")
print("I need to ask some questions about you...")
print("First of all, what's your name?")
name = input("My name is... ")
print(f"Oh, nice to meet you, {name}! That's a wonderful name!")
print(f"So, {name}, how old are you? Please, just tell me the whole number.")
age = input("I'm... ")
print(f"{age}, huh? I'm envy of you, {name}! And the final question, I promise!")
print("Ready?")
prompt = input()
print("Where do you live?")
place = input("I live in... ")
print(f"So your name is {name}, you're {age} years old and live in {place}, right?")


