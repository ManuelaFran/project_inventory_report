from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport
import pytest


@pytest.fixture
def products_list():
    return [
        {
            "id": 1,
            "nome_do_produto": "Nicotine Polacrilex",
            "nome_da_empresa": "Target Corporation",
            "data_de_fabricacao": "2021-02-18",
            "data_de_validade": "2023-09-17",
            "numero_de_serie": "CR25 1551 4467 2549 4402 1",
            "instrucoes_de_armazenamento": "instrucao 1",
        },
        {
            "id": 2,
            "nome_do_produto": "fentanyl citrate",
            "nome_da_empresa": "Target Corporation",
            "data_de_fabricacao": "2020-12-06",
            "data_de_validade": "2023-12-25",
            "numero_de_serie": "FR29 5951 7573 74OY XKGX 6CSG D20",
            "instrucoes_de_armazenamento": "instrucao 2",
        },
        {
            "id": 3,
            "nome_do_produto": "NITROUS OXIDE",
            "nome_da_empresa": "Galena Biopharma",
            "data_de_fabricacao": "2020-12-22",
            "data_de_validade": "2024-11-07",
            "numero_de_serie": "CZ09 8588 0858 8435 9140 2695",
            "instrucoes_de_armazenamento": "instrucao 3",
        },
    ]


def test_decorar_relatorio(products_list):
    GREEN = "\033[32m"
    BLUE = "\033[36m"
    RED = "\033[31m"
    RESET = "\033[0m"

    expected = (
        f"{GREEN}Data de fabricação mais antiga:{RESET} "
        f"{BLUE}2020-12-06{RESET}\n"
        f"{GREEN}Data de validade mais próxima:{RESET} "
        f"{BLUE}2023-09-17{RESET}\n"
        f"{GREEN}Empresa com mais produtos:{RESET} "
        f"{RED}Target Corporation{RESET}"
    )

    colored_report = ColoredReport(SimpleReport).generate(products_list)

    assert colored_report == expected
