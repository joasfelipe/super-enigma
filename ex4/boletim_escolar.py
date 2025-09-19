alunos = ["Lays", "Joás", "Maria", "João"]
disciplinas = ("Português", "Matemática", "Química", "Física", "História")
notas_lays = [10, 9.5, 9, 8.5]
notas_joas = [8, 7.5, 7, 6.5]
notas_maria = [6, 5.5, 5, 4.5]
notas_joao = [4, 4.5, 3, 3.5]

numero = int(input("\nLista de alunos matrículados\n\n"
                   "1 - Lays\n"
                   "2 - Joás\n"
                   "3 - João\n"
                   "4 - Maria\n\n"
                   "Digite um número da lista para ver o boletim: "))

if numero == 1:
    print(f"\nAluno(a): {alunos[0]}"
           "\n\nBoletim de notas:"
          f"\n{disciplinas[0]} = {notas_lays[0]}"
          f"\n{disciplinas[1]} = {notas_lays[1]}"
          f"\n{disciplinas[2]} = {notas_lays[2]}"
          f"\n{disciplinas[3]} = {notas_lays[3]}\n")

elif numero == 2:
    print(f"\nAluno(a): {alunos[1]}"
           "\n\nBoletim de notas:"
          f"\n{disciplinas[0]} = {notas_joas[0]}"
          f"\n{disciplinas[1]} = {notas_joas[1]}1"
          f"\n{disciplinas[2]} = {notas_joas[2]}"
          f"\n{disciplinas[3]} = {notas_joas[3]}\n")

elif numero == 3:
    print(f"\nAluno(a): {alunos[2]}"
           "\n\nBoletim de notas:"
          f"\n{disciplinas[0]} = {notas_maria[0]}"
          f"\n{disciplinas[1]} = {notas_maria[1]}"
          f"\n{disciplinas[2]} = {notas_maria[2]}"
          f"\n{disciplinas[3]} = {notas_maria[3]}\n")

elif numero == 4:
    print(f"\nAluno(a): {alunos[3]}"
           "\n\nBoletim de notas:"
          f"\n{disciplinas[0]} = {notas_joao[0]}"
          f"\n{disciplinas[1]} = {notas_joao[1]}"
          f"\n{disciplinas[2]} = {notas_joao[2]}"
          f"\n{disciplinas[3]} = {notas_joao[3]}\n")

else:
    print("\nVocê digitou um número inválido!\n")