class Equipamento:
    def __init__(self, nome, tipo, disponivel=True):
        self.nome = nome
        self.tipo = tipo
        self.disponivel = disponivel

        from abc import ABC, abstractmethod
from datetime import date, timedelta

class Equipamento(ABC):
    """Classe abstrata base — não instanciável diretamente."""
    
    def __init__(self, nome: str, valor_diaria: float = 0.0):
        self.nome = nome
        self.valor_diaria = valor_diaria
        self.data_emprestimo: date | None = None
        self.data_devolucao: date | None = None
    
    @abstractmethod
    def calcular_multa(self, dias_atraso: int) -> float:
        """Método abstrato obrigatório para todas as subclasses [web:1][web:10]."""
        pass

class Livro(Equipamento):
    """Multa: R$ 2,00 × dias_atraso"""
    def calcular_multa(self, dias_atraso: int) -> float:
        return max(0.0, 2.0 * dias_atraso)

class EquipamentoEletronico(Equipamento):
    """Multa: R$ 10,00 × dias_atraso"""
    def calcular_multa(self, dias_atraso: int) -> float:
        return max(0.0, 10.0 * dias_atraso)

class MaterialEsportivo(Equipamento):
    """Multa: R$ 5,00 × dias_atraso"""
    def calcular_multa(self, dias_atraso: int) -> float:
        return max(0.0, 5.0 * dias_atraso)