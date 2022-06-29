voto1 = input("Informe qual premio deseja ganhar: PLAYSTAITON, XBOX, NINTENDO")
voto2 = input("Informe qual premio deseja ganhar: PLAYSTAITON, XBOX, NINTENDO")
voto3 = input("Informe qual premio deseja ganhar: PLAYSTAITON, XBOX, NINTENDO")
voto4 = input("Informe qual premio deseja ganhar: PLAYSTAITON, XBOX, NINTENDO")
voto5 = input("Informe qual premio deseja ganhar: PLAYSTAITON, XBOX, NINTENDO")

playstation: int = 0
xbox = 0
nintendo = 0

if voto1.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto1.upper() == "XBOX":
    xbox = xbox + 1
elif voto1.upper() == "NINTENDO":
     nintendo = nintendo + 1
else:
    print("O colabor 1 digitou um console inexistente e seu voto será desconsiderado")

print("PLAYSTATION: {}\nXBOX: {}\nNINTENDO: {}".format(playstation, xbox, nintendo))

if voto2.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto2.upper() == "XBOX":
    xbox = xbox + 1
elif voto2.upper() == "NINTENDO":
     nintendo = nintendo + 1
else:
    print("O colabor 2 digitou um console inexistente e seu voto será desconsiderado")

print("PLAYSTATION: {}\nXBOX: {}\nNINTENDO: {}".format(playstation, xbox, nintendo))

if voto3.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto3.upper() == "XBOX":
    xbox = xbox + 1
elif voto2.upper() == "NINTENDO":
     nintendo = nintendo + 1
else:
    print("O colabor 3 digitou um console inexistente e seu voto será desconsiderado")

print("PLAYSTATION: {}\nXBOX: {}\nNINTENDO: {}".format(playstation, xbox, nintendo))

if voto4.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto4.upper() == "XBOX":
    xbox = xbox + 1
elif voto4.upper() == "NINTENDO":
     nintendo = nintendo + 1
else:
    print("O colabor 4 digitou um console inexistente e seu voto será desconsiderado")

print("PLAYSTATION: {}\nXBOX: {}\nNINTENDO: {}".format(playstation, xbox, nintendo))

if voto5.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto5.upper() == "XBOX":
    xbox = xbox + 1
elif voto5.upper() == "NINTENDO":
     nintendo = nintendo + 1
else:
    print("O colabor 5 digitou um console inexistente e seu voto será desconsiderado")

print("PLAYSTATION: {}\nXBOX: {}\nNINTENDO: {}".format(playstation, xbox, nintendo))

if playstation > xbox and playstation > nintendo:
    print("O console escolhido foi Playstation")
elif xbox > playstation and xbox > nintendo:
    print("O console escolhido foi Xbox")
elif nintendo > playstation and nintendo > xbox:
    print("O console escolhido foi Nintendo")
else:
    print("Favor entrar em contato com a direção")