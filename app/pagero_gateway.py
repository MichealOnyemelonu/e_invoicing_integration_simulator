from random import random
from .models import Invoice, InvoiceStatus, InvoiceResponse


def send_to_pagero(invoice: Invoice) -> InvoiceResponse:
    """
    Simulate sending invoice to Pagero.
    For demo: random acceptance/rejection with a simple rule.
    """

    if invoice.total_amount > 100000:
        return InvoiceResponse(
            id=invoice.id,
            status=InvoiceStatus.REJECTED,
            message="Amount exceeds allowed limit in mock gateway",
        )

    
    if random() < 0.1:
        return InvoiceResponse(
            id=invoice.id,
            status=InvoiceStatus.REJECTED,
            message="Mock network error sending to Pagero",
        )

    return InvoiceResponse(
        id=invoice.id,
        status=InvoiceStatus.ACCEPTED,
        message="Invoice successfully delivered (mock)",
    )