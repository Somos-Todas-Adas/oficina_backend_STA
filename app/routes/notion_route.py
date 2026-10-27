from typing import Annotated

from fastapi import APIRouter, Depends, status

from app.schemas.notion_schemas import (
    CreateDatabase,
    CreatePage,
)
from app.services.notion_service import NotionService

notion_router = APIRouter()

NotionServiceDep = Annotated[NotionService, Depends()]


@notion_router.post("/paginas", status_code=status.HTTP_200_OK)
async def create_page(create_page: CreatePage, service: NotionServiceDep):
    return await service.create_page(create_page)


@notion_router.post("/databases", status_code=status.HTTP_200_OK)
async def create_database(create_database: CreateDatabase, service: NotionServiceDep):
    return await service.create_database(create_database)


@notion_router.get("/")
async def list_database_rows(data_source_id: str, service: ...):
    """Lista todas as linhas do banco de dados"""
    linhas = await service.list_rows(...)
    return ...


@notion_router.patch("/")
async def update_row_field(page_id: str, update_data: ..., service: NotionServiceDep):
    """Atualiza um campo específico de uma linha usando o seu page_id"""
    resultado = await service.update_single_field(page_id, update_data)
    return ...
