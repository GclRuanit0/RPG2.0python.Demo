from personagens.entidades import Personagem
from ataques import ATAQUES_POR_CLASSE
from itens import ITENS_INICIAIS
from typing import List, Dict

class Jogador(Personagem):
    def __init__(self, nome: str, classe_nome: str, vida: int, mana: int, ataque_base: int = 0, defesa: int = 0):
        super().__init__(nome, vida, ataque=ataque_base, defesa=defesa)

        self.classe = classe_nome
        self._mana = int(mana)
        self._mana_max = int(mana)
        self.inventario: List[str] = list(ITENS_INICIAIS.get(classe_nome, []))
        self.capacidade_inventario: int = 10
        self.ataques: List[Dict] = [dict(a) for a in ATAQUES_POR_CLASSE.get(classe_nome, [])]
        self.xp = 0
        self.nivel = 1
        self.xp_req = 100
        self.mana_regen_por_turno = 25 

    @property
    def mana(self):
        return self._mana

    def regenerar_mana(self):
        self._mana = min(self._mana_max, self._mana + self.mana_regen_por_turno)

        print(f"{self._nome} recuperou {self.mana_regen_por_turno} de mana. Mana atual: {self._mana}/{self._mana_max}")


    def mostrar_inventario(self):
        print("\n--- Inventário ---")
        if not self.inventario:
            print("Seu inventário está vazio.")
            return
        contagem = {}
        for item in self.inventario:
            contagem[item] = contagem.get(item, 0) + 1
        for nome, qtd in contagem.items():
            print(f"- {nome} x{qtd}")
        print(f"Total: {len(self.inventario)}/{self.capacidade_inventario}")

    def adicionar_item(self, item_nome: str) -> bool:
        if len(self.inventario) < self.capacidade_inventario:
            self.inventario.append(item_nome)
            print(f"{item_nome} adicionado ao inventário.")
            return True
        print("Inventário cheio!!! Não foi possível adicionar o item.")
        return False

    def usar_item(self, nome_item: str) -> str:
        nome_item = nome_item.strip().lower()
        for i, item in enumerate(self.inventario):
            if item.lower() == nome_item:

                if item.lower() == "poção de vida":
                    self._vida += 30
                    self.inventario.pop(i)
                    return "Você usou Poção de Vida e recuperou 30 de vida."
                elif item.lower() == "poção de mana":
                    self._mana = min(self._mana_max, self._mana + 30)
                    self.inventario.pop(i)
                    return "Você usou Poção de Mana e recuperou 30 de mana."
                else:

                    return f"Item {item} não pode ser usado (implementação básica)."
        return "Item não encontrado."


    def listar_ataques(self):
        for i, atk in enumerate(self.ataques):
            print(f"{i+1} - {atk['nome']} (Dano: {atk['dano']} | Mana: {atk['mana']})")

    def atacar(self, indice: int = 0) -> int:
        """Aplica o ataque selecionado (indice). Retorna dano ou -1 se falha (mana insuf)."""
        if indice < 0 or indice >= len(self.ataques):
            print("Ataque inválido.")
            return 0
        atk = self.ataques[indice]
        if self._mana < atk["mana"]:
            print("Mana insuficiente para este ataque.")
            return 0
        self._mana -= atk["mana"]
        dano = atk["dano"]
        print(f"{self._nome} usou {atk['nome']} e causou {dano} de dano! Mana restante: {self._mana}/{self._mana_max}")
        return dano


    def ganhar_xp(self, quantidade: int):
        self.xp += int(quantidade)
        print(f"XP ganho: {quantidade} | Total: {self.xp}/{self.xp_req}")
        while self.xp >= self.xp_req:
            self.subir_nivel()

    def subir_nivel(self):
        self.nivel += 1
        self.xp -= self.xp_req
        self.xp_req += 100

        self._vida += 15
        self._mana_max += 25
        self._mana = min(self._mana, self._mana_max)
        print(f"\nVocê subiu para o nível {self.nivel}! Vida e mana aumentaram.")
        print(f"Vida atual: {self._vida} | Mana máxima: {self._mana_max}")


    @classmethod
    def criar_com_classe(cls, nome: str, classe_escolhida: str):
        classe_escolhida = classe_escolhida.lower()
        if classe_escolhida == "mago":
            return cls(nome, "mago", vida=100, mana=150, ataque_base=10, defesa=2)
        elif classe_escolhida == "guerreiro":
            return cls(nome, "guerreiro", vida=150, mana=70, ataque_base=12, defesa=5)
        elif classe_escolhida == "arqueiro":
            return cls(nome, "arqueiro", vida=100, mana=30, ataque_base=11, defesa=3)
        else:
            # padrão
            return cls(nome, "guerreiro", vida=120, mana=50, ataque_base=10, defesa=3)