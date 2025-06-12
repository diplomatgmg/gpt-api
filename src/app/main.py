from fastapi import FastAPI
from app.core.config import app_config

app = FastAPI()


@app.get("/health")
async def health_check():
    return {"status": "healthy"}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(
        "main:app",
        host=app_config.host,
        port=app_config.port,
    )