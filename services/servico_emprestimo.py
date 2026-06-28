from services.observer import Subject

class ServicoEmprestimo(Subject):

    def __init__(self, repositorio):
        super().__init__()
        self.repositorio = repositorio