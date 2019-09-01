n1 = int(input("DIGITE UM NUMERO:\n"))
n2 = int(input("DIGITE OUTRO NUMERO:\n")) 
n3 = int(input("DIGITE MAIS OUTRO NUMERO\n"))
n4 = 0

if n1 < 0:
	n4 +=1
if n2 < 0:
	n4 +=1
if n3 < 0:
	n4 +=1

print("A QUANTIDADE DE NUMEROS NEGATIVOS É IGUAL A: \n", n4)