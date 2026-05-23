
class NotificadorFalso:
    def __init__(self):
        self.chamadas = []

    def enviar_email(self, mensagem):
        self.chamadas.append(("enviar_email", mensagem))