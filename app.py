from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Livro
from logger import logger
from schemas import *
from flask_cors import CORS

info = Info(title="Livraria API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc, RapiDoc, RapiPDF, Scalar, ou Elements")
livro_tag = Tag(name="Livro", description="Adição, visualização e remoção de livros à base")



@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.post('/livro_adiciona', tags=[livro_tag],
          responses={"200": LivroViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_livro(form: LivroSchema):
    """Adiciona um novo Livro na base de dados

    Retorna uma representação dos livros associado.
    """
    livro = Livro(
        nome=form.nome,
        autor=form.autor,
        quantidade=form.quantidade,
        valor=form.valor)
    logger.debug(f"Adicionando livro de nome: '{livro.nome}'")
    try:
        # criando conexão com a base
        session = Session()
        # adicionando livro
        session.add(livro)
        # efetivando o comando de adição de novo livro na tabela
        session.commit()
        logger.debug(f"Adicionado livro de nome: '{livro.nome}'")
        return apresenta_livro(livro), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Livro de mesmo nome já salvo na base de dados :/"
        logger.warning(f"Erro ao adicionar livro '{livro.nome}', {error_msg}")
        return {"mesage": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar livro '{livro.nome}', {error_msg}")
        return {"mesage": error_msg}, 400


@app.get('/livros_list', tags=[livro_tag],
         responses={"200": ListagemLivrosSchema, "404": ErrorSchema})
def get_livros():
    """Lista todos os Livros cadastrados.

    Retorna uma representação da listagem de livros.
    """
    logger.debug(f"Coletando livros ")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    livros = session.query(Livro).all()

    if not livros:
        # se não há livros cadastrados
        return {"livros": []}, 200
    else:
        logger.debug(f"%d livros econtrados" % len(livros))
        # retorna a representação de produto
        print(livros)
        return apresenta_livros(livros), 200


@app.get('/livro_busca', tags=[livro_tag],
         responses={"200": LivroViewSchema, "404": ErrorSchema})
def get_livro(query: LivroBuscaSchema):
    """Faz a busca por um livro a partir do nome do livro.

    Retorna uma representação dos livros associados.
    """
    livro_nome = query.nome
    logger.debug(f"Coletando dados sobre produto #{livro_nome}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    livro = session.query(Livro).filter(Livro.nome == livro_nome).first()

    if not livro:
        # se o livro não foi encontrado
        error_msg = "Livro não encontrado na base :/"
        logger.warning(f"Erro ao buscar livro '{livro_nome}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"Livro econtrado: '{livro.nome}'")
        # retorna a representação do livro
        return apresenta_livro(livro), 200


@app.delete('/livro_del', tags=[livro_tag],
            responses={"200": LivroDelSchema, "404": ErrorSchema})
def del_livro(query: LivroBuscaSchema):
    """Deleta um livro a partir do seu nome.

    Retorna uma mensagem de confirmação da remoção.
    """
    livro_nome = unquote(unquote(query.nome))
    print(livro_nome)
    logger.debug(f"Deletando dados sobre o livro #{livro_nome}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Livro).filter(Livro.nome == livro_nome).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Livro deletado #{livro_nome}")
        return {"mesage": "Livro removido", "Livro": livro_nome}
    else:
        # se o produto não foi encontrado
        error_msg = "Livro não encontrado na base :/"
        logger.warning(f"Erro ao deletar um livro #'{livro_nome}', {error_msg}")
        return {"mesage": error_msg}, 404


