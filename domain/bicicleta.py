class Bicicleta:

    def __init__(self, bike_id, modelo):
        self.id = bike_id
        self.modelo = modelo
        self.disponivel = True

    def calcular_multa(self, atraso_horas):
        raise NotImplementedError()


class BikeUrbana(Bicicleta):

    def calcular_multa(self, atraso_horas):
        return max(0, atraso_horas) * 5.0


class BikeMountain(Bicicleta):

    def calcular_multa(self, atraso_horas):
        return max(0, atraso_horas) * 8.0


class BikeEletrica(Bicicleta):

    def calcular_multa(self, atraso_horas):
        return max(0, atraso_horas) * 15.0