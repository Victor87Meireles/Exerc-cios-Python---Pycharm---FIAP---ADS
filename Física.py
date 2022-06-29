#Esse programa recebe a distância e tempo e calcula a velocidade média
#Primeiro vamos pedir a distância e o tempo
print ("Esse é o calculador de velocidade media")
distancia = input("digite a distância percorrida: ")
tempo = input("digite o tempo percorrido: ")
#Realizando o calculo
velocidade_media = float(distancia) / float(tempo)
#Exibindo a mensagem
print("A velocidade media calculada foi de {:.2f}  Km/h".format(velocidade_media))
