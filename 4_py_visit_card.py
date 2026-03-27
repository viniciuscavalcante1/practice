"""
**Projeto 1 — Gerador de Cartão de Visita**
O programa pede ao usuário: nome, profissão, e-mail e telefone.
Depois, exibe um cartão formatado com bordas feitas de caracteres como 
`=`, `-` e `|`. 
O resultado deve ficar visualmente alinhado no terminal, algo como:

```
================================
|     ANA SILVA               |
|     Desenvolvedora Python   |
|     ana@email.com           |
|     (11) 99999-0000         |
================================
```

Dica: use `\n`, espaços e `end=""` para controlar o layout.
"""

name = input("Name: ")
profession = input("Profession: ")
email = input("E-mail: ")
telephone = input("Telephone: ")

LEN_NAME = len(name)
LEN_PROFESSION = len(profession)
LEN_EMAIL = len(email)
LEN_TELEPHONE = len(telephone)
MAX_LEN = max(LEN_NAME, LEN_PROFESSION, LEN_EMAIL, LEN_TELEPHONE)

fields = {
    name: LEN_NAME,
    profession: LEN_PROFESSION,
    email: LEN_EMAIL,
    telephone: LEN_TELEPHONE
    }

print((MAX_LEN + 4) * "=")
for k, v in fields.items():
    print(f"| {k}{" " * (int(MAX_LEN) - int(v))} |")
print((MAX_LEN + 4) * "=")
