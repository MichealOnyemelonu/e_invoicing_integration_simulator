import json
import requests
from pathlib import Path

API_URL = "http://127.0.0.1:8000/invoices"


def send_invoice(path: Path):
    with open(path, "r") as f:
        payload = json.load(f)

    resp = requests.post(API_URL, json=payload)
    print(path.name, "->", resp.status_code, resp.json())


def main():
    data_dir = Path(__file__).parent.parent / "data"
    for file in data_dir.glob("*.json"):
        send_invoice(file)


if __name__ == "__main__":
    main()