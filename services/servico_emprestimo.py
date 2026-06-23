from repositories.repositorio_emprestimo import RepositorioEmprestimo
from services.notificador import Notificador

from services.observer import Subject

class ServicoEmprestimo(Subject):
    def __init__(self, repositorio):
        super().__init__()
        self.repositorio = repositorio

    def registrar(self, equipamento_id, usuario_nome, usuario_email, dias):
        # sua regra antiga continua aqui
        self.notificar({
            "tipo": "emprestimo",
            "email": usuario_email,
            "data": data_devolucao
        })
        return True

    def devolver(self, emprestimo_id):
        # sua regra antiga continua aqui
        self.notificar({
            "tipo": "devolucao",
            "email": emprestimo.usuario_email,
            "multa": multa
        })

    def listar_atrasados(self):
        # sua regra antiga continua aqui
        self.notificar({
            "tipo": "atraso",
            "email": emprestimo.usuario_email
        })


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