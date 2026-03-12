from fastapi import FastAPI, HTTPException
from typing import Dict
from .models import InvoiceStatus, InvoiceResponse
from .mappers import map_erp_to_standard
from .validators import validate_invoice
from .pagero_gateway import send_to_pagero

app = FastAPI(title="E-Invoicing Integration Simulator")


INVOICE_STORE: Dict[str, InvoiceResponse] = {}


@app.post("/invoices", response_model=InvoiceResponse)
def submit_invoice(erp_payload: dict):
    invoice = map_erp_to_standard(erp_payload)

    valid, error = validate_invoice(invoice)
    if not valid:
        resp = InvoiceResponse(
            id=invoice.id, status=InvoiceStatus.REJECTED, message=error
        )
        INVOICE_STORE[invoice.id] = resp
        return resp

    gateway_response = send_to_pagero(invoice)
    INVOICE_STORE[invoice.id] = gateway_response
    return gateway_response


@app.get("/invoices/{invoice_id}", response_model=InvoiceResponse)
def get_invoice_status(invoice_id: str):
    if invoice_id not in INVOICE_STORE:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return INVOICE_STORE[invoice_id]