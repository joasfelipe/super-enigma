# palavra = input("Digite uma palavra: ")
# print(palavra)

nota = float(input("Digite uma nota: "))
media = float(input("Digite uma média: "))

if nota >= media:
    print(f"Aprovado com nota {nota}!\n"
          f"A média é {media}!")
else:
    print(f"Reprovado com nota {nota}!\n"
          f"A média é {media}!")