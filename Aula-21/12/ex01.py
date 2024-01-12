def mostrarNumero():
  print("Escreva um número menor ou igual a 100")
  numero_valido = False
  

  while(numero_valido == False):
    num = int(input())
    if(num <= 100):
      print("Boa! O número que você escolheu é o: " + str(num))
      numero_valido = True
    else:
      print("Você precisa escolher um número menor ou igual a 100")

mostrarNumero()