from infrastructure.db.connectionDB import conn
from application.entities.CurrencyQuotationEntity import CurrencyQuotationEntity


def insert(dollarQuotation: CurrencyQuotationEntity):
    cur = conn.cursor()
    cur.execute(
        f'INSERT INTO "public".dollar_quotation VALUES ('
        f"'{str(dollarQuotation.name.name)}',"
        f"'{dollarQuotation.date}',"
        f"'{dollarQuotation.quotationBR}',"
        f"'{str(dollarQuotation.type.name)}')"
    )
    conn.commit()
    cur.close()
    conn.close()
