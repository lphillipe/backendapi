from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base


class Livro(Base):
    __tablename__ = 'Livros'

    id = Column("pk_Livros", Integer, primary_key=True)
    nome = Column(String(140), unique=True)
    autor = Column(String(140))
    quantidade = Column(Integer)
    valor = Column(Float)
    
  
    def __init__(self, nome:str, autor: str, quantidade:int, valor:float ):
        """
        Cria um Livro

        Arguments:
            nome: nome do livro.
            autor: autor do livro.
            quantidade: quantidade de livros.
            valor: o valor do livro.
        """
        self.nome = nome
        self.autor = autor
        self.quantidade = quantidade
        self.valor = valor

