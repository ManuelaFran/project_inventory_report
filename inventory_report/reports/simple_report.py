from datetime import date


class SimpleReport:
    def __init__(self) -> None:
        pass

    @staticmethod
    def generate(data):
        oldest_date = min([product["data_de_fabricacao"] for product in data])

        expiration_date = date.max
        for year in [product["data_de_validade"] for product in data]:
            year_formatting = date.fromisoformat(year)
            if (
                year_formatting >= date.today()
                and year_formatting < expiration_date
            ):
                expiration_date = year_formatting

        companies = [product["nome_da_empresa"] for product in data]
        company_name = max(set(companies), key=companies.count)

        return (
            f"Data de fabricação mais antiga: {oldest_date}\n"
            f"Data de validade mais próxima: {expiration_date}\n"
            f"Empresa com mais produtos: {company_name}"
        )
