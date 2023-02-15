##################################################################
#  Projeto individual 2 - Módulo 2 - Contratando!                #
#  Data de criação: 14/02/2023                                   #
#  Criação e edição:  Robson da Silva                            #
#  versão = '3.11' 64 bit                                        #
#########################################################################################
#                                                                                       #
#     Contexto:                                                                         #
#                                                                                       #
#     Uma empresa de recrutamento recebeu muitos currículos                             #
#   para determinadas vagas e agora precisa classificar                                 #
#   quantos candidatos tem o perfil necessário e quantos                                #
#   candidatos estão concorrendo a cada vaga específica.                                #
#                                                                                       #
#   Seguindo as informações do contexto, a seguinte linha de código foi projetada.      #
#                                                                                       #
#########################################################################################

vaga1 = {}
aproved = {}
notaproved= {}

vaga2 = {}
aproved2 = {}
notaproved2 = {}
def cadastro():
    continuar = 1
    while continuar !=0:
        nome = input("Digite o nome do candidato: ")
        curriculo = input("Envie o currículo do candidato: ")
        vaga1.update({nome:curriculo})
        for chave,valor in vaga1.items():
            if "Python" and "programação" and "desenvolvimento" in valor:
                print(f"\nCandidato {chave} está qualificado para a vaga")
                aproved.update({chave:valor})
            else:
                print(f"\nCandidato {chave} não está qualificado para a vaga.")
                notaproved.update({nome:curriculo})
                
            
        continuar = int(input("\nDigite 1 para continuar. Digitte 0 para encerrar: "))
    for chave,valor in aproved.items():
        print(f"\nCandidato aprovado:\nNome: {chave}\nCurrículo: {valor}\n")
    for chave,valor in notaproved.items():
        print(f"Candidato não aprovado: \nNome: {chave}\nCurrículo: {valor}\n")

def cadastro2():
    continuar = 1
    while continuar !=0:
        nome = input("Digite o nome do candidato: ")
        curriculo = input("Envie o currículo do candidato: ")
        vaga2.update({nome:curriculo})
        for chave,valor in vaga2.items():
            if "Análise de dados" and "dados" and "SQL" in valor:
                print(f"\nCandidato {chave} está qualificado para a vaga.\n")
                aproved2.update({chave:valor})
            else:
                print(f"Candidato {chave} não está qualificado para a vaga.\n")
                notaproved2.update({nome:curriculo})
                
        continuar = int(input("Digite 1 para continuar. Digitte 0 para encerrar: "))
    for chave,valor in aproved2.items():
        print(f"\nCandidato aprovado:\nNome: {chave}\nCurrículo: {valor}\n")
    for chave,valor in notaproved2.items():
        print(f"Candidato não aprovado: \nNome: {chave}\nCurrículo: {valor}\n")
    
def menuvaga1():
    opcao=0
    while opcao !="3":
        print("\n""1. Cadastrar currículo""\n""2. Listar candidatos" "\n""3. Voltar" "\n")
        try :
            opcao = int(input("\n""Opção: "))
        except:
            print ("\n""Opcão inválida, tente novamente.")
            continue
        if  (opcao==1):
            cadastro()
        elif(opcao==2):
            print(f"\nLista de candidatos aprovados para a Vaga 1 - Requisitos: Python, Programação, Desenvolvimento.")
            for chave,valor in aproved.items():
                print(f"Candidato aprovado:\nNome: {chave}\nCurrículo: {valor}\n")
            print(f"Quantidade de candidatos aprovados para vaga 1: {len(aproved)} ")                
        elif(opcao==3):
            break
        else:
            print ("\n""Opcão inválida, tente novamente.")
def menuvaga2():
    opcao=0
    while opcao !="3":
        print("\n""1. Cadastrar currículo""\n""2. Listar candidatos" "\n""3. Voltar" "\n")
        try :
            opcao = int(input("\n""Opção: "))
        except:
            print ("\n""Opcão inválida, tente novamente.")
            continue
        if  (opcao==1):
            cadastro2()
        elif(opcao==2):
            print(f"\nLista de candidatos aprovados para a Vaga 2: Requisitos: Análise de dados, Dados, SQL.")
            for chave,valor in aproved2.items():
                print(f"\nCandidato aprovado:\nNome: {chave}\nCurrículo/: {valor}\n")
            print(f"Quantidade de candidatos aprovados para vaga 1: {len(aproved2)} ")                
        elif(opcao==3):
            break
        else:
            print ("\n""Opcão inválida, tente novamente.")

def menu(): #Menu Principal
    opcao=0
    while opcao !="3":
        print("\n     Selecione a vaga desejada: ""\n""\n""1. Vaga 1: Python, Programação, Desenvolvimento""\n""2. Vaga 2: Análise de dados, Dados, SQL" "\n""3. Listar todos os candidatos" "\n""4. Sair")
        try :
            opcao = int(input("\n""Opção: "))
        except:
            print ("\n""Opcão inválida, tente novamente.")
            continue
        if  (opcao==1):
            menuvaga1()
        elif(opcao==2):
            cadastro2()
        elif(opcao==3):
            print(f"\nLista de candidatos aprovados para a Vaga 1 - Requisitos: Python, Programação, Desenvolvimento.")
            for chave,valor in aproved.items():
                print(f"Candidato aprovado:\nNome: {chave}\nCurrículo: {valor}\n")
            print(f"Quantidade de candidatos aprovados: {len(aproved)} ")
            print("="*200)
            print(f"\nLista de candidatos aprovados para a Vaga 2: Requisitos: Análise de dados, Dados, SQL.")
            for chave,valor in aproved2.items():
                print(f"\nCandidato aprovado:\nNome: {chave}\nCurrículo: {valor}\n")            
            print(f"Quantidade de candidatos aprovados: {len(aproved2)} ")
            print("="*200)
        elif(opcao==4):
            print("\n""Aplicativo encerrado.\n")
            break
        else:
            print ("\n""Opcão inválida, tente novamente.")
menu()
