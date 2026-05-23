class Aluguel:

    def __init__(self, aluguel_id, bicicleta, cliente, email, devolucao):
        self.id = aluguel_id
        self.bicicleta = bicicleta
        self.cliente = cliente
        self.email = email
        self.devolucao = devolucao
        self.devolvido = False