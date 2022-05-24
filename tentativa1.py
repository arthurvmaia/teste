# Desenvolva um algoritmo que apresente as seguintes opções ao usuário:
# 1 - Cadastrar um funcionário
# 2 - Alterar um funcionário
# 2 - Listar (imprimir) todos os funcionários
# 3 - Excluir um funcionário
# 4 - Adicionar um aumento de salário


# Sabendo que todos os funcionários cadastrados precisam ter no mínimo os dados: Código do Funcionário, Nome, E-mail, Data de Admissão e Salário.
lista_funcionários = []
tupla = ()



def menu():
  print('1) Cadastrar funcionário ')
  print('2) Alterar funcionário ')
  print('3) Listar todos funcionários ')
  print('4) Excluir um funcionário ')
  print('5) Adicionar um aumento de salário ')
  print('0) Para sair do programa ' )
  number = int(input('Digite um número da alternativa > '))
  return number


def cadastrar():
  print('Olá vamos cadastrar o seu funcionário!')
  nome = (input('Digite o nome do funcionário que você quer cadastrar: '))
  email = (input('Digite o email do funcionário: '))
  codigo = (input('Digite o código que esse funcionário vai ter: '))
  admissao = (input('Digite a data de admissão desse funcionário: '))
  salario = (input('Digite o salário que ele inicialmente vai ganhar: '))
  tupla[nome] = (email,codigo,admissao,salario)
  lista_funcionários.append(tupla[nome])


def alterar():
  print('Vamos alterar os dados de um funcionário: ') 
  name = input('Digite o nome do funcionário que você quer alterar os dados')
  print('Esses são os dados do funcionário que você digitou')
  lista_funcionários[(name)]
  alteracao = input('Qual dado você quer alterar')
  novo_dado = input('Agora você quer que esse dado escolhido assuma qual valor: ')
  lista_funcionários[(name)][alteracao] = novo_dado
  print('Pronto os dados do funcionário foi alterado.')
  for dados in lista_funcionários[(name)]:
    print(dados)


def listar():
  print('Esses são todos os funcionários no atual momento:')
  print(lista_funcionários)

def excluir():
  print('Vamos excluir um funcionário.')
  name = input('Digite o nome do funcionário que você quer excluir > ')
  print('Este é o funcionário que você deseja excluir')
  print(lista_funcionários[(name)])
  lista_funcionários.remove([name])
  print('Funcionário removido!')

def aumento():
  print('Vamos fazer um aumento agora!')
  aumento_funcionario = input('Digite o nome do funcionário que você quer dar um aumento > ')
  valor_aumento = input('Quanto você quer que esse funcionário passe a ganhar agora? > ')
  lista_funcionários[(aumento_funcionario)]['salario'] = valor_aumento
  print('Aumento de salário feito!')
  print(lista_funcionários[(aumento_funcionario)])


def main():
  while menu() != 0:
    if menu() == 1:
      print(cadastrar())
    elif menu() == 2:
      print(alterar())
    elif menu() == 3:
      print(excluir())
    elif menu() == 4:
      print(aumento())

from os import system
system('cls')
menu()
system('cls')
main()









