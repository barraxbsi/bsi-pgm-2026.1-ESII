# main.py - Executar interface CLI do sistema
from datetime import date, timedelta
from repositories.repositorio_emprestimo import RepositorioEmprestimo
from services.servico_emprestimo import ServicoEmprestimo


def menu():
    print("\n=== Sistema de Empréstimo ===")
    print("1 - Registrar empréstimo")
    print("2 - Devolver equipamento")
    print("3 - Listar atrasados")
    print("4 - Sair")


def main():
    # Cria o repositório e o serviço dentro da função
    repositorio = RepositorioEmprestimo()
    servico = ServicoEmprestimo(repositorio)
    
    # Adiciona alguns equipamentos de exemplo
    repositorio.adicionar_equipamento("Livro de Python", "livro")
    repositorio.adicionar_equipamento("Tablet", "eletronico")
    repositorio.adicionar_equipamento("Bicicleta", "esportivo")
    
    while True:
        menu()
        opcao = input("Escolha: ")
        
        if opcao == "1":
            equipamento = input("Nome do equipamento: ")
            usuario = input("Usuário: ")
            dias_prazo = int(input("Prazo em dias (padrão 7): ") or "7")
            
            # Registrar empréstimo com data atual
            data_atual = date.today()
            servico.emprequisar(equipamento, data_atual, prazo_dias=dias_prazo)
            print(f"Empréstimo registrado de {equipamento} para {usuario}")
        
        elif opcao == "2":
            equipamento = input("Nome do equipamento: ")
            dias_atraso = int(input("Dias de atraso: ") or "0")
            
            multa = servico.devolver_equipamento(equipamento, date.today())
            if multa is not None:
                print(f"Devolução registrada. Multa: R$ {multa:.2f}")
            else:
                print("Equipamento não encontrado.")
        
        elif opcao == "3":
            data_atual = date.today()
            atrasados = servico.listar_atrasados(repositorio.listar_todos(), data_atual)
            
            if not atrasados:
                print("\nNenhum equipamento atrasado.")
            else:
                print("\n=== Equipamentos Atrasados ===")
                for nome, dias, multa in atrasados:
                    print(f"  {nome}: {dias} dias - Multa: R$ {multa:.2f}")
        
        elif opcao == "4":
            print("Saindo...")
            break
        
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()