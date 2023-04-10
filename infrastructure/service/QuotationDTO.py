from dataclasses import dataclass


@dataclass
class QuotationDTO:
    currency: str
    date_quotation: list
    quotation_for_bid: list
    quotation_for_ask: list
    quotation_for_low: list
    quotation_for_high: list
