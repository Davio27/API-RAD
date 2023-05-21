from dataclasses import dataclass
from application.model.enum.QuotationType import QuotationType


@dataclass
class CurrencyQuotationEntity:
    name: str
    date: str
    quotationBR: str
    type: QuotationType
