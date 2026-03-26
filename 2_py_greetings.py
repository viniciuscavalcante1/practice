"""
**Exercício 2 — Saudação personalizada** 
Peça ao usuário que digite seu nome e, em seguida,
imprima uma saudação no formato: `Olá, [nome]! Bem-vindo(a) ao Python.`
"""

print("Hi, may I ask you your name?\n")
print("For sure! My name is: ", end="")

name = input()

print(f"\nOh, hello, {name}! Welcome to Python!")