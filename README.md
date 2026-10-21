# Oficina de Backend - Integração de APIs

Este material foi elaborado pelo Projeto Somos Todas ADA para oficina de backend ministrada na Semana Nacional de Ciência e Tecnologia na Universidade Estadual do Amazonas, com o intuito de ensinar e estimular as alunas na área de backend.

## Especificações do projeto

- Linguagem: Python (>= 3.13)
- Framework: FastAPI
- Integração: API Notion
- Gerenciador de Pacotes: uv

O projeto consiste no desenvolvimento de uma API Rest para gerenciamento de tabelas no Notion. O grande diferencial será a integração com o Notion, que atuará como o banco de dados (database) da aplicação.

## Propostas da atividade

A atividade prática será focada no desenvolvimento de 6 endpoints. A arquitetura do projeto utilizará a separação de responsabilidades (camadas de rotas, serviços e repositórios) com o objetivo de mapear e implementar com clareza as operações clássicas de um CRUD (Create, Read, Update, Delete).

## Pré-requisitos

Antes de começar, certifique-se de ter instalado em sua máquina:
- [Python 3.13 ou superior](https://www.python.org/downloads/)
- [uv](https://docs.astral.sh/uv/) (Gerenciador de pacotes rápido para Python)
- Uma conta no [Notion](https://www.notion.so/) com uma integração criada (Internal Integration Token) e conectada à sua página/banco de dados.

## Configuração do Projeto (Setup)

1. **Clone o repositório:**
   Abra o seu terminal e rode o comando abaixo:
   ```bash
   git clone <url-do-seu-repositorio>
   cd <nome-da-pasta-do-repositorio>
   ```

2. **Instalação das dependências:**
   O projeto utiliza o `uv` para o gerenciamento ágil de pacotes (conforme mapeado no arquivo `uv.lock`). Para instalar todas as bibliotecas necessárias (como `fastapi`, `notion-client`, `pydantic-settings` e `uvicorn`), execute:
   ```bash
   uv sync
   ```

   __(Nota: Se você ainda não possui o uv, pode baixar [aqui](https://docs.astral.sh/uv/#__tabbed_1_1))__


3. **Configuração das Variáveis de Ambiente:**
   Na raiz do seu projeto, faça uma cópia do arquivo chamado `.env-example` e adicione as suas credenciais do Notion no arquivo .env:
   ```bash
   cp .env-example .env
   ```

## Executando a Aplicação

Para subir o servidor de desenvolvimento, utilize o Uvicorn por meio do ambiente configurado pelo `uv`:

```bash
uv run uvicorn main:app --reload
```

Com o servidor rodando, a API estará acessível em `http://127.0.0.1:8000`. 
O FastAPI gera a documentação automática interativa (Swagger UI), que você pode acessar em: `http://127.0.0.1:8000/docs`.

## Instruções da Atividade

Durante a oficina, você irá trabalhar em uma API estruturada com separação de responsabilidades. Algumas partes do código já virão prontas, outras faremos juntas, e algumas serão o seu desafio para completar!

### 1. O que já vem pronto
Estes endpoints já estão implementados no projeto para criar páginas e bancos de dados:

```python
@notion_router.post("/paginas", status_code=status.HTTP_200_OK)
async def create_page(create_page: CreatePage, service: NotionServiceDep):
    return await service.create_page(create_page)

@notion_router.post("/databases", status_code=status.HTTP_200_OK)
async def create_database(create_database: CreateDatabase, service: NotionServiceDep):
    return await service.create_database(create_database)
```

### 2. O que faremos juntas
- **Adicionar linha:** O endpoint responsável por adicionar uma nova linha (registro) ao banco de dados será construído passo a passo com a professora durante a oficina.

### 3. O que a aluna deve completar
Você encontrará alguns endpoints incompletos no código. O seu desafio é preencher as partes faltando (indicadas por `...`) para que as rotas funcionem corretamente:

**Listar as linhas do banco de dados:**
```python
@notion_router.get("/")
async def list_database_rows(database_id: str, service: ...):
    """Lista todas as linhas do banco de dados"""
    linhas = await service.list_rows(database_id)
    return ...
```

**Atualizar um campo específico:**
```python
@notion_router.patch("/")
async def update_row_field(page_id: str, update_data: ..., service: NotionServiceDep):
    """Atualiza um campo específico de uma linha usando o seu page_id"""
    resultado = await service.update_single_field(page_id, update_data)
    return ...
```

### 4. O último endpoint é livre

Sugestões

- Apagar linha da database
- Buscar item específico por meio do ID

---
**Bom código e aproveite a oficina!**