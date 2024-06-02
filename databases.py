from config import Base
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

# Criação da tabela dos pacientes

class Paciente(Base):
    __tablename__ = "pacientes"

    nome = Column(String, primary_key=True)
    email = Column(String, nullable=False)
    data_cadastro = Column(String, nullable=False)
    agendamentos = relationship("Agendamento", back_populates="paciente")

    def __init__(self, nome, email, data_cadastro):
        self.nome = nome
        self.email = email
        self.data_cadastro = data_cadastro


# Criação da tabela dos médicos

class Medico(Base):
    __tablename__ = "medicos"

    nome = Column(String, primary_key=True)
    especialidade = Column(String, nullable=False)
    data_registro = Column(String, nullable=False)
    agendamentos = relationship("Agendamento", back_populates="medico")

    def __init__(self, nome, especialidade, data_registro):
        self.nome = nome
        self.especialidade = especialidade
        self.data_registro = data_registro


# Criação da tabela de agendamentos

class Agendamento(Base):
    __tablename__ = "agendamentos"
    
    id_agendamento = Column(Integer, primary_key=True)
    nome_paciente = Column(String, ForeignKey("pacientes.nome"))
    nome_medico = Column(String, ForeignKey("medicos.nome"))
    data = Column(DateTime, nullable=False)
    observacoes = Column(String, nullable=True)
    
    paciente = relationship("Paciente", back_populates="agendamentos")
    medico = relationship("Medico", back_populates="agendamentos")

    def __init__(self, nome_paciente, nome_medico, data, observacoes):
        self.nome_paciente = nome_paciente
        self.nome_medico = nome_medico
        self.data = data
        self.observacoes = observacoes
 