nota1 = int(input("nota1"))
nota2 = int(input("nota2"))

if (nota1 + nota2) >= 7:
	print("APROVADO")
else:
	recuperacao = int(input("NOTA RECUPERACAO\n"))
	if(((nota2 + nota1)/2)+recuperacao) >= 5:
		print("APROVADO APÓS A RECUPERAÇÃO")
	else:
		print("REPROVADO")