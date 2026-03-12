# E‑Invoicing Integration Simulator (ERP → ONESOURCE → Pagero)

**Tech:** Python, FastAPI, Pydantic, pytest  
**Focus:** Data mapping, country-specific validation, gateway simulation, API-first design, troubleshooting

## Overview

This project simulates a production-like **e‑invoicing integration** flow used by enterprises when connecting ERPs to **ONESOURCE** and **Pagero**:

1. **Receive** ERP-style invoice JSON
2. **Map** ERP payload → standardized invoice model
3. **Validate** by **country rules** (IT/DE/PL demo)
4. **Dispatch** to a simulated Pagero gateway
5. **Track & query** invoice status via API

It showcases my approach to **implementation work**: API contracts, config-driven validation, deterministic testing, and clear observability for troubleshooting.

---

## Why This Matters (Implementation Specialist Context)

- Mirrors real client flows: ERP → Integration Layer → Compliance Gateway → Status
- Demonstrates **mapping**, **validation**, **configuration**, and **error handling**
- Provides a **sandbox** to discuss country nuances and troubleshooting approaches
- Easily extensible to more countries, schemas (UBL/Peppol), and real persistence

---

## Architecture at a Glance

- `app/mappers.py`: Maps arbitrary ERP payloads → standard invoice model
- `app/validators.py`: Country-level rule checks (JSON-configurable)
- `app/pagero_gateway.py`: Simulates acceptance/rejection & transient failures
- `app/main.py`: FastAPI endpoints for submission and status retrieval
- `tests/test_invoices.py`: Automated contract & validation tests
- `scripts/send_sample_invoices.py`: Sends sample invoices from `/data`

See diagrams below for full sequence & components.

---

## Key Scenarios (Demo-Ready)

- **Valid IT invoice** → accepted or rejected by mock gateway
- **Invalid IT invoice** → rejected at validation (missing VAT)
- **PL invoice below allowed min amount** → rejected at validation
- **Gateway transient error** (optional enhancement) → retry & backoff logic

---

## Run Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload