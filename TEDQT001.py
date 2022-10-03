nota_1 = float(input("Digite a primeira nota:"))
nota_2 = float(input("Digite a segunda nota:"))
nota_3 = float(input("Digite a terceira nota:"))
media = (nota_1+nota_2+nota_3)/3
if media == 10:
    msg = "aprovado com distinção"
elif media <7:
    msg = "reprovado"
else:
    msg = "aprovado"
print("O aluno foi %s, e sua média alcançada foi %.2f"%(msg, media))