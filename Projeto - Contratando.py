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
