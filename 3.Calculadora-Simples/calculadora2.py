def calcular(n1, n2, operador):
  if(operador == 1):
    resultado = n1 + n2
    return resultado
  elif(operador == 2):
    resultado = n1 - n2
    return resultado
  elif(operador == 3):
    resultado = n1 * n2
    return resultado
  elif(operador == 4):
    if(n2 != 0):
      resultado = n1 / n2
      return resultado
    else:
      return "Não é possível dividir por zero!"
  else:
    return "Operador inválido!"


operador = 0

while(operador != 5):
  print("1.Soma")
  print("2.Subtração")
  print("3.Multiplicação")
  print("4.Divisão")
  print("5.SAIR")

  operador = int(input("Por favor, informe qual operação deseja realizar: "))

  if(operador in [1, 2, 3, 4]):
    n1 = int(input("Informe o primeiro valor: "))
    n2 = int(input("Informe o segundo valor: "))

    resultado = calcular(n1, n2, operador)
    print(f"Resultado da operação: {resultado} \n")

  elif(operador == 5):
    print("Saindo do programa...")

  else:
    print("Operação inválida. Por favor, escolha novamente.")