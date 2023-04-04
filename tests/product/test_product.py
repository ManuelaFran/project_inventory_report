from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        2,
        "fentanyl citrate",
        "Target Corporation",
        "2020-12-06",
        "2023-12-25",
        "FR29 5951 7573 74OY XKGX 6CSG D20",
        "instrucao 2",
    )
    assert product.id == 2
    assert product.nome_do_produto == "fentanyl citrate"
    assert product.nome_da_empresa == "Target Corporation"
    assert product.data_de_fabricacao == "2020-12-06"
    assert product.data_de_validade == "2023-12-25"
    assert product.numero_de_serie == "FR29 5951 7573 74OY XKGX 6CSG D20"
    assert product.instrucoes_de_armazenamento == "instrucao 2"
