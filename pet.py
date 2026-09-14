animais = []
donos = []
consultas = []

def cadastrar_dono():
    print("\n CADASTRAR DONO")

    nome = input("Nome: ")
    telefone = input("Telefone: ")

    dono = {
        "id": len(donos) + 1,
        "nome": nome,
        "telefone": telefone
    }

    donos.append(dono)

    print("\nDono cadastrado com sucesso!")


def listar_donos():
    print("\nLISTA DE DONOS")

    if not donos:
        print("Nenhum dono cadastrado.")
        return

    for dono in donos:
        print(
            f"ID: {dono['id']} | "
            f"Nome: {dono['nome']} | "
            f"Telefone: {dono['telefone']}"
        )

def cadastrar_animal():
    print("\n CADASTRAR ANIMAL")

    nome = input("Nome do animal: ")
    especie = input("Espécie: ")
    raca = input("Raça: ")
    idade = input("Idade: ")

    listar_donos()

    if donos:
        dono_id = int(input("ID do dono: "))
    else:
        print("Nenhum dono cadastrado.")
        return

    animal = {
        "id": len(animais) + 1,
        "nome": nome,
        "especie": especie,
        "raca": raca,
        "idade": idade,
        "dono_id": dono_id
    }

    animais.append(animal)

    print("\nAnimal cadastrado com sucesso!")


def listar_animais():
    print("\nLISTA DE ANIMAIS")

    if not animais:
        print("Nenhum animal cadastrado.")
        return

    for animal in animais:

        dono_nome = "Não encontrado"

        for dono in donos:
            if dono["id"] == animal["dono_id"]:
                dono_nome = dono["nome"]

        print(
            f"ID: {animal['id']} | "
            f"Nome: {animal['nome']} | "
            f"Espécie: {animal['especie']} | "
            f"Raça: {animal['raca']} | "
            f"Idade: {animal['idade']} | "
            f"Dono: {dono_nome}"
        )


def cadastrar_consulta():
    print("\n CADASTRAR CONSULTA")

    if not animais:
        print("Nenhum animal cadastrado.")
        return

    listar_animais()

    animal_id = int(input("ID do animal: "))
    data = input("Data: ")
    horario = input("Horário: ")
    veterinario = input("Veterinário: ")
    motivo = input("Motivo da consulta: ")

    consulta = {
        "id": len(consultas) + 1,
        "animal_id": animal_id,
        "data": data,
        "horario": horario,
        "veterinario": veterinario,
        "motivo": motivo
    }

    consultas.append(consulta)

    print("\nConsulta cadastrada com sucesso!")


def listar_consultas():
    print("\nLISTA DE CONSULTAS")

    if not consultas:
        print("Nenhuma consulta cadastrada.")
        return

    for consulta in consultas:

        animal_nome = "Não encontrado"

        for animal in animais:
            if animal["id"] == consulta["animal_id"]:
                animal_nome = animal["nome"]

        print(
            f"ID: {consulta['id']} | "
            f"Animal: {animal_nome} | "
            f"Data: {consulta['data']} | "
            f"Horário: {consulta['horario']} | "
            f"Veterinário: {consulta['veterinario']} | "
            f"Motivo: {consulta['motivo']}"
        )

def menu():

    while True:

        print("\n")
        print("🐾 PETCARE")
        print("1 - Cadastrar dono")
        print("2 - Listar donos")
        print("3 - Cadastrar animal")
        print("4 - Listar animais")
        print("5 - Cadastrar consulta")
        print("6 - Listar consultas")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_dono()

        elif opcao == "2":
            listar_donos()

        elif opcao == "3":
            cadastrar_animal()

        elif opcao == "4":
            listar_animais()

        elif opcao == "5":
            cadastrar_consulta()

        elif opcao == "6":
            listar_consultas()

        elif opcao == "0":
            break

        else:
            print("\nOpção inválida!")

menu()