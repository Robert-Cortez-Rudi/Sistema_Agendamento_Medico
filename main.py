# Importação das funções
from config import Base, engine
from models import *
import os

# Criação das tabelas no Banco de Dados

Base.metadata.create_all(engine)

# Menu

def menu():
    print("\n--- Sistema de Agendamento Médico ---")
    print("1 - Ala Pacientes")
    print("2 - Ala Médicos")
    print("3 - Ala de Agendamentos")
    print("4 - Sair")


while True:
    menu()
    try:
        opcao = int(input("\nO que você deseja fazer ?: "))

        match opcao:

            case 1:
                ala_pacientes()
            case 2:
                ala_medicos()
            case 3:
                ala_agendamentos()
            case 4:
                break
            case _: 
                os.system("cls") # "clear" para Linux/macOS
                print("Opção invalida!")
    except ValueError:
        os.system("cls")
        print("Insira uma opção!")
