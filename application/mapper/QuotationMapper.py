from infrastructure.service.QuotationDTO import QuotationDTO
from datetime import datetime as dt


def to_DTO(quotations):
    quotation_DTO = QuotationDTO([], [], [], [], [])

    for x in quotations.json():
        timestamp = int(x['timestamp'])
        date = dt.utcfromtimestamp(timestamp).strftime('%d/%m\n%Y')
        quotation_DTO.date_quotation.insert(0, date)
        quotation_DTO.quotation_for_bid.insert(0, float(x['bid']))
        quotation_DTO.quotation_for_ask.insert(0, float(x['ask']))
        quotation_DTO.quotation_for_low.insert(0, float(x['low']))
        quotation_DTO.quotation_for_high.insert(0, float(x['high']))

    return quotation_DTO
