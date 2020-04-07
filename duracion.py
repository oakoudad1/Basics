hora = int(input("Hora de inicio (horas): "))
minu = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

minu +=dura
dato = minu // 60
minufinal = minu % 60
horaFinal = dato + hora
horaMostrada = horaFinal % 24
print("El evento finaliza a las: ", end="")
print(str(horaMostrada),str(minufinal),sep=":")
