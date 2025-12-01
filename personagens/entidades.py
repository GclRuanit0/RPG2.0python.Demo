from abc import ABC, abstractmethod

class Personagem(ABC):
    def __init__(self, nome: str, vida: int, ataque: int, defesa: int):

        self._nome = nome
        self._vida = max(0, int(vida))
        self._ataque = int(ataque)
        self._defesa = int(defesa)

    @property
    def nome(self):
        return self._nome

    @property
    def vida(self):
        return self._vida

    @property
    def ataque(self):
        return self._ataque

    @property
    def defesa(self):
        return self._defesa

    def esta_vivo(self) -> bool:
        return self._vida > 0

    def receber_dano(self, dano: int) -> int:
        """Aplica defesa e reduz vida. Retorna dano real aplicado."""
        dano_real = max(1, int(dano) - self._defesa)
        self._vida = max(0, self._vida - dano_real)
        print(f"{self._nome} recebeu {dano_real} de dano! Vida atual: {self._vida}")
        return dano_real

    @abstractmethod
    def atacar(self):
        """Deve retornar um inteiro representando o dano do ataque."""
        pass