FROM python:3.14.0rc3-slim-trixie as builder


WORKDIR /backend

RUN apt-get update && apt-get upgrade -y \
    && apt-get install -y build-essential curl git \
    && rm -rf /var/lib/apt/lists/*

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/


Copy . .
RUN uv sync --locked

FROM python:3.14.0rc3-slim-trixie AS runtime
WORKDIR /backend
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
COPY --from=builder /app /app
ENV PATH="/backend/.venv/bin:$PATH"
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]