#!/usr/bin/env python
#-*- coding: utf-8 -*-
import ast # https://docs.python.org/3/library/ast.html
import sys # https://docs.python.org/3/library/sys.html

# inicio = input('Você deseja adcionar um novo contato?(S/N)')

arquivoNome = "agenda.txt"
agenda = {}
taRodando = True

agendaAlterado = {}
b = 0
n = 0
cont=0

def lerAgenda():
	'''	try:
			with open('agan.txt', 'r') as f:
				cont = 1
				n +=1
				lerTxt()
		except IOError:
			print("Nenhum contato adicionado anteriomente")'''

	arquivo = open(arquivoNome, "r")
	agenda.update(ast.literal_eval(arquivo.read()))
	arquivo.close()
	return

def gravarAgenda():
	return

def mostrarAgenda():
	conteudoTxt = ""
	x = n-1
	agendaAlterado = sorted(agenda.items(), key = lambda t: t[0])
	agendaAlterado = dict(agendaAlterado)
	for contatoLista,numeroLista in agendaAlterado.items():
		conteudoTxt += str(n-x) +')' + contatoLista + ' - ' + numeroLista + '\n'
		print(n-x,')',contatoLista, ' - ', numeroLista)
		x-=1
	arquivo = open(arquivoNome, "w")
	arquivo.wriagendaines(conteudoTxt)
	arquivo.close()

	arquivo = open(aquivoNome, "w")
	arquivo.wriagendaines(str(agendaAlterado))
	arquivo.close()

def adcionarContato():
	nome = input('Nome do contato: ').capitalize()
	numero = input('Número: ')
	agenda[nome] = numero

def alterarContato():
	exibirLista()
	contatoAlterado = input('Digite o nome do contato que quer alterar: ').capitalize()
	#while(contatoAlterado<1 or contatoAlterado>n):
		#contatoAlterado = int(input('Índice inexistente! Digite um índice válido: '))
	del agenda[contatoAlterado]
	nome = input('Novo nome: ').capitalize()
	numero = input('Novo número: ')
	agenda[nome] = numero

def excluirContato():
	n-1
	exibirLista()
	contatoExcluido = input('Digite o nome do contato que quer excluir: ').capitalize()
	#while(contatoAlterado<1 or contatoAlterado>n):
		#contatoAlterado = int(input('Índice inexistente! Digite um índice válido: '))
	del agenda[contatoExcluido]

def main():
	print('****Agenda agendaefônica em TXT****')
	menuTexto = '''Digite o número da opção desejada:
	1 - Adcionar contato
	2 - Alterar contato
	3 - Excluir contato
	4 - Encerrar programa
	'''

	while taRodando:
		opcao = input(menuTexto)
		if (opcao == "1"):
			adcionarContato()
		elif (opcao == "2"):
			alterarContato()
		elif (opcao == "3"):
			excluirContato()
		elif (opcao == "4"):
			sys.exit(1)
		else:
			print("Opção inválida!\n" + menuTexto)

main()
