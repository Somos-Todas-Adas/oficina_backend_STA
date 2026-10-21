from notion_client import Client

from app.config.core import settings


class NotionRepository:
    def __init__(self):
        self.notion = Client(auth=settings.NOTION_TOKEN)

    def new_page_in_notion(self, payload: dict) -> dict:
        """Usa o SDK oficial para criar a página"""
        return self.notion.pages.create(**payload)

    def new_database_in_notion(self, payload: dict) -> dict:
        """Usa o SDK oficial para criar a página"""
        return self.notion.databases.create(**payload)

    def get_all_rows(self, database_id: str):
        """Busca todas as páginas contidas em um database (equivalente a 'SELECT *')"""
        return ...

    def update_row(self, page_id: str, properties: dict):
        """Atualiza propriedades de uma página específica"""
        return self.notion.pages.update(page_id=page_id, properties=properties)
