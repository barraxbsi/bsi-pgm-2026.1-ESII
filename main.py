from app.sistema import SistemaDeEmprestimos
from models.fabrica_equipamento import FabricaEquipamento

sistema = SistemaDeEmprestimos()

equipamento = FabricaEquipamento.criar("notebook", 1, "Dell")

print("Sistema iniciado com Strategy + Observer")