try:
	n=0
	n=int(input("\nIntroduzca un numero: "));
except ValueError:
	print("\nEso no es un numero")
	exit()
a=0
b=1
z=0
for i in range(n):
	z=a+b
	print(str(z))
	a=b
	b=z
print("\nEstos son los primeros " + str(n) + " numeros de la sucesión de Fibonacci")
	
