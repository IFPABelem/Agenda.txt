#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sys # https://docs.python.org/3/library/sys.html

arquivoNome = "agenda.txt"
agenda = {}

def textoParaAgenda(texto):
	tabela = {}
	linhas = texto.split("\n")
	for linha in linhas:
		if (linha != ""):
			colunas = linha.split("|")
			nome = colunas[0]
			numero = colunas[1]
			tabela[numero] = nome
	return tabela

def agendaParaTexto(tabela):
	texto = ""
	for numero in tabela:
		nome = tabela[numero]
		texto += f"{nome}|{numero}\n"
	return texto

def gravarAgenda(tabela):
	texto = agendaParaTexto(ordenarAgenda(tabela))
	arquivo = open(arquivoNome, "w")
	arquivo.write(texto)
	arquivo.close()
	return texto

def lerAgenda():
	texto = ""
	try:
		arquivo = open(arquivoNome, "r")
		texto = arquivo.read()
		arquivo.close()
	except FileNotFoundError:
		texto = gravarAgenda(agenda)
	tabela = textoParaAgenda(texto)
	return tabela

def ordenarAgenda(tabela):
	if (len(tabela) <= 0):
		return tabela

	tabela = sorted(tabela.items(), key = lambda x: x[1])
	return dict(tabela)

def mostrarAgenda(tabela):
	texto = ""
	i = 0
	for numero in ordenarAgenda(tabela):
		i += 1
		nome = tabela[numero]
		texto += f"{i}. {nome} - {numero}\n"
	
	print("\n\nAgenda:")
	print(texto)
	return texto

def adcionarContato(tabela):
	nome = input('Nome do contato: ').capitalize()
	numero = input('Número: ')
	tabela[numero] = nome
	return tabela

def alterarContato(tabela):
	contato = input('Digite o número telefonico do contato que quer alterar: ').capitalize()
	del tabela[contato]
	return adcionarContato(tabela)

def excluirContato(tabela):
	contato = input('Digite o número telefonico do contato que quer excluir: ').capitalize()
	del tabela[contato]
	return tabela

def main():
	print('****Agenda agendaefônica em TXT****')
	menuTexto = '''Digite o número da opção desejada:
	1 - Mostrar contatos
	2 - Adcionar contato
	3 - Alterar contato
	4 - Excluir contato
	5 - Encerrar programa
	'''

	agenda = lerAgenda()
	if (len(agenda) <= 0):
		terUmNovoContato = input('Você deseja adcionar um novo contato? (S/N): ').capitalize()
		if (terUmNovoContato == "S"):
			agenda = adcionarContato(agenda)
			gravarAgenda(agenda)

	while True:
		opcao = input(menuTexto)
		if (opcao == "1"):
			mostrarAgenda(agenda)
		elif (opcao == "2"):
			mostrarAgenda(agenda)
			agenda = adcionarContato(agenda)
		elif (opcao == "3"):
			mostrarAgenda(agenda)
			agenda = alterarContato(agenda)
		elif (opcao == "4"):
			mostrarAgenda(agenda)
			agenda = excluirContato(agenda)
		elif (opcao == "5"):
			agenda = gravarAgenda(agenda)
			sys.exit(1)
		else:
			print("Opção inválida!\n" + menuTexto)
			pass

		print("----- ----- ----- ----- -----")
		if (opcao != "1"):
			gravarAgenda(agenda)
main()
