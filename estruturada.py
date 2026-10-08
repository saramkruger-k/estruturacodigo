
nome = []
nota1 = []
nota2 = []

def cadastrar_usuario():

    nome = input("Nome do estudante: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))

nome.append(nome)
nota1.append(nota1)
nota2.append(nota2)
print("Estudante cadastrado")

def calcular_media(indice):
    return (nota1[indice] + nota2[indice]) / 2

def situacao(indice):
    media = calcular_media(indice)
    if media >= 6:
        return "Aprovado"
    elif media >= 4:
        return "Recuperação"
    else:
        return "Reprovado"

def listar():
    if len(nome) == 0:
        print("Nenhum estudante cadastrado.")   
        return
    print(f"\n{'Nome':<16}{'Nota 1':<7}{'Nota 2':<7}{'Média':<8}{'Situação':<14}")
    
    for i in range(len(nome)):
        print(f"{nome[i]:<16}{nota1[i]:<7}{nota2[i]:<7}{calcular_media(i):<8.1f}{situacao(i):<14}")

def menu():
    while True:
        print("\nMenu:")
        print("1. Cadastrar estudante")
        print("2. Listar estudantes")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            listar()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")