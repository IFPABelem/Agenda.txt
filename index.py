import ast
tel = {}
telAlterado = {}
b = 0
n = 0
cont=0

def lerTxt():
    arquivo = open("BD2.txt","r")
    tel.update(ast.literal_eval(arquivo.read()))
    arquivo.close()
    exibirLista()

    
def adcionar():
    nome = input('Nome do contato: ').capitalize()
    numero = input('Número: ')
    tel[nome] = numero

def exibirLista():
    conteudoTxt = ""
    x = n-1
    telAlterado = sorted(tel.items(), key = lambda t: t[0])
    telAlterado = dict(telAlterado)
    for contatoLista,numeroLista in telAlterado.items():
        conteudoTxt += str(n-x) +')' + contatoLista + ' - ' + numeroLista + '\n'
        print(n-x,')',contatoLista, ' - ', numeroLista)
        x-=1
    arquivo = open("BD.txt", "w")
    arquivo.writelines(conteudoTxt)
    arquivo.close()

    arquivo = open("BD2.txt", "w")
    arquivo.writelines(str(telAlterado))
    arquivo.close()
def alterar():
    exibirLista()
    contatoAlterado = input('Digite o nome do contato que quer alterar: ').capitalize()
    #while(contatoAlterado<1 or contatoAlterado>n):
        #contatoAlterado = int(input('Índice inexistente! Digite um índice válido: '))
    del tel[contatoAlterado]
    nome = input('Novo nome: ').capitalize()
    numero = input('Novo número: ')
    tel[nome] = numero

def excluir():
    n-1
    exibirLista()
    contatoExcluido = input('Digite o nome do contato que quer excluir: ').capitalize()
    #while(contatoAlterado<1 or contatoAlterado>n):
        #contatoAlterado = int(input('Índice inexistente! Digite um índice válido: '))
    del tel[contatoExcluido]

print('****Agenda telefônica****')
try:
   with open('BD2.txt', 'r') as f:
       cont = 1
       n +=1
       lerTxt()
except IOError:
    print("Nenhum contato adicionado anteriomente")

if (cont == 0):
    inicio = input('Você deseja adcionar um novo contato?(S/N)')
    if (inicio == 's' or inicio == 'S'):
        n += 1
        adcionar()
        exibirLista()

while (b!=4 and n>0):
    b = int(input('Digite o número da opção desejada:\n1 - Adcionar contato\n2 - Alterar contato\n3 - Excluir contato\n4 - Encerrar programa\n'))
    while(b<1 or b>4):
        b = int(input('Opção inválida!\nDigite o número da opção desejada:\n1 - Adcionar contato\n2 - Alterar contato\n3 - Excluir contato\n4 - Encerrar programa\n'))
    if (b == 1):
        n += 1
        adcionar()
        exibirLista()

    if (b == 2):
        alterar()
        exibirLista()

    if (b == 3):
        excluir()
        exibirLista()
