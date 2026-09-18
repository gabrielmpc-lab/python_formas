def Círculo():
    raio = float(input("Digite o raio do circulo: "))
    real_raio = (raio * raio)

    resultado = 3.14 * real_raio
    print(f"Área: {resultado}")

def Triângulo():
    base = float(input("Digite a base do triângulo: "))
    altura = float(input("Agora digite sua altura: "))

    resultadot = (base * altura / 2)
    print(f"Área: {resultadot}")

def Quadrado():
    baseq = float(input("Digite a base do quadrado: "))
    alturaq = float(input("Agora digite a altura: "))

    resultadoq = (baseq * alturaq)
    print(f"Área: {resultadoq}")

def Retângulo():
    baser = float(input("Digite a base do retângulo: "))
    alturar = float(input("Agora digite a altura: "))

    resultador = (baser * alturar)
    print(f"Área: {resultador}")

def Paralelogramo():
    basep = float(input("Digite a base do paralelogramo: "))
    alturap = float(input("Agora digite a altura: "))

    resultadop = (basep * alturap)
    print(f"Área: {resultadop}")

def Losango():
    diagonal_menor = float(input("Digite a primeira diagonal: "))
    diagonal_maior = float(input("Agora digite a segunda diagonal: "))

    resultadol = (diagonal_maior * diagonal_menor / 2)
    print(f"Área: {resultadol}")

def Trapézio():
    base_menor = float(input("Digite a primeira base: "))
    base_maior = float(input("Agora digite a segunda base: "))
    alturat = float(input("Por fim, digite a altura: "))

    resultadot = (base_maior + base_menor) * alturat / 2
    print(f"Área: {resultadot}")

def Sair():
    print("Saindo do sistema...")

while True:

    print("CÁLCULO DE FORMAS")
    print("1 - Círculo")
    print("2 - Triângulo")
    print("3 - Quadrado")
    print("4 - Retângulo")
    print("5 - Paralelogramo")
    print("6 - Losango")
    print("7 - Trapézio")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        Círculo()

    elif opcao == "2":
        Triângulo()

    elif opcao == "3":
        Quadrado()

    elif opcao == "4":
        Retângulo()

    elif opcao == "5":
        Paralelogramo()

    elif opcao == "6":
        Losango()

    elif opcao == "7":
        Trapézio()

    elif opcao == "0":
        Sair()
        break

    else:
        print("Opção inválida. Tente novamente!")