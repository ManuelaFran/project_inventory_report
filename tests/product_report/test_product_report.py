from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        2,
        "fentanyl citrate",
        "Target Corporation",
        "2020-12-06",
        "2023-12-25",
        "FR29 5951 7573 74OY XKGX 6CSG D20",
        "instrucao 2",
    )

    assert str(product.__repr__()) == (
        "O produto fentanyl citrate"
        " fabricado em 2020-12-06"
        " por Target Corporation com validade"
        " até 2023-12-25"
        " precisa ser armazenado instrucao 2."
    )
