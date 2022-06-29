voto1 = input("Informe qual dia da semana: SEGUNDA-FEIRA, TERÇA-FEIRA, QUARTA-FEIRA, QUINTA-FEIRA, SEXTA-FEIRA")
voto2 = input("Informe qual dia da semana: SEGUNDA-FEIRA, TERÇA-FEIRA, QUARTA-FEIRA, QUINTA-FEIRA, SEXTA-FEIRA")
voto3 = input("Informe qual dia da semana: SEGUNDA-FEIRA, TERÇA-FEIRA, QUARTA-FEIRA, QUINTA-FEIRA, SEXTA-FEIRA")
voto4 = input("Informe qual dia da semana: SEGUNDA-FEIRA, TERÇA-FEIRA, QUARTA-FEIRA, QUINTA-FEIRA, SEXTA-FEIRA")
voto5 = input("Informe qual dia da semana: SEGUNDA-FEIRA, TERÇA-FEIRA, QUARTA-FEIRA, QUINTA-FEIRA, SEXTA-FEIRA")

segunda_feira: int = 0
terça_feira = 0
quarta_feira = 0
quinta_feira = 0
sexta_feira = 0

if voto1.upper() == "SEGUNDA-FEIRA":
    segunda_feira = segunda_feira + 1
elif voto1.upper() == "TERÇA-FEIRA":
    terça_feira = terça_feira + 1
elif voto1.upper() == "QUARTA-FEIRA":
     quarta_feira = quarta_feira + 1
elif voto1.upper() == "QUINTA-FEIRA":
    quinta_feira = quinta_feira + 1
elif voto1.upper() == "SEXTA-FEIRA":
     sexta_feira = sexta_feira + 1
else:
    print("O colabor 1 digitou um dia inexistente e seu voto será desconsiderado")

print("SEGUNDA-FEIRA: {}\nTERÇA-FEIRA: {}\nQUARTA-FEIRA: {}\nQUINTA-FEIRA: {}\nSEXTA-FEIRA: {}".format(segunda_feira, terça_feira, quarta_feira, quinta_feira, sexta_feira))

if voto2.upper() == "SEGUNDA-FEIRA":
    segunda_feira = segunda_feira + 1
elif voto2.upper() == "TERÇA-FEIRA":
    terça_feira = terça_feira + 1
elif voto2.upper() == "QUARTA-FEIRA":
     quarta_feira = quarta_feira + 1
elif voto2.upper() == "QUINTA-FEIRA":
    quinta_feira = quinta_feira + 1
elif voto2.upper() == "SEXTA-FEIRA":
     sexta_feira = sexta_feira + 1
else:
    print("O colabor 2 digitou um dia inexistente e seu voto será desconsiderado")

print("SEGUNDA-FEIRA: {}\nTERÇA-FEIRA: {}\nQUARTA-FEIRA: {}\nQUINTA-FEIRA: {}\nSEXTA-FEIRA: {}".format(segunda_feira, terça_feira, quarta_feira, quinta_feira, sexta_feira))

if voto3.upper() == "SEGUNDA-FEIRA":
    segunda_feira = segunda_feira + 1
elif voto3.upper() == "TERÇA-FEIRA":
    terça_feira = terça_feira + 1
elif voto3.upper() == "QUARTA-FEIRA":
     quarta_feira = quarta_feira + 1
elif voto3.upper() == "QUINTA-FEIRA":
    quinta_feira = quinta_feira + 1
elif voto3.upper() == "SEXTA-FEIRA":
     sexta_feira = sexta_feira + 1
else:
    print("O colabor 3 digitou um dia inexistente e seu voto será desconsiderado")

print("SEGUNDA-FEIRA: {}\nTERÇA-FEIRA: {}\nQUARTA-FEIRA: {}\nQUINTA-FEIRA: {}\nSEXTA-FEIRA: {}".format(segunda_feira, terça_feira, quarta_feira, quinta_feira, sexta_feira))

if voto4.upper() == "SEGUNDA-FEIRA":
    segunda_feira = segunda_feira + 1
elif voto4.upper() == "TERÇA-FEIRA":
    terça_feira = terça_feira + 1
elif voto4.upper() == "QUARTA-FEIRA":
     quarta_feira = quarta_feira + 1
elif voto4.upper() == "QUINTA-FEIRA":
    quinta_feira = quinta_feira + 1
elif voto4.upper() == "SEXTA-FEIRA":
     sexta_feira = sexta_feira + 1
else:
    print("O colabor 4 digitou um dia inexistente e seu voto será desconsiderado")

print("SEGUNDA-FEIRA: {}\nTERÇA-FEIRA: {}\nQUARTA-FEIRA: {}\nQUINTA-FEIRA: {}\nSEXTA-FEIRA: {}".format(segunda_feira, terça_feira, quarta_feira, quinta_feira, sexta_feira))

if voto5.upper() == "SEGUNDA-FEIRA":
    segunda_feira = segunda_feira + 1
elif voto5.upper() == "TERÇA-FEIRA":
    terça_feira = terça_feira + 1
elif voto5.upper() == "QUARTA-FEIRA":
     quarta_feira = quarta_feira + 1
elif voto5.upper() == "QUINTA-FEIRA":
    quinta_feira = quinta_feira + 1
elif voto5.upper() == "SEXTA-FEIRA":
     sexta_feira = sexta_feira + 1
else:
    print("O colabor 5 digitou um dia inexistente e seu voto será desconsiderado")

print("SEGUNDA-FEIRA: {}\nTERÇA-FEIRA: {}\nQUARTA-FEIRA: {}\nQUINTA-FEIRA: {}\nSEXTA-FEIRA: {}".format(segunda_feira, terça_feira, quarta_feira, quinta_feira, sexta_feira))

if segunda_feira > terça_feira and segunda_feira > quarta_feira:
    if segunda_feira > quinta_feira and segunda_feira > sexta_feira:
        print("O dia escolhido foi Segunda-feira")
elif terça_feira > segunda_feira and terça_feira > quarta_feira:
    if terça_feira > quinta_feira and terça_feira > sexta_feira:
        print("O dia escolhido foi Terça-feira")
elif quarta_feira > segunda_feira and quarta_feira > terça_feira:
    if quarta_feira > quinta_feira and quarta_feira > sexta_feira:
        print("O dia escolhido foi Quarta-feira")
elif quinta_feira > segunda_feira and quinta_feira > terça_feira:
    if quinta_feira > quarta_feira and quinta_feira > sexta_feira:
        print("O dia escolhido foi Quinta-feira")
elif sexta_feira > segunda_feira and sexta_feira > terça_feira:
    if sexta_feira > quarta_feira and sexta_feira > quinta_feira:
        print("O dia escolhido foi Sexta-feira")