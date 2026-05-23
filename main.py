import datetime

from domain.bicicleta import BikeUrbana
from domain.aluguel import Aluguel

from repositories.repositorio_aluguel import RepositorioAluguel
from notifications.notificador_email import NotificadorEmail
from services.servico_aluguel import ServicoAluguel


bike = BikeUrbana(1, "Caloi Urbana")

aluguel = Aluguel(
    1,
    bike,
    "João",
    "joao@email.com",
    datetime.datetime.now() - datetime.timedelta(hours=2)
)

repo = RepositorioAluguel()
repo.adicionar(aluguel)

notificador = NotificadorEmail()

servico = ServicoAluguel(repo, notificador)

multa = servico.devolver(1)

print("Multa final:", multa)