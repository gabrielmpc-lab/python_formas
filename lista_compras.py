#Lista de original referência
lista = ["Notebook", "Caixa de Som", "Headphone", "Xbox 360", "Iphone 14 Pro Max", "Tablet S24"]

#def para printar a lista
def listona():
    print(lista)

#def para cadastrar um novo ítem à lista de referência
def cadastrar():
    cadastro_item = input("Digite o ítem que deseja cadastrar: ")
    lista.append (cadastro_item)

#def para excluir um ítem da lista de referência
def excluir():
    excluir_item = input("Digite o ítem que deseja excluir: ")
    lista.remove (excluir_item)

#def para modificar um ítem da lista de referência
def modificar():
    item_antigo = input("Digite o nome do item que quer trocar: ")
    item_novo = input("Digite qual será o novo ítem: ")

    posicao = lista.index(item_antigo)
    lista[posicao] = item_novo

#def para sair do sistema do Supermercado
def sair():
    print("Saindo do sistema SuperMercado... ")

#def caso a opção digitada não corresponder com as apresentadas
def nem_um_nem_outro():
    print("Opção inválida, favor tente novamente. ")

while True:

#Lista de opções do SuperMercado
    print("SISTEMA SUPERMERCADO")
    print("1 - Mostrar lista")
    print("2 - Cadastrar item na lista")
    print("3 - Excluir ítem da lista")
    print("4 - Modificar ítem da lista")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        listona()

    elif opcao == "2":
        cadastrar()    
    
    elif opcao == "3":
        listona()
        excluir()

    elif opcao == "4":
        listona()
        modificar()

    elif opcao == "5":
        sair()
        break

    else:
        nem_um_nem_outro()