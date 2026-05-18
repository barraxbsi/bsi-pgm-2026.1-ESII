from datetime import date
from models.equipamento import Equipamento


class ServicoEmprestimo:
    """
    Serviço para gerenciar operações de empréstimo.
    
    OCP: Eliminação de if/elif - cada equipamento calcula sua própria multa
    através do método polimórfico calcular_multa().
    """
    
    def __init__(self, repositorio):
        self.repositorio = repositorio
    
    def calcular_multa_equipamento(self, equipamento: Equipamento, dias_atraso: int) -> float:
        """
        Calcula a multa para um equipamento específico.
        
        OCP aplicado: SEMPRE mais if/elif!
        Chamada polimórfica - cada subclasse implementa sua própria fórmula.
        """
        # Chamada polimórfica - cada subclasse define sua própria fórmula
        return equipamento.calcular_multa(dias_atraso)
    
    def listar_atrasados(self, equipamentos: list[Equipamento], data_atual: date) -> list[tuple]:
        """
        Retorna lista de equipamentos atrasados com suas multas.
        
        OCP aplicado: não há duplicação de lógica de cálculo de multa
        - cada equipamento sabe calcular sua própria multa.
        """
        atrasados = []
        
        for eq in equipamentos:
            dias_atraso = eq.get_dias_atraso(data_atual)
            if dias_atraso > 0:
                # Chamada polimórfica - sem duplicação!
                multa = eq.calcular_multa(dias_atraso)
                atrasados.append((eq.nome, dias_atraso, multa))
        
        return atrasados
    
    def emprequisar(self, nome_equipamento: str, data_emprestimo: date, prazo_dias: int = 7) -> bool:
        """Registra empréstimo de um equipamento."""
        eq = self.repositorio.buscar_por_nome(nome_equipamento)
        if eq is None:
            return False
        
        eq.registrar_emprestimo(data_emprestimo)
        return True
    
    def devolver_equipamento(self, nome_equipamento: str, data_devolucao: date) -> float | None:
        """Registra devolução e retorna a multa (se houver atraso)."""
        eq = self.repositorio.buscar_por_nome(nome_equipamento)
        if eq is None:
            return None
        
        eq.registrar_devolucao(data_devolucao)
        dias_atraso = eq.get_dias_atraso(data_devolucao)
        
        if dias_atraso > 0:
            return eq.calcular_multa(dias_atraso)
        
        return 0.0