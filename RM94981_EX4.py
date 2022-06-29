numero = int(input("Quantos minutos está marcando na sua tela?: "))

resultado=1

for n in range(1, numero+1):
    resultado *= n

print("Insira a senha: LIBERDADE{}".format(resultado))