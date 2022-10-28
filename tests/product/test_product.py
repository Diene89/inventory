from inventory_report.inventory.product import Product


def test_cria_produto():
    new_product = Product(
        9,
        "eucalyptus globulus",
        "Target Corporation",
        "2020-09-06",
        "2024-05-21",
        "GT74 LHWJ FCXL JNQT ZCXM 4761 GWSP",
        "instrucao 9"
    )

    assert new_product.id == 9
    assert new_product.nome_do_produto == "eucalyptus globulus"
    assert new_product.nome_da_empresa == "Target Corporation"
    assert new_product.data_de_fabricacao == "2020-09-06"
    assert new_product.data_de_validade == "2024-05-21"
    assert new_product.numero_de_serie == "GT74 LHWJ FCXL JNQT ZCXM 4761 GWSP"
    assert new_product.instrucoes_de_armazenamento == "instrucao 9"
