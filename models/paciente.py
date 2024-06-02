from config import session
from datetime import datetime
from databases import Paciente
import os

# Ala Pacientes

def ala_pacientes():
    os.system("cls") # "clear" para Linux/macOS
    while True:
        try:
            print("\n--- Ala de Pacientes ---")
            print("1 - Cadastrar pacientes")
            print("2 - Listar os pacientes")
            print("3 - Remover pacientes")
            print("4 - Voltar ao menu")
            opcao = int(input("Qual serviço você deseja fazer ?: "))
            match opcao:
                case 1:
                    add_paciente()
                case 2:
                    mostrar_pacientes()
                case 3:
                    del_paciente()
                case 4:
                    os.system("cls")
                    break
                case _:
                    os.system("cls")
                    print("Opção invalida!")
        except ValueError:
            os.system("cls") 
            print("\nRealize sua escolha!")

# Cadastro de pacientes
def add_paciente():
    nome = input("\nDigite o nome do paciente: ").lower()
    email = input("Insira o email do paciente: ")
    data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    paciente = Paciente(nome, email, data)
    session.add(paciente)
    session.commit()
    print("Paciente cadastrado com sucesso!\n")
    session.close()

# Consulta de pacientes
def mostrar_pacientes():
    pacientes = session.query(Paciente).order_by(Paciente.nome).all()
    if pacientes:
        print("\n--- Lista de pacientes ---")
        for paciente in pacientes:
            print(f"Paciente: {paciente.nome} - Email: {paciente.email}")
    else:
        print("Sem pacientes cadastrados!")
    session.close()
    

# Remoção de pacientes
def del_paciente():
    mostrar_pacientes()
    nome_paciente = input("\nDigite o nome do paciente que deseja remover: ").strip().lower()
    paciente = session.query(Paciente).filter(Paciente.nome.ilike(nome_paciente)).first()
    if paciente:
        session.delete(paciente)
        session.commit()
        print("Paciente removido!")
    else:
        print("Paciente não cadastrado no sistema!")
    session.close()