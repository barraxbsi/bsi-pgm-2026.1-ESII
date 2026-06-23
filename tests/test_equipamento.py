from models.fabrica_equipamento import FabricaEquipamento

def test_calcular_multa_notebook():
    equipamento = FabricaEquipamento.criar("notebook", 1, "Dell")
    assert equipamento.calcular_multa(2) == 20.0