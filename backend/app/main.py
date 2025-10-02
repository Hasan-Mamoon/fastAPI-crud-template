from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.database.session import init_db
from app.api.v1.studentApi import router

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield
    # Shutdown code (optional)
    # e.g., close connections if needed

app = FastAPI(title="Student Management API", lifespan=lifespan)
app.include_router(router)