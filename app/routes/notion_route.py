from typing import Annotated

from fastapi import APIRouter, Depends, status

from app.schemas.notion_schemas import CreateDatabase, CreatePage
from app.services.notion_service import NotionService

notion_router = APIRouter()

NotionServiceDep = Annotated[NotionService, Depends()]

@notion_router.post(
    "/paginas",
    status_code=status.HTTP_200_OK
)
async def create_page(create_page: CreatePage, service: NotionServiceDep):
    return await service.create_page(create_page)

@notion_router.post(
    "/databases",
    status_code=status.HTTP_200_OK
)
async def create_database(create_database: CreateDatabase, service: NotionServiceDep):
    return await service.create_database(create_database)