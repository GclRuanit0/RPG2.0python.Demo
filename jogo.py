from personagens.jogador import Jogador
from combate.geradorinimigo import gerar_inimigo
from combate.combate import combate
import historia

def escolher_classe():
    print("Escolha sua classe:")
    print("1 - Mago     | Vida: 100 | Mana: 150")
    print("2 - Guerreiro| Vida: 150 | Mana: 70")
    print("3 - Arqueiro | Vida: 100 | Mana: 30")
    escolha = input("Insira o número da sua classe: ").strip()
    if escolha == "1":
        return "mago"
    elif escolha == "2":
        return "guerreiro"
    elif escolha == "3":
        return "arqueiro"
    else:
        print("Opção inválida, selecionando Guerreiro por padrão.")
        return "guerreiro"

def main():
    historia.introducao()
    nome = input("Antes de tudo, qual é o seu nome? ").strip() or "Herói"
    classe = escolher_classe()
    jogador = Jogador.criar_com_classe(nome, classe)

    print(f"\nPersonagem criado: {jogador.nome} | Classe: {jogador.classe} | Vida: {jogador.vida} | Mana: {jogador.mana}")
    jogador.mostrar_inventario()


    for i in range(5):
        inimigo = gerar_inimigo()
        combate(jogador, inimigo)
        if not jogador.esta_vivo():
            print("Você morreu. Fim de jogo.")
            return
    print("\nVocê sobreviveu... (fim da demo)")

if __name__ == "__main__":
    main()