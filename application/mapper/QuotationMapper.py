from infrastructure.service.QuotationDTO import QuotationDTO
from datetime import datetime as dt


def to_quotation_DTO(quotations):
    test = QuotationDTO([], [], [], [], [])
    
    for x in quotations.json():
        ts = int(x['timestamp'])
        xEixo = dt.utcfromtimestamp(ts).strftime('%d/%m\n%Y')
        test.xData_dolar.insert(0, xEixo)
        test.yData_dolar.insert(0, float(x['bid']))
        test.yData2_dolar.insert(0, float(x['ask']))
        test.yData3_dolar.insert(0, float(x['low']))
        test.yData4_dolar.insert(0, float(x['high']))

    return test
