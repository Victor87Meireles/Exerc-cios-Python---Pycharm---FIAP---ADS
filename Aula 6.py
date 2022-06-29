valor_compra = float(input("digite o valor da compra"))
forma_pagamento = int(input("1 - Dinheiro / 2 - Cartão"))

if valor_compra > 100 and forma_pagamento==1:
    valor_compra = valor_compra * 0.9
    print("Você têm direito a um desconto")

print("O valor a pagar é {}".format(valor_compra))

