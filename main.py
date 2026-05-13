# main: executar interface CLI do sistema.

from services.servico_emprestimo import ServicoEmprestimo


def menu():
    print("\n1 - Registrar empréstimo")
    print("2 - Devolver equipamento")
    print("3 - Listar atrasados")
    print("4 - Sair")


def main():
    servico = ServicoEmprestimo()

    while True:
        menu()

        opcao = input("Escolha: ")

        if opcao == "1":
            equipamento = input("Equipamento: ")
            usuario = input("Usuário: ")

            servico.registrar_emprestimo(
                equipamento,
                usuario
            )

        elif opcao == "2":
            equipamento = input("Equipamento: ")
            dias = int(input("Dias de atraso: "))

            servico.devolver_equipamento(
                equipamento,
                dias
            )

        elif opcao == "3":
            atrasados = servico.listar_atrasados()

            if not atrasados:
                print("Nenhum empréstimo atrasado.")

            for emprestimo in atrasados:
                print(
                    emprestimo["usuario"],
                    "-",
                    emprestimo["equipamento"]["nome"]
                )

        elif opcao == "4":
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()