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


        