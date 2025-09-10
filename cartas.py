class Carta:
    def __init__(self, nome, atributos):
        """
        Classe que representa uma carta do Super Trunfo.
        :param nome: str -> nome da carta
        :param atributos: dict -> atributos da carta (ex.: {"força": 80, "velocidade": 70})
        """
        self.nome = nome
        self.atributos = atributos

    def __str__(self):
        return f"{self.nome} - {self.atributos}"
