print("VERIFICADOR DE FREQUÊNCIAS CARDÍACAS")
idade = int(input("Por favor informe a sua idade"))
bpm = int(input("Por favor informe seu bpm"))

if idade <= 2:
    if bpm >= 120:
        if bpm <= 140:
            print("Batimentos normais para a idade fornecida")
        else:
            print("Batimento acima dos indicados para a idade")
    else:
        print("Batimentos abaixo dos indicados para a idade")
elif idade >= 8:
    if idade <= 17:
        if bpm >= 80:
            if bpm <= 100:
                print("Batimentos normais para a idade fornecida")
            else:
                print("Batimentos acima para a idade fornecida")
        else:
            print("Batimentos abaixo para a idade fornecida")
    if idade >= 18:
        if idade <= 60:
            if bpm >= 70:
                if bpm <= 80:
                    print("Batimentos normais para a idade fornecida")
                else:
                    print("Batimentos acima para a idade fonecida")
            else:
                print("Batimentos abaixo para a idade fornecidade")
        else:
            if bpm >= 50:
                if bpm <= 60:
                    print("Batimentos normais para a idade fornecida")
                else:
                    print("Batimentos acima para a idade fonecida")
            else:
                ("Batimentos abaixo para a idade fornecidade")
else:
    print("Não foi possível verificar os batimentos para esta idade")