print("ASSINATURA DO CLIENTE")
assinatura = (input("Por favor informe a sua assinatura"))
valor_assinatura = (input("Por favor informe o valor da assinatura"))

#Basic = 50.00
#Silver = 65.00
#Gold = 80
#Platinum = 200


if assinatura == "Basic":
    print("Sua porcentagem sobre faturamento é de 30%")
    print("O  bônus que o cliente deve pagar a vocês é {}".format(600 * 0.3))
    print("O  lucro anual do cliente é {}".format(600 * 8))
if assinatura == "Silver":
    print("Sua porcentagem sobre faturamento é de 20%")
    print("O  bônus que o cliente deve pagar a vocês é {}".format(780 * 0.2))
    print("O  lucro anual do cliente é {}".format(780 * 8))
if assinatura == "Gold":
    print("Sua porcentagem sobre faturamento é de 15%")
    print("O  bônus que o cliente deve pagar a vocês é {}".format(960 * 0.15))
    print("O  lucro anual do cliente é {}".format(960 * 8))
if assinatura == "Platinum":
    print("Sua porcentagem sobre faturamento é de 5%")
    print("O  bônus que o cliente deve pagar a vocês é {}".format(2400 * 0.05))
    print("O  lucro anual do cliente é {}".format(2400 * 8))
