from config import session
from datetime import datetime
from databases import Paciente, Medico, Agendamento
from models.paciente import *
from models.medico import *
import os

# Ala de Agendamentos

def ala_agendamentos():
    os.system("cls") # "clear" para Linux/macOS
    while True:
        try:
            print("\n--- Ala de Agendamentos ---")
            print("1 - Realizar um agendamento")
            print("2 - Consultar os agendamentos")
            print("3 - Cancelar um agendamento")
            print("4 - Voltar ao menu")
            opcao = int(input("Insira a opção de sua escolha: "))
            match opcao: 
                case 1:
                    criar_agendamento()
                case 2:
                    mostrar_agendamentos()
                case 3:
                    cancel_agendamento()
                case 4:
                    os.system("cls") 
                    break
                case _:
                    os.system("cls") 
                    print("Opção invalida!\n")
        except ValueError:
            os.system("cls") 
            print("\nRealize sua escolha!")

# Realização de agendamento
def criar_agendamento():
    mostrar_pacientes()
    paciente = input("\nDigite o nome do paciente que deseja fazer a consulta: ").lower()
    paciente_existe = session.query(session.query(Paciente).filter_by(nome=paciente).exists()).scalar()
    if paciente_existe:
        mostrar_medicos()
        medico = input("\nInsira o médico que fará a consulta: ").lower()
        medico_existe = session.query(session.query(Medico).filter_by(nome=medico).exists()).scalar()
        if medico_existe:
            data = input("Digite a data e hora do agendamento (formato: YYYY-MM-DD HH:MM:SS): ")
            try:
                data_marcada = datetime.strptime(data, "%Y-%m-%d %H:%M:%S")
                observacao = input("Possui alguma observação a ser feita ?: ")
                agendamento = Agendamento(nome_paciente=paciente, nome_medico=medico, data=data_marcada, observacoes=observacao)
                session.add(agendamento)
                session.commit()
                print("Agendamento concluido com sucesso!")
            except ValueError:
                print("Formato para data invalido")
        else:
            print("Médico não disponivel!")     
    else:
        print("Paciente não cadastrado!")
    session.close()

# Consulta de agendamentos
def mostrar_agendamentos():
    agendamentos = session.query(Agendamento).order_by(Agendamento.id_agendamento).all()
    if agendamentos:
        print("\n--- Lista de Agendamentos ---")
        for agendamento in agendamentos:
            print(f"Id do agendamento: {agendamento.id_agendamento} - Data do agendamento: {agendamento.data}")
            print(f"Nome do paciente: {agendamento.nome_paciente} - Nome do médico: {agendamento.nome_medico}\n")
    else:
        print("Não há agendamentos marcados!")

# Cancelamento de agendamento  
def cancel_agendamento():
    mostrar_agendamentos()
    try:
        id = int(input("Digite o id do agendamento que deseja cancelar: "))
        agendamento = session.query(Agendamento).filter(Agendamento.id_agendamento == id).first()
        if agendamento:
            session.delete(agendamento)
            session.commit()
            print("Agendamento Cancelado!")
        else:
            print("Agendamento não registrado no sistema!")
    except ValueError:
        print("Insira um valor válido!")
    session.close()
