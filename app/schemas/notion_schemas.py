from pydantic import BaseModel, Field


class CreatePage(BaseModel):
    title: str = Field(..., description='Titulo da página a ser criada')
    text: str | None = Field(None, description='Adicionar texto a base')

class DatabaseProporties(BaseModel):
    # O Notion obriga ter 1 coluna principal do tipo "title"
    coluna_principal: str = Field(default="ID", description="Nome da coluna principal")
    
    # Lista simples com os nomes das colunas de texto
    colunas_texto: list[str] = Field(default=[], description="Nomes das colunas de texto")
    
    # Dicionário onde a chave é o nome da coluna e o valor é a lista de opções (Ex: {"Status": ["A Fazer", "Feito"]})
    colunas_selecao: dict[str, list[str]] = Field(default={}, description="Colunas de select e suas opções")

class CreateDatabase(BaseModel):
    id_page: str = Field(..., description='ID da página onde o database é criado')
    title: str = Field(..., description='Título da databae')
    text: str = Field(..., description='Adicionar texto a base')
    properties: DatabaseProporties


