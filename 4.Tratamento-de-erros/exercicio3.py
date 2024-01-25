print('==============================')
print('          FORMULÁRIO          ')
print('==============================')

nome = input('Por favor, informe seu nome completo: ')

while True:
  try:
    ano_nascimento = int(input('Por favor, informe seu ano de nascimento: '))
    ano_atual = 2023
    
    if(ano_nascimento < ano_atual and ano_nascimento > 1922):
      idade = ano_atual - ano_nascimento
      print(f'Seu nome completo é {nome} e você tem {idade} anos.')
      break
    else:
      print('Você digitou um ano inválido! Tente novamente.\n')

  except(ValueError, TypeError):
    print('[ERRO] Caractere inválido! Tente novamente.\n')