from typing import Dict, Any
from .models import Invoice


def map_erp_to_standard(erp_payload: Dict[str, Any]) -> Invoice:
    """
    Simulate mapping from an ERP-specific payload to a standard invoice model.
    """
    return Invoice(
        id=str(erp_payload["doc_id"]),
        country=erp_payload["country"],
        customer_vat_id=erp_payload.get("cust_vat", ""),
        supplier_vat_id=erp_payload.get("supp_vat", ""),
        invoice_number=erp_payload["invoice_no"],
        invoice_date=erp_payload["invoice_date"],
        total_amount=erp_payload["amount"],
        currency=erp_payload["currency"],
    )