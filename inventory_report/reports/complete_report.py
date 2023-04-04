from abc import abstractmethod
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def generate(data):
        products_by_company = {}
        stocked_quantity = ''

        for product in data:
            products_by_company[product["nome_da_empresa"]] = (
                products_by_company.get(product["nome_da_empresa"], 0) + 1
            )

        for company in products_by_company.items():
            stocked_quantity += f"- {company[0]}: {company[1]}\n"

        return (
            f"{SimpleReport.generate(data)}\n"
            "Produtos estocados por empresa:\n"
            f"{stocked_quantity}"
        )
