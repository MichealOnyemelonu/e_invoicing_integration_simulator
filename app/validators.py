import json
from pathlib import Path
from typing import Tuple, Optional
from .models import Invoice

RULES_PATH = Path(__file__).parent / "config" / "country_rules.json"


with open(RULES_PATH, "r") as f:
    COUNTRY_RULES = json.load(f)


def validate_invoice(invoice: Invoice) -> Tuple[bool, Optional[str]]:
    """Validate invoice against simple country-specific rules."""
    rules = COUNTRY_RULES.get(invoice.country.upper())
    if not rules:
        return False, f"No validation rules configured for country {invoice.country}"

    
    if rules.get("require_customer_vat") and not invoice.customer_vat_id:
        return False, "Customer VAT ID is mandatory"

    if rules.get("min_amount") is not None and invoice.total_amount < rules["min_amount"]:
        return False, f"Total amount must be >= {rules['min_amount']}"

    
    return True, None