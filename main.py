
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
=======
from services.servico_emprestimo import ServicoEmprestimo
from repositories.repositorio_emprestimo import RepositorioEmprestimo
from notifications.notificador import Notificador

def menu():
    print("\n1 - Registrar empréstimo")
    print("2 - Devolver equipamento")
    print("3 - Listar atrasados")
    print("4 - Sair")

def main():
    repositorio = RepositorioEmprestimo()
    notificador = Notificador()
    servico = ServicoEmprestimo(repositorio, notificador)

    while True:
        menu()
        opcao = input("Escolha: ")

        if opcao == "1":
            equipamento = input("Equipamento: ")
            usuario = input("Usuário: ")
            servico.registrar_emprestimo(equipamento, usuario)

        elif opcao == "2":
            equipamento = input("Equipamento: ")
            dias = int(input("Dias de atraso: "))
            servico.devolver_equipamento(equipamento, dias)

        elif opcao == "3":
            atrasados = servico.listar_atrasados()
            if not atrasados:
                print("Nenhum empréstimo atrasado.")
            for emprestimo in atrasados:
                print(emprestimo["usuario"], "-", emprestimo["equipamento"]["nome"])

        elif opcao == "4":
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
