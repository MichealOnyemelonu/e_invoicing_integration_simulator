# E-Invoicing Integration Simulator (Python + FastAPI)

This project simulates an ONESOURCE ↔ Pagero style integration:

- Receives ERP-style invoices (JSON)
- Maps them to a standard model
- Validates them using country-specific rules
- Simulates sending them to a gateway (Pagero)
- Exposes status via API
- Includes automated tests and sample scripts

## Tech

- Python
- FastAPI
- Pydantic
- pytest

## How to run

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload