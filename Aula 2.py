pontuacao = int(input("informe a pontuacao!"))

if pontuacao > 1000:
    print("você ganhou 3gb de bonus")
elif pontuacao > 500:
    print("Você ganhou 1,5gn de bônus")
elif pontuacao > 200:
    print("Você ganhou 500mg de bônus")
else:
    print("Você nao ganhou nada!")

#>1000 3g
#>500 1,5gb
#>200 500mb
#<200 nada