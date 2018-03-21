#n1=nota1
#n2=nota2
#n3=nota3
n1=float(input("Digite a primeira nota: "))
n2=float(input("Digite a segunda nota: "))
n3=float(input("Digite a terceira nota: "))
media=(n1+n2+n3)/2
if(media<7):
    print("Reprovado!")
    print("Sua média foi: ", media)
else:
    print("Aprovado!")
    print("Sua média foi: ", media)
