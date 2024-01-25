print("===============================")
print("      CALCULADORA SIMPLES      ")
print("===============================")

while True: 
  try: 
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. SAIR \n")

    opcao = int(input("Qual operação gostaria de fazer? "))

    if(opcao < 5): 
      n1 = float(input("Informe o primeiro valor: "))
      n2 = float(input("Informe o segundo valor: "))
      print("\n")
    elif(opcao == 5):
        print("Saindo...")
        break

    if opcao == 1:
      resultado = (n1 + n2)
    elif opcao == 2:
      resultado = (n1 - n2)
    elif opcao == 3:
      resultado = (n1 * n2)
    elif opcao == 4:
      resultado = (n1 / n2)
    
    print(f"O resultado do seu calculo é {resultado}.\n")

  except(ZeroDivisionError):
    print('Não é possível dividir um número por zero! \n')

  except(ValueError, TypeError):
    print('[ERRO] Verifique as opções e tente novamente! \n')