sombrac=float(input("Digite o comprimento da sombra da caixa em metros,(EXEMPLO: 25, 26.4..): "))
sombrapessoa=float(input("Digite o comprimento da sua sombra metros,(EXEMPLO: 4, 4.5..): "))
altura=float(input("Digite sua altura,(EXEMPLO: 1.80..): "))
alturacaixa=altura*(sombrac/sombrapessoa)
print("A altura da caixa d'água é: ",alturacaixa,"M")