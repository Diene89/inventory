from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        "9",
        "eucalyptus globulus",
        "Target Corporation",
        "2020-09-06",
        "2024-05-21",
        "GT74 LHWJ FCXL JNQT ZCXM 4761 GWSP",
        "ao abrigo da luz",
    )
    assert (
        str(product) == "O produto eucalyptus globulus fabricado em 2020-09-06"
        " por Target Corporation com validade até 2024-05-21"
        " precisa ser armazenado ao abrigo da luz."
    )
