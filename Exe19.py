area=int(input("Digite a área total a ser pintada: "))
llatas=18
coberturapl=3
valor=80
cobertura=(area/coberturapl)
total=(cobertura/llatas)
pagar=total*valor
print("Você precisa-rá de: ", total,"Latas")
print("E o valor total é: ",pagar,"R$")