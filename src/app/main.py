from fastapi import FastAPI

from app.core.config import app_config
from common.environment.config import env_config


app = FastAPI(
    title=f"{env_config.project_name} API",
    docs_url="/api/docs",
)


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host=app_config.host,
        port=app_config.port,
        reload=env_config.debug,
    )
