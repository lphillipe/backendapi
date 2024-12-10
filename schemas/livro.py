from pydantic import BaseModel
from typing import Optional, List
from model.livro import Livro




class LivroSchema(BaseModel):
    """ Define como um novo produto a ser inserido deve ser representado
    """
    nome: str = "Dom Casmurro"
    autor: str = "Machado de Assis"
    quantidade: Optional[int] = 1
    valor: float = 37.00


class LivroBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do produto ou id.
    """
    nome: str ="Dom Casmurro"


class ListagemLivrosSchema(BaseModel):
    """ Define como uma listagem de produtos será retornada.
    """
    livros:List[LivroSchema]


def apresenta_livros(livros: List[Livro]):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    result = []
    for livro in livros:
        result.append({
            "id": livro.id,
            "nome": livro.nome,
            "autor": livro.autor,
            "quantidade": livro.quantidade,
            "valor": livro.valor,
        })

    return {"livros": result}


class LivroViewSchema(BaseModel):
    """ Define como um produto será retornado.
    """
    id: int = 1
    nome: str = "Dom Casmurro"
    autor: str = "Machado de Assis"
    quantidade: Optional[int] = 1
    valor: float = 37.00


class LivroDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    nome: str

def apresenta_livro(livro: Livro):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    return {
        "id": livro.id,
        "nome": livro.nome,
        "autor": livro.autor,
        "quantidade": livro.quantidade,
        "valor": livro.valor,
    }
