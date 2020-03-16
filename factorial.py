while True:
	num=int(input("\nIntroduzca un numero: "));
	res=range(1,num+1)
	lista=list(res)
	product=1
	for x in lista:
		product = product*x
	print ("El factorial de " + str(num) + " es " + str(product))