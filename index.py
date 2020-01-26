#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sys # https://docs.python.org/3/library/sys.html

arquivoNome = "agenda.txt"
agenda = {}

def temNumeroNaLista(tabela, numero):
	if (numero not in tabela):
		print("Número não encotrado!")
		return False

	return True

def semNumeroNaLista(tabela, numero):
	if (numero in tabela):
		print("Número já existe!")
		return False

	return True

def textoParaAgenda(texto):
	tabela = {}
	linhas = texto.split("\n")
	for linha in linhas:
		if (linha != ""):
			colunas = linha.split("|")
			nome = colunas[0]
			numero = colunas[1]
			data = colunas[2]
			tabela[numero] = [nome, data]
	return tabela

def agendaParaTexto(tabela):
	texto = ""
	for numero in tabela:
		nome = tabela[numero][0]
		data = tabela[numero][1]
		texto += f"{nome}|{numero}|{data}\n"
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

def mostrarData(data):
	data += '00000000'
	data = data[0:8]
	data = f'{data[0:2]}/{data[2:4]}/{data[4:8]}'
	return data

def mostrarAgenda(tabela):
	texto = ""
	i = 0
	for numero in ordenarAgenda(tabela):
		i += 1
		nome = tabela[numero][0]
		data = tabela[numero][1]
		texto += f"{i}. {nome} ({mostrarData(data)}) - {numero}\n"
	
	print("\n\nAgenda:")
	print(texto)
	return texto

def adcionarContato(tabela):
	nome = input('Nome do contato: ').capitalize()
	if (len(nome) <= 1):
		print("Esse nome é muito pequeno!")
		return adcionarContato(tabela)

	data = input('Data de nascimento (DDMMAAAA):').replace('/', '');
	if (len(data) != 8):
		print('Falha, data deve contém 8 dígitos')
		return adcionarContato(tabela)
	
	contato = input('Número: ')
	if (len(contato) <= 1):
		print("Esse número é muito pequeno!")
		return adcionarContato(tabela)
	elif (semNumeroNaLista(tabela, contato)):
		tabela[contato] = ['', '']
		tabela[contato][0] = nome
		tabela[contato][1] = data
	return tabela

def alterarContato(tabela):
	contato = input('Digite o número telefonico do contato que quer alterar: ').capitalize()
	if (temNumeroNaLista(tabela, contato)):
		del tabela[contato]
		return adcionarContato(tabela)
	else:
		return tabela

def excluirContato(tabela):
	contato = input('Digite o número telefonico do contato que quer excluir: ').capitalize()
	if (temNumeroNaLista(tabela, contato)):
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
		
		if (opcao in ["1", "2", "3", "4", "5"]):
			mostrarAgenda(agenda)

		if (opcao == "2"):
			agenda = adcionarContato(agenda)
		elif (opcao == "3"):
			agenda = alterarContato(agenda)
		elif (opcao == "4"):
			agenda = excluirContato(agenda)
		elif (opcao == "5"):
			agenda = gravarAgenda(agenda)
			sys.exit(1)
		else:
			print("\nOpção inválida!\n" + menuTexto)
			pass

		print("----- ----- ----- ----- -----")
		if (opcao != "1"):
			gravarAgenda(agenda)
main()
