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
			numero = colunas[0]
			nome = colunas[1]
			tabela[numero] = nome
	agenda = tabela
	return agenda

def agendaParaTexto():
	texto = ""
	for numero in agenda:
		nome = agenda[numero]
		texto += f"{nome}|{numero}\n"
	return texto

def gravarAgenda():
	texto = agendaParaTexto()
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
	except:
		texto = gravarAgenda()
	agenda = textoParaAgenda(texto)
	return agenda

def ordenarAgenda():
	tabela = sorted(agenda.items(), key = lambda x: x[1])
	agenda = dict(tabela)
	return agenda

def mostrarAgenda():
	texto = ""
	i = 0
	for numero in agenda:
		i += 1
		nome = agenda[numero]
		texto += f"{i}. {nome} {numero}\n"
	
	print("\n\nAgenda:")
	print(texto)
	return texto

def adcionarContato():
	nome = input('Nome do contato: ').capitalize()
	numero = input('Número: ')
	agenda[numero] = nome

def alterarContato():
	contato = input('Digite o número telefonico do contato que quer alterar: ').capitalize()
	del agenda[contato]
	adcionarContato()

def excluirContato():
	contato = input('Digite o número telefonico do contato que quer excluir: ').capitalize()
	del agenda[contato]

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
			adcionarContato()

	while True:
		opcao = input(menuTexto)
		if (opcao == "1"):
			mostrarAgenda()
		if (opcao == "2"):
			mostrarAgenda()
			adcionarContato()
		elif (opcao == "3"):
			mostrarAgenda()
			alterarContato()
		elif (opcao == "4"):
			mostrarAgenda()
			excluirContato()
		elif (opcao == "5"):
			gravarAgenda()
			sys.exit(1)
		else:
			print("Opção inválida!\n" + menuTexto)
			pass

		print("----- ----- ----- ----- -----")
		if (opcao != "1"):
			gravarAgenda()
main()
