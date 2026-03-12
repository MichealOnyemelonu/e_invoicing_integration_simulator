from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional
from datetime import date


class InvoiceStatus(str, Enum):
    PENDING = "PENDING"
    SENT = "SENT"
    REJECTED = "REJECTED"
    ACCEPTED = "ACCEPTED"


class Invoice(BaseModel):
    id: str
    country: str = Field(..., description="ISO country code, e.g. IT, DE, PL")
    customer_vat_id: str
    supplier_vat_id: str
    invoice_number: str
    invoice_date: date
    total_amount: float
    currency: str


class InvoiceResponse(BaseModel):
    id: str
    status: InvoiceStatus
    message: Optional[str] = None