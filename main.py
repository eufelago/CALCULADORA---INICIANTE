def soma(x, y):
  return x + y

def subtracao(x, y):
  return x - y

def multiplicacao(x, y):
  return x * y

def divisao(x, y):
  if y != 0:
      return x / y
  else:
      return "Erro: Divisão por zero!"

def calculadora():
  print("Selecione a operação:")
  print("1. soma")
  print("2. Subtração")
  print("3. Multiplicação")
  print("4. Divisão")

  escolha = input("Digite 1, 2, 3 ou 4: ")

  if escolha not in ('1', '2', '3', '4'):
      print("Escolha inválida. Tente novamente.")
      return

  num1 = float(input("Digite o primeiro número: "))
  num2 = float(input("Digite o segundo número: "))

  if escolha == '1':
      print(num1, "+", num2, "=", soma(num1, num2))
  elif escolha == '2':
      print(num1, "-", num2, "=", subtracao(num1, num2))
  elif escolha == '3':
      print(num1, "*", num2, "=", multiplicacao(num1, num2))
  elif escolha == '4':
      resultado = divisao(num1, num2)
      if isinstance(resultado, float):
          print(num1, "/", num2, "=", resultado)
      else:
          print(resultado)

# Chamar a função principal
calculadora()
