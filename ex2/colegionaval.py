nota = 4
ma = 7
mb = 5

if nota >= ma:
    print("O aluno foi aprovado! 😊")
elif nota >= mb:
    print("O aluno deverá fazer a prova final! 😓")
    nota_pf = 4
    if nota_pf >= 7:
        print("O aluno foi aprovado na prova final! 😊")
else:
    print("O aluno deverá fazer recuperação final! 😱")
    nota_rf = 4
    if nota_rf >= 5:
        print("O aluno foi aprovado na recuperação final! 😊")
    else:
        print("O aluno foi REPROVADO! 😥")