#n1=nota1
#n2=nota2
#n3=nota3
#p1=peso1
#p2=peso2
#p3=peso3
n1=float(input("Digite a primeira nota: "))
n2=float(input("Digite a segunda nota: "))
n3=float(input("Digite a terceira nota: "))
p1=1
p2=2
p3=5
mediafinal=7
media=(n1*p1+n2*p2+n3*p3)/(p1+p2+p3)
if media<mediafinal:
    print("Você foi reprovado!")
    print("Sua média foi: ", media)
else:
    print("Você foi aprovado!")
    print("Sua média foi: ". media)