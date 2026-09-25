#Lista original de clientes
clientes = [
    {"nome":"Ana", "cel":"40028922", "empresa":"Volkswagen"},
    {"nome":"Gabriel", "cel":"12345678", "empresa":"Apple"},
    {"nome":"Lucas", "cel":"87654321", "empresa":"FIAT"},
    {"nome":"Patrick Jane", "cel":"24687531", "empresa":"Apple"}
]

#Código para printar um cliente da lista original
print("--->PROCURANDO CLIENTE JÁ EXISTENTE<---")
informacoes = input("Digite a empresa que deseja os clientes: ")
for cliente in clientes:
    if cliente["empresa"] == informacoes:
        print (cliente)


print("---> CADASTRANDO NOVO CLIENTE <---")
nome = input("Digite o nome que deseja cadastrar: ")
cel = input("Digite o número de telefone: ")
empresa = input("Digite a empresa: ")

novo_cliente = {
    "nome":nome,
    "cel":cel,
    "empresa":empresa
}
clientes.append (novo_cliente)
print (clientes)

#Código para remover um cliente existente
print("--->EXCLUIR CLIENTE<---")
excluir_cliente = input("Digite o nome do cliente que deseja remover: ")
for cliente in clientes:
    if cliente["nome"] == excluir_cliente:
        clientes.remove (cliente)
        break

print(clientes)