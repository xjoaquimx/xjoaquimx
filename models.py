from sqlalchemy import Column, Integer, String 
from database import Base

class Filmes(Base):
    __tablename__ = 'filmes' 

    id = Column('id', Integer, primary_key=True, index=True)
    nome_filme = Column('nome_filme', String)
    genero = Column('genero', String)
