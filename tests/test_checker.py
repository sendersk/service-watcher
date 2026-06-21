from service_watcher.checker import check_service


def test_check_service_returns_result() -> None:
    result = check_service(
        {
            "name": "Example",
            "url": "https://example.com"
        }
    )

    assert "status" in result
    assert "checked_at" in result