from fastapi import HTTPException
from notion_client import APIResponseError

from app.config.core import settings
from app.repository.notion_repository import NotionRepository
from app.schemas.notion_schemas import (
    CreateDatabase,
    CreatePage,
    UpdateRowField,
)


class NotionService:
    def __init__(self):
        self.repository = NotionRepository()

    async def create_page(self, create_page: CreatePage) -> dict:
        """Monta o payload para criação de uma página no Notion"""

        payload = {
            "parent": {"page_id": settings.NOTION_PAGE},
            "properties": {
                "title": {"title": [{"text": {"content": create_page.title}}]}
            },
            "children": [
                {"paragraph": {"rich_text": [{"text": {"content": create_page.text}}]}}
            ],
        }

        try:
            return self.repository.new_page_in_notion(payload)

        except APIResponseError as erro:
            raise HTTPException(status_code=400, detail=f"Erro no Notion: {erro!s}")

        except HTTPException:
            raise HTTPException(status_code=500, detail="Erro interno no servidor.")

    async def create_database(self, create_database: CreateDatabase):
        """Monta o payload para criação de um database no Notion"""

        notion_properties = {
            create_database.properties.principal_column: {"type": "title", "title": {}}
        }
        for coluna in create_database.properties.text_column:
            notion_properties[coluna] = {"type": "rich_text", "rich_text": {}}

        for column_name, options in create_database.properties.selection_column.items():
            notion_properties[column_name] = {
                "type": "select",
                "select": {"options": [{"name": op} for op in options]},
            }

        payload = {
            "parent": {"type": "page_id", "page_id": create_database.id_page},
            "title": [{"type": "text", "text": {"content": create_database.title}}],
            "is_inline": True,
            # Injeta as colunas estruturadas aqui
            "initial_data_source": {"properties": notion_properties},
        }

        try:
            return self.repository.new_database_in_notion(payload)

        except APIResponseError as erro:
            raise HTTPException(status_code=400, detail=f"Erro no Notion: {erro!s}")

        except HTTPException:
            raise HTTPException(status_code=500, detail="Erro interno no servidor.")

    async def list_rows(self, data_source_id: str):
        """Retorna todas as linhas de um database"""
        try:
            response = ...
            return ...

        except ValueError:
            raise HTTPException(status_code=500, detail="Erro interno no servidor.")

    async def update_single_field(self, page_id: str, update_data: UpdateRowField):
        """Monta o payload para atualizar uma única coluna na linha escolhida"""

        notion_properties = {}

        if update_data.column_type == ...:
            notion_properties[update_data.column_name] = {
                "title": [{"text": {"content": ...}}]
            }
        elif update_data.column_type == ...:
            notion_properties[update_data.column_name] = {
                "rich_text": [{"text": {"content": ...}}]
            }
        elif update_data.column_type == ...:
            notion_properties[update_data.column_name] = {"select": {"name": ...}}

        try:
            return ...

        except APIResponseError as erro:
            raise HTTPException(status_code=400, detail=f"Erro no Notion: {erro!s}")
