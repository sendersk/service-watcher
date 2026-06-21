from checker import check_service
from config import load_services
from reporter import generate_report
from storage import save_results


def main() -> None:
    services = load_services()

    results = [
        check_service(service)
        for service in services
    ]

    save_results(results)

    report = generate_report(results)

    print(report)


if __name__ == "__main__":
    main()