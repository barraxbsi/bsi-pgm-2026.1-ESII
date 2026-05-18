class RepositorioEmprestimo:
    def __init__(self):
        self.equipamentos = [
            {"nome": "Notebook", "tipo": "notebook", "disponivel": True},
            {"nome": "Camera", "tipo": "camera", "disponivel": True},
        ]

        self.emprestimos = []

    def listar_equipamentos(self):
        return self.equipamentos

    def buscar_equipamento(self, nome):
        for equipamento in self.equipamentos:
            if equipamento["nome"].lower() == nome.lower():
                return equipamento
        return None

    def marcar_indisponivel(self, equipamento):
        equipamento["disponivel"] = False

    def marcar_disponivel(self, equipamento):
        equipamento["disponivel"] = True

    def adicionar_emprestimo(self, emprestimo):
        self.emprestimos.append(emprestimo)

    def listar_emprestimos(self):
        return self.emprestimos

        def adicionar_equipamento(self, nome: str, tipo: str) -> Equipamento:
    if tipo == "livro":
        eq = Livro(nome)
    elif tipo == "eletronico":
        eq = EquipamentoEletronico(nome)
    elif tipo == "esportivo":
        eq = MaterialEsportivo(nome)
    else:
        eq = Livro(nome)
    
    self.equipamentos.append(eq)
    return eq