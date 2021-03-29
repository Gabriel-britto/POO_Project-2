from processo import Processo
from advogado import Advogado


flag = 0
teste = Advogado(3)
while flag != 9:
    print("-" * 15, "Sistema Jurídico", "-" * 15)
    flag = int(input("\n1 - Objetos de teste\n2 - Processos\n3 - Remover Processo\n4 - Mostrar Tamanho\n5 - Adicionar Processo\n6 - Ordenar objetos\n7 - Buscar Processo\n8 - Custo\n9 - Sair\n> "))
    if flag == 1:
        teste.adicionar_processo_L(0, Processo("Deferido", 123, "Latrocinio", 100))
        teste.adicionar_processo_L(0, Processo("Indeferido", 400, "Assalto", 300))
        teste.adicionar_processo_L(0, Processo("Deferido", 1000, "Fraude", 400))
        teste.adicionar_processo_P(Processo("Deferido", 515, "Desacato", 1))
        teste.adicionar_processo_P(Processo("Indeferido", 3415, "Assalto a mão armada", 2))
        teste.adicionar_processo_F(Processo("Indeferido", 100, "Danos morais", 50))
        teste.adicionar_processo_F(Processo("Indeferido", 50, "Danos", 600))
        print("Objetos Adicionados!")
    elif flag == 2:
        menuelemento = 0
        while menuelemento != 4:
            print("-" * 15, "Processos", "-" * 15)
            menuelemento = int(input("1 - Pilha\n2 - Fila\n3 - Lista\n4 - Sair\n> "))
            if menuelemento == 1:
                print(teste.processosP)
            elif menuelemento == 2:
                print(teste.processosF)
            elif menuelemento == 3:
                teste.imprimir_processos()
    elif flag == 3:
        menuremover = 0
        while menuremover != 4:
            print("-" * 15, "Remover processo", "-" * 15)
            menuremover = int(input("1 - Remover Processo(Pilha)\n2 - Remover Processo(Fila)\n3 - Remover Processo(Lista)\n 4 - Sair\n> "))
            if menuremover == 1:
                teste.remover_processo_P()
                print("Processo removido")
            elif menuremover == 2:
                teste.remover_processo_F()
                print("Processo removido")
            elif menuremover == 3:
                posicao = int(input("Digite a posição do processo na lista(O processo deve existir na lista): "))
                teste.remover_processo_L(posicao)
    elif flag == 4:
        menutamanho = 0
        while menutamanho != 4:
            print("-" * 15, "Mostrar Tamanho", "-" * 15)
            menutamanho = int(input("1 - Tamanho Pilha\n2 - Tamanho Fila\n3 - Tamanho Lista\n4 - Sair\n> "))
            if menutamanho == 1:
                print("Processos Pilha tem {} objetos.".format(teste.mostrar_tam_processosP()))
            elif menutamanho == 2:
                print("Processos Fila tem {} objetos.".format(teste.mostrar_tam_processosF()))
            elif menutamanho == 3:
                print("Processos Lista tem {} objetos.".format(teste.mostrar_tam_processosL()))
    elif flag == 5:
        menuadicionar = 0
        while menuadicionar != 4:
            print("-"*15, "Adicionar Processo", "-" * 15)
            menuadicionar = int(input("1 - Adicionar em Pilha\n2 - Adicionar em Fila\n3 - Adicionar em Lista\n4 - Sair\n> "))
            if menuadicionar == 1:
                status = input("Digite o Status do processo: ")
                custo = int(input("Digite o custo do processo: "))
                descricao = input("Digite a descrição do processo: ")
                cod = int(input("Digite o Código do processo: "))
                novo = Processo(status,custo,descricao,cod)
                teste.adicionar_processo_P(novo)
            elif menuadicionar == 2:
                status = input("Digite o Status do processo: ")
                custo = int(input("Digite o custo do processo: "))
                descricao = input("Digite a descrição do processo: ")
                cod = int(input("Digite o Código do processo: "))
                novo = Processo(status,custo,descricao,cod)
                teste.adicionar_processo_F(novo)
            elif menuadicionar == 3:
                posicao = int(input("Digite a posição do processo a ser adicionado(0 se for no inicio| A lista deve ter elemenos na posição pedida): "))
                status = input("Digite o Status do processo: ")
                custo = int(input("Digite o custo do processo: "))
                descricao = input("Digite a descrição do processo: ")
                cod = int(input("Digite o Código do processo: "))
                novo = Processo(status,custo,descricao,cod)
                teste.adicionar_processo_L(posicao, novo)
    elif flag == 6:
        teste.ordena_processos()
        print("Objetos Ordenados")
    elif flag == 7:
        print("-"*15,"Buscar Processo","-"*15)
        cod = int(input("Digite o Código do Processo: "))
        saida = teste.busca_processo(cod)
        print(saida)
    elif flag == 8:
        menucusto = 0
        while menucusto != 4:
            print("-" * 15, "Menu Custo", "-" * 15)
            menucusto = int(input("1 - Menor Custo\n2 - Maior Custo\n3 - Incrementar Custo\n4 - Sair\n> "))
            if menucusto == 1:
                teste.menor_custo()
            elif menucusto == 2:
                teste.maior_custo()
            elif menucusto == 3:
                cod = int(input("Digite o Código do Processo: "))
                valor = int(input("Digite em quanto quer aumentar o custo: "))
                teste.incrementa_custo_processo(cod, valor)