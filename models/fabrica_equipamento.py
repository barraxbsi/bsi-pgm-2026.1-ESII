from models.equipamento import (
    Equipamento,
    Livro,
    EquipamentoEletronico,
    MaterialEsportivo,
)

class FabricaEquipamento:
    @staticmethod
    def criar(tipo: str, nome: str) -> Equipamento:
        if tipo == "livro":
            return Livro(nome)

        elif tipo == "eletronico":
            return EquipamentoEletronico(nome)

        elif tipo == "esportivo":
            return MaterialEsportivo(nome)

        raise ValueError(f"Tipo desconhecido: {tipo}")