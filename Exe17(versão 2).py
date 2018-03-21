sexo=int(input("Digite (1) para mulher e (2) para homem: "))
if sexo != 1 or 2:
    if sexo==1:
        altura=float(input("Digite sua altura (EXEMPLO: 1.85): "))
        peso=float(input("Digite seu peso: "))
        pesoideal=(62.1*altura-44.7)
        diferença=peso-pesoideal
        print("Seu peso ideal é: ",pesoideal,"Kg")
        if peso>pesoideal:
            print("Você precisa perder: ",diferença,"Kg para chegar no seu peso ideal.")
            print("Programa encerrado :) ")
        else:
            diferença3=diferença*(-1)
            print("Você precisa ganhar: ",diferença3,"Kg para chegar no seu peso ideal.")
            print("Programa encerrado :) ")
        quit()
    if sexo==2:
        altura2=float(input("Digite sua altura (EXEMPLO: 1.85): "))
        peso2=float(input("Digite seu peso: "))
        pesoidela2=(72.7*altura2-58)
        diferença2=peso2-pesoidela2
        print("Seu peso ideal é: ",pesoidela2,"Kg")
        if peso2>pesoidela2:
            print("Você precisa perder: ", diferença2,"Kg para chegar no seu peso ideal.")
            print("Programa encerrado :) ")
        else:
            diferença4 = diferença2*(-1)
            print("Você precisa ganhar: ",diferença4,"Kg para chegar no seu peso ideal.")
            print("Programa encerrado :) ")
        quit()
print("Alternativa","(",sexo,")","não é relacionado a nenhum.")
print("Digite apenas (1) para Mulher ou (2) para Homem.")