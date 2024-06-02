from config import session
from datetime import datetime
from databases import Medico
import os

# Ala Médicos

def ala_medicos():
    os.system("cls") # "clear" para Linux/macOS
    while True:
        try:
            print("\n--- Ala de Médicos ---")
            print("1 - Registrar um médico")
            print("2 - Consultar os médicos")
            print("3 - Remover um médico")
            print("4 - Voltar ao menu")
            opcao = int(input("Qual será sua escolha ?: "))
            match opcao:
                case 1:
                    add_medico()
                case 2:
                    mostrar_medicos()
                case 3:
                    del_medico()
                case 4:
                    os.system("cls")
                    break
                case _:
                    os.system("cls")
                    print("Opção invalida!")
        except ValueError:
            os.system("cls") 
            print("\nRealize sua escolha!")

# Cadastro de médicos
def add_medico():
    nome = input("Digite o nome do novo médico: ").lower()
    especialidade = input("Insira sua área de especialidade: ")
    data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    medico = Medico(nome.lower(), especialidade, data)
    session.add(medico)
    session.commit()
    print("Médico cadastrado no sistema! \n")
    session.close()


# Consulta de médicos
def mostrar_medicos():
    medicos = session.query(Medico).order_by(Medico.nome).all()
    if medicos:
        print("\n--- Lista de médicos ---")
        for medico in medicos:
            print(f"Médico: {medico.nome} - Especialidade: {medico.especialidade}")
    else:
        print("Sem médicos registrados!")

# Remoção de médicos
def del_medico():
    mostrar_medicos()
    nome_medico = input("\nDigite o nome do medico: ").lower()
    medico = session.query(Medico).filter(Medico.nome.ilike(nome_medico)).first()
    if medico:
        session.delete(medico)
        session.commit()
        print("Médico removido!")
    else:
        print("Médico não registrado no sistema!")
    session.close()
