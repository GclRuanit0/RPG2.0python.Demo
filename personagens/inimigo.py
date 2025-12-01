
import random
from personagens.entidades import Personagem

class Inimigo(Personagem):
    def __init__(self, nome: str, vida: int, dano_min: int, dano_max: int, xp_drop: int, item_drop: str):

        super().__init__(nome, vida, ataque=0, defesa=0)
        self._dano_min = int(dano_min)
        self._dano_max = int(dano_max)
        self.xp_drop = int(xp_drop)
        self.drop = item_drop

    def atacar(self) -> int:
        dano = random.randint(self._dano_min, self._dano_max)
        print(f"{self._nome} ataca e causa {dano} de dano.")
        return dano