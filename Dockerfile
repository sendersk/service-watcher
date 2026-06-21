FROM python:3.13-slim

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN pip install uv

RUN uv sync --frozen

COPY src ./src
COPY config ./config

RUN mkdir -p data reports

CMD ["uv", "run", "python", "src/service_watcher/main.py"]