#mtq=Metros quadrados da sala
mtq=float(input("Digite quantos metros quadrados tem a sala: "))
largura=int(input("Digite a largura do taco: "))
comprimento=int(input("Digite o comprimento do taco: "))
largurametro=(largura/100)
comprimentometro=(comprimento/100)
areataco=(largurametro*comprimentometro)
total=mtq/areataco
print("A quantidade de tacos necessária para preencher a sala é: ", total)