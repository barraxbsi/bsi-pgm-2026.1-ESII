class RepositorioAluguel:

    def __init__(self):
        self.alugueis = []

    def adicionar(self, aluguel):
        self.alugueis.append(aluguel)

    def buscar_por_id(self, aluguel_id):

        for aluguel in self.alugueis:
            if aluguel.id == aluguel_id:
                return aluguel

        return None

    def salvar(self, aluguel):
        pass