from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Configuração do Banco de Dados

user = "postgres" # usuario do sistema PostgreSQL
password = "senha" # incluir a senha do seu banco de dados
host = "localhost"
database = "Consultas_medicas" # nome do banco de dados

DATABASE_URI = f"postgresql://{user}:{password}@{host}/{database}"

engine = create_engine(DATABASE_URI)

Session = sessionmaker(bind=engine)

session = Session()

Base = declarative_base()
