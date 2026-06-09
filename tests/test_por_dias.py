from multa import calcular_multa_com_carencia


def test_cobra_apenas_dias_excedentes_da_carencia():
    assert calcular_multa_com_carencia(
        dias_atraso=5,
        dias_carencia=2,
        valor_por_dia=10.0
    ) == 30.0