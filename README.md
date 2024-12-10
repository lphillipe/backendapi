# Livraria API

Este é meu primeiro projeto do módulo MVP da disciplina **Desenvolvimento Full Stack Básico** da PUC-Rio.

A ideia do projeto é criar um site de livraria onde você pode:  
- Inserir o nome do livro, autor, quantidade e valor.  
- Visualizar uma lista com os livros cadastrados.  
- Adicionar novos livros ou deletar os existentes.

---

## Passo a Passo para Executar

### 1. Clonando o Repositório

Clone o repositório para sua máquina local e acesse a pasta raiz do projeto pelo terminal:

```bash
git clone <URL_DO_REPOSITORIO>
cd <NOME_DA_PASTA>
```

---

### 2. Configurando o Ambiente Virtual

É recomendável usar um ambiente virtual para isolar as dependências do projeto.

#### Windows

1. **Criar o Ambiente Virtual:**
   ```cmd
   python -m venv env
   ```

2. **Ativar o Ambiente Virtual:**
   ```cmd
   .\env\Scripts\activate
   ```

#### Linux

1. **Criar o Ambiente Virtual:**
   ```bash
   python3 -m venv env
   ```

2. **Ativar o Ambiente Virtual:**
   ```bash
   source env/bin/activate
   ```

---

### 3. Instalando Dependências

Com o ambiente virtual ativado, instale as dependências descritas no arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

### 4. Executando a API

Inicie a API com o comando:

```bash
flask run --host 0.0.0.0 --port 5000
```

#### Modo de Desenvolvimento

Para recarregar automaticamente as alterações no código, use o modo de desenvolvimento com a flag `--reload`:

```bash
flask run --host 0.0.0.0 --port 5000 --reload
```

---

### 5. Verificando a API

Com a API em execução, abra o navegador e acesse o seguinte endereço para verificar a documentação e o status:

[http://localhost:5000/#/](http://localhost:5000/#/)

