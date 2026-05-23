import datetime


class ServicoAluguel:

    def __init__(self, repositorio, notificador):
        self.repositorio = repositorio
        self.notificador = notificador

    def devolver(self, aluguel_id):

        aluguel = self.repositorio.buscar_por_id(aluguel_id)

        if aluguel is None:
            return None

        if aluguel.devolvido:
            return None

        atraso_horas = (
            datetime.datetime.now() - aluguel.devolucao
        ).total_seconds() / 3600

        multa = aluguel.bicicleta.calcular_multa(atraso_horas)

        aluguel.devolvido = True
        aluguel.bicicleta.disponivel = True

        self.repositorio.salvar(aluguel)

        self.notificador.enviar(
            aluguel.email,
            f"Devolução registrada. Multa: R${multa:.2f}"
        )

        return round(multa, 2)