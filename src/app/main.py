from fastapi import Depends, FastAPI

from app.api.v1 import v1_router
from app.core.config import app_config
from app.dependencies import verify_api_key
from common.environment.config import env_config
from common.logging.config import log_config
from common.logging.setup import setup_module_logging


setup_module_logging("app")

app = FastAPI(
    title=f"{env_config.project_name} API",
    debug=env_config.debug,
    docs_url="/api/docs",
)

app.include_router(v1_router, prefix="/api/v1", dependencies=[Depends(verify_api_key)])


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host=app_config.host,
        port=app_config.port,
        log_config=None,
        log_level=log_config.level.lower(),
        reload=env_config.debug,
    )
