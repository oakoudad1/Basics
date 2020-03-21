#3 bits encoder dec2bin 
while True: 
	dec=int(input("\nIntroduzca un numero decimal entre el 0 y el 7: "));
	if dec<0 or dec>7:
		print("\nEl numero debe estar entre 0 y 7")
		break
	i=0
	lista= [0,0,0]
	while dec >= 1:
		a=dec%2
		dec=int(dec/2)
		lista[i] = a
		i=i+1 
	for x in lista[::-1]: #invierte la lista
		print(x, end=' ')
