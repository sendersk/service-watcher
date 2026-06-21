# Service Watcher

> Production-oriented HTTP service monitoring tool built

Service Watcher is a lightweight but extensible monitoring system for HTTP services and APIs.  
It checks service availability, collects structured health data, persists results, and generates incident reports.

Designed with DevOps and automation workflows in mind.

---

## 🚀 Features

- HTTP/REST service health checks
- YAML-based configuration
- Structured JSON persistence
- Markdown incident reporting
- Clean modular architecture
- Type hints + strict typing support
- Linting and formatting (Ruff)
- Static type checking (MyPy-ready)
- Test coverage with Pytest

---

## 🧱 Architecture

```
config/         # YAML configuration of services
data/           # JSON results storage
reports/        # generated incident reports
src/service_watcher/
    config.py   # YAML loader
    checker.py  # HTTP health checks
    storage.py  # JSON persistence
    reporter.py # report generation
    main.py     # orchestration layer
tests/          # unit tests
```

---

## ⚙️ Requirements

- Python 3.13+
- uv (recommended package manager)

---

## 📦 Installation

```bash
git clone https://github.com/sendersk/service-watcher.git
cd service-watcher

uv sync
```

---

## ⚙️ Configuration

Define monitored services in:

```yaml
config/services.yaml
```

Example:

```yaml
services:
  - name: GitHub API
    url: https://api.github.com

  - name: Example
    url: https://example.com
```

---

## ▶️ Usage

Run full monitoring cycle:

```bash
uv run python -m service_watcher.main
```

Output:

- JSON results → `data/checks.json`
- Markdown report → `reports/report.md`

---

## 📊 Example Report

```markdown
# Service Watcher Report

Detected unavailable services:

- Example (https://example.com)
```

---

## 🧪 Testing

Run unit tests:

```bash
uv run pytest
```

Run with coverage:

```bash
uv run pytest --cov=service_watcher
```

---

## 🔍 Code Quality

Lint code:

```bash
uv run ruff check .
```

Format code:

```bash
uv run ruff format .
```

Type checking:

```bash
uv run mypy src
```

---

## Docker

Build image:

```bash
docker build -t service-watcher .
```

Run container:

```bash
docker run --rm service-watcher
```

---

## Docker Compose

Run monitoring:

```bash
docker compose up --build
```

Generated files:

```text
data/checks.json
reports/report.md
```

---

## 🧰 Tech Stack

- Python 3.13
- httpx (HTTP client)
- PyYAML (configuration parsing)
- Pytest (testing)
- Ruff (linting + formatting)
- MyPy (type checking)

---

## 📈 Roadmap

- Async HTTP checks (httpx.AsyncClient)
- Retry mechanism with exponential backoff
- Prometheus metrics export
- Docker support
- GitHub Actions CI pipeline
- Slack/Discord alerts
- Cron-based scheduling mode

---

## 🧑‍💻 Use Cases

- Internal service monitoring
- API health checks
- DevOps automation scripts
- Lightweight alternative to full APM tools
- CI/CD health validation

---

## 🛡️ Reliability Notes

- All requests use timeout protection
- Failures are gracefully captured
- System is designed for partial failure tolerance
- No external dependencies beyond minimal HTTP stack

---

## 👤 Author

Created by Przemysław Senderski