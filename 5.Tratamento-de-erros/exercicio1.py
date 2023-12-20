#PRATICA DE TRATAMENTO DE ERRO!!

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    res = a / b

except(ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou!')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
else:
    print(f'O resultado é {res:.1f}')
finally:
    print('Volte sempre! Muito obrigado!')