from repositories.repositorio_emprestimo import RepositorioEmprestimo
from services.notificador import Notificador


class ServicoEmprestimo:
    def __init__(self):
        self.repositorio = RepositorioEmprestimo()
        self.notificador = Notificador()

    def registrar_emprestimo(self, nome_equipamento, usuario):
        equipamento = self.repositorio.buscar_equipamento(nome_equipamento)

        if equipamento is None:
            print("Equipamento não encontrado.")
            return

        if not equipamento["disponivel"]:
            print("Equipamento indisponível.")
            return

        emprestimo = {
            "usuario": usuario,
            "equipamento": equipamento,
            "dias_atraso": 0
        }

        self.repositorio.adicionar_emprestimo(emprestimo)
        self.repositorio.marcar_indisponivel(equipamento)

        self.notificador.enviar_email(
            f"Empréstimo registrado para {usuario}"
        )

        print("Empréstimo registrado com sucesso.")

    def devolver_equipamento(self, nome_equipamento, dias_atraso):
        for emprestimo in self.repositorio.listar_emprestimos():
            equipamento = emprestimo["equipamento"]

            if equipamento["nome"].lower() == nome_equipamento.lower():

                multa = 0

                # Mantido propositalmente (problema de OCP)
                if equipamento["tipo"] == "notebook":
                    multa = dias_atraso * 10

                elif equipamento["tipo"] == "camera":
                    multa = dias_atraso * 5

                self.repositorio.marcar_disponivel(equipamento)

                self.notificador.enviar_email(
                    f"Equipamento devolvido. Multa: R${multa}"
                )

                print("Devolução realizada.")
                return

        print("Empréstimo não encontrado.")

    def listar_atrasados(self):
        atrasados = []

        for emprestimo in self.repositorio.listar_emprestimos():
            if emprestimo["dias_atraso"] > 0:
                atrasados.append(emprestimo)

        return atrasados