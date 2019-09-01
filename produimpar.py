algoritmo "semnome"
var
   imp1, imp2, prod: inteiro
inicio
      escreval ("------------------------------")
      escreval ("Calculadora de números Impares")
      Escreval ("Digite o primeiro número: ")
      leia (imp1)
      escreval ("Digite o segundo número: ")
      leia (imp2)
      escreval ("------------------------------")
      prod <- imp1 * imp2
      se (imp1=2) e (imp2=2) e (imp1=4) e (imp2=4) e (imp1=6) e (imp2=6) e (imp1=8) e (imp2=8) e (imp1=10) e (imp2=10) e (imp1=12) e (imp2=12) e (imp1=14) e (imp2=14) entao
      escreval ("Valores inválidos")
      senao
      escreval ("A multiplicação de ",imp1," e ",imp2," é: ", prod)
      fimse
      escreval ("")
fimalgoritmo