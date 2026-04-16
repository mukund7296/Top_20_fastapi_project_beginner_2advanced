from fastapi import FastAPI
from .database import engine, Base
from .routes import router

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Hello Health API",
    description="Day 1 — FastAPI project with SQLite. Covers basic routes, request/response, and status codes.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.include_router(router, prefix="/api/v1")


@app.get("/", tags=["Root"])
def root():
    return {"message": "Welcome to Hello Health API 🏥", "docs": "/docs"}
