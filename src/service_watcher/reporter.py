from pathlib import Path

REPORT_FILE = Path("reports/report.md")


def generate_report(results: list[dict]) -> str:
    REPORT_FILE.parent.mkdir(exist_ok=True)

    down_services = [
        item
        for item in results
        if item["status"] == "DOWN"
    ]

    report_lines = [
        "# Service Watcher Report",
        ""
    ]

    if not down_services:
        report_lines.append("All monitored services are available.")
    else:
        report_lines.append("Detected unavailable services:")
        report_lines.append("")

        for service in down_services:
            report_lines.append(f"- {service["name"]} ({service["url"]})")

    report_content = "\n".join(report_lines)

    REPORT_FILE.write_text(report_content, encoding="utf-8")

    return report_content