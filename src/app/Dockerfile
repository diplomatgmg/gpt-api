# ============================ #
#              BASE            #
# ============================ #
FROM python:3.13-alpine AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    PYTHONPATH=/app \
    PATH="/app/.venv/bin:$PATH"

WORKDIR /app

RUN apk add --no-cache uv

COPY ./pyproject.toml ./uv.lock ./


# ============================ #
#         DEPS INSTALLING      #
# ============================ #
FROM base AS deps-dev

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-install-project --group app


# ================================= #
#           DEVELOPMENT             #
# ================================= #
FROM deps-dev AS development

WORKDIR /app/src/app

COPY ./ ./

CMD ["python", "-m", "app.main"]
