#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sys # https://docs.python.org/3/library/sys.html

# inicio = input('Você deseja adcionar um novo contato?(S/N)')

arquivoNome = "agenda.txt"
agenda = {}
taRodando = True

agendaAlterado = {}

def textoParaAgenda(texto):
	tabela = {}
	linhas = texto.split("\n")
	for linha in linhas:
		if (linha != ""):
			colunas = linha.split("|")
			numero = colunas[0]
			nome = colunas[1]
			tabela[numero] = nome
	return tabela

def agendaParaTexto(tabela):
	texto = ""
	for numero in tabela:
		nome = agenda[numero]
		texto += f"{nome}|{numero}\n"
	return texto

def lerAgenda():
	texto = ""
	try:
		arquivo = open(arquivoNome, "r")
		texto = arquivo.read()
		arquivo.close()
	except:
		saida = gravarAgenda(agenda)

	tabela = textoParaAgenda(texto)
	return tabela

def gravarAgenda(tabela):
	texto = agendaParaTexto(tabela)
	arquivo = open(arquivoNome, "w")
	arquivo.write(texto)
	arquivo.close()
	return texto

def ordenarAgenda(tabela):
	novaTabela = sorted(tabela.items(), key = lambda x: x[1])
	return dict(novaTabela)

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
				
#main()
