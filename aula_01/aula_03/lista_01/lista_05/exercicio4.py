def Aprovado(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media >= 60


nota1 = float(input("Digite a nota do primeiro bimestre: "))
nota2 = float(input("Digite a nota do segundo bimestre: "))

if Aprovado(nota1, nota2):
    print("Você está aprovado!")
else:
    print("Prova final.")

Aprovado(nota1,nota2)
