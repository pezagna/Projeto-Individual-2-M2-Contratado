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

def cadastro():
    continuar = 1
    while continuar !=0:
        nome = input("Digite o nome do candidato: ")
        curriculo = input("Envie o currículo do candidato: ")
        vaga1.update({nome:curriculo})
        for chave,valor in vaga1.items():
            if "python" and "programação" and "desenvolvimento" in valor:
                print(f"\nO candidato {chave} está qualificado para a vaga")
            else:
                print(f"\nO candidato {chave} não está qualificado para a vaga.")
        continuar = int(input("Digite 1 para continuar. Digitte 0 para encerrar: "))
    print(vaga1)

    
cadastro()
