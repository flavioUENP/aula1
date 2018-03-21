deposito=float(input("Digite o valor de seu deposito: "))
jurosmes=0.007
meses=int(input("Digite quantos meses: "))
rendmes=(jurosmes*deposito)+deposito
redimento=rendmes*meses
print("Seu rendimento foi de: ", redimento, "R$")