import random
from personagens.inimigo import Inimigo

def gerar_inimigo():
    inimigos = [
        Inimigo("Goblin", 40, 5, 12, 30, "poção de vida"),
        Inimigo("Esqueleto", 60, 8, 15, 25, "pilha de ossos"),
        Inimigo("Orc", 120, 10, 18, 60, "banha de orc"),
        Inimigo("Beholder", 150, 15, 20, 120, "olho do beholder"),
    ]
    return random.choice(inimigos)