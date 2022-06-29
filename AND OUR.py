print("VERIFICADOR DE FREQUÊNCIAS CARDÍACAS")
idade = int(input("Por favor informe a sua idade"))
bpm = int(input("Por favor informe seu bpm"))

if idade <= 2:
    if bpm >= 120 and bpm <= 140:
        print("Frequência cardiaca adequada")
    else:
        print("Frequência cardiaca inadequada")
elif idade >= 8 and idade <= 17:
    if bpm >= 80 and bpm <= 100:
        print("Frequência cardiaca adequada")
    else:
        print("Frequência cardiaca inadequada")
elif idade >= 18 and idade <= 60:
    if bpm >= 70 and bpm <= 80:
        print("Frequência cardiaca adequada")
    else:
        print("Frequência cardiaca inadequada")
elif idade >= 18 and idade <= 60:
    if bpm >= 70 and bpm <= 80:
        print("Frequência cardiaca adequada")
    else:
        print("Frequência cardiaca inadequada")
elif idade >= 60:
    if bpm >= 50 and bpm <= 60:
        print("Frequência cardiaca adequada")
    else:
        print("Frequência cardiaca inadequada")
else:
    print("Não existe dados para a idade indicada")