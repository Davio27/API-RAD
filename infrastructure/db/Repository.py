from infrastructure.db.connectionDB import conn
from application.entities.CurrencyQuotationEntity import CurrencyQuotationEntity


def insert(dollarQuotation: CurrencyQuotationEntity):
    cur = conn.cursor()
    cur.execute(
        f'INSERT INTO "public".{str(dollarQuotation.name).lower()}_quotation VALUES ('
        f"'{str(dollarQuotation.name)}',"
        f"'{dollarQuotation.date}',"
        f"'{dollarQuotation.quotationBR}',"
        f"'{str(dollarQuotation.type.name)}')"
    )
    conn.commit()


def get_quotation_by_day(currency: str, days: str):
    
    cur = conn.cursor()
    cur.execute(
        f"""SELECT * FROM "public".{currency}_quotation WHERE date = '{days}'"""
    )
    response = cur.fetchall()

    return response
