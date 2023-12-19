def calcular(n1, n2, operador):
  if (operador == "+"):
    resultado = n1 + n2
    return resultado
  elif (operador == "-"):
    resultado = n1 - n2
    return resultado
  elif (operador == "*"):
    resultado = n1 * n2
    return resultado
  elif(operador == "/"):
    if n2 != 0:  
      resultado = n1 / n2
      return resultado
    else:
      return "Não é possível dividir por zero."
  else:
    return "Operador inválido."


n1 = int(input("Informe o primeiro valor: "))
n2 = int(input("Informe o segundo valor: "))
operador = input("Informe o tipo de operação [*, /, -, +]: ")

resultado = calcular(n1, n2, operador)
print(f"Resultado da operação: {resultado}")