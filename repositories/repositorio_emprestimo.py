from models.equipamento import Equipamento, Livro, EquipamentoEletronico, MaterialEsportivo


class RepositorioEmprestimo:
    """
    Repositório para gerenciar empréstimos de equipamentos.
    """
    
    def __init__(self):
        self.equipamentos: list[Equipamento] = []
    
    def adicionar_equipamento(self, nome: str, tipo: str) -> Equipamento:
        """
        Cria e adiciona um equipamento do tipo especificado.
        
        OCP: Agora cada tipo é instanciado pela sua própria classe,
        não pela classe genérica.
        """
        if tipo == "livro":
            eq = Livro(nome)
        elif tipo == "eletronico":
            eq = EquipamentoEletronico(nome)
        elif tipo == "esportivo":
            eq = MaterialEsportivo(nome)
        else:
            # Padrão: Livro
            eq = Livro(nome)
        
        self.equipamentos.append(eq)
        return eq
    
    def listar_todos(self) -> list[Equipamento]:
        return self.equipamentos.copy()
    
    def buscar_por_nome(self, nome: str) -> Equipamento | None:
        for eq in self.equipamentos:
            if eq.nome.lower() == nome.lower():
                return eq
        return None