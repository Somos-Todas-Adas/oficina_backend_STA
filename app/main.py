from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.notion_route import notion_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(notion_router, prefix="/api/v1")


@app.get("/")
async def root():
    return {"message": "Hello from oficina-backend-sta!", "docs": "/docs"}
