n=int(input("Digite um número inteiro: "))
def reverso(x):
 x=str(x)
 return x[::-1]
print("O reverso de %d é: "%n,reverso(n),"\n\n***Fim do programa***")