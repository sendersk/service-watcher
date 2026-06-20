import httpx
from datetime import datetime, UTC


def check_service(service: dict[str, str]) -> dict:
    try:
        response = httpx.get(
            service["url"],
            timeout=5.0,
            follow_redirects=True,
        )

        return {
            "name": service["name"],
            "url": service["url"],
            "status": "UP" if response.status_code < 400 else "DOWN",
            "http_code": response.status_code,
            "checked_at": datetime.now(UTC).isoformat(),
        }

    except Exception as exc:
        return {
            "name": service["name"],
            "url": service["url"],
            "status": "DOWN",
            "error": str(exc),
            "checked_at": datetime.now(UTC).isoformat(),
        }