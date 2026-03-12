from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_valid_italian_invoice():
    payload = {
        "doc_id": "INV-IT-001",
        "country": "IT",
        "cust_vat": "IT1234567890",
        "supp_vat": "IT0987654321",
        "invoice_no": "2024-0001",
        "invoice_date": "2024-01-10",
        "amount": 100.0,
        "currency": "EUR"
    }

    resp = client.post("/invoices", json=payload)
    assert resp.status_code == 200
    body = resp.json()
    assert body["id"] == "INV-IT-001"
    assert body["status"] in ["ACCEPTED", "REJECTED"]


def test_missing_customer_vat_rejected():
    payload = {
        "doc_id": "INV-IT-002",
        "country": "IT",
        "cust_vat": "",
        "supp_vat": "IT0987654321",
        "invoice_no": "2024-0002",
        "invoice_date": "2024-01-10",
        "amount": 50.0,
        "currency": "EUR"
    }

    resp = client.post("/invoices", json=payload)
    assert resp.status_code == 200
    body = resp.json()
    assert body["status"] == "REJECTED"
    assert "Customer VAT ID is mandatory" in body["message"]