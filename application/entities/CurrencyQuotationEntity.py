from dataclasses import dataclass
from application.model.enum.Currencies import Currencies
from application.model.enum.QuotationType import QuotationType


@dataclass
class CurrencyQuotationEntity:
    name: Currencies
    date: str
    quotationBR: str
    type: QuotationType
