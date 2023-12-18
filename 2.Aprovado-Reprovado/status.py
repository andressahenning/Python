#Aprovado ou Reprovado?

nota = int(input("Qual a nota do aluno? "))

if(nota < 40):
    print("O aluno está reprovado!")
elif(nota < 70):
    print("O aluno está em recuperação!")
else:
    print("O aluno está aprovado!")
