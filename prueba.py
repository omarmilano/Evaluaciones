
num1 = float (raw_input("Operando: "))
op = raw_input("Operador: ")
num2 = float (raw_input ("Operando: "))

resultado = ''

if op == "+":
    resultado = num1 + num2
elif op == "-":
    resultado = num1 - num2
elif op == "*":
    resultado = num1 * num2
elif op == "/":
    if num2 !=0:
      resultado = num1 / num2
    else:
		print "no se puede dividir entre cero"
elif op == "**":
    resultado = num1 ** num2
else:
	print "el operador no es valido"

if resultado != '':
	print num1, op, num2, "=", resultado  
    

    
    
    
