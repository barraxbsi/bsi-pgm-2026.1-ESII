from services.servico_emprestimo import ServicoEmprestimo
from services.notificador_email import NotificadorEmail
from repositories.repositorio_emprestimo import RepositorioEmprestimo

class SistemaDeEmprestimos:
    def __init__(self):
        self._repositorio = RepositorioEmprestimo()
        self._servico = ServicoEmprestimo(self._repositorio)

        self._servico.registrar_observer(NotificadorEmail())