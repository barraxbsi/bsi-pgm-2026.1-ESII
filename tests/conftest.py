import pytest
from services.observer import Observer
from services.servico_emprestimo import ServicoEmprestimo
from models.fabrica_equipamento import FabricaEquipamento

class NotificadorSpy(Observer):
    def __init__(self):
        self.eventos = []

    def update(self, evento):
        self.eventos.append(evento)

@pytest.fixture
def repositorio_fake():
    # mantenha sua implementação, mas crie equipamentos via fábrica
    pass

@pytest.fixture
def notificador_spy():
    return NotificadorSpy()

@pytest.fixture
def servico(repositorio_fake, notificador_spy):
    s = ServicoEmprestimo(repositorio_fake)
    s.registrar_observer(notificador_spy)
    return s