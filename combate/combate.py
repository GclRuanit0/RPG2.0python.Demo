import time


def combate(jogador, inimigo):
    print(f"\nUm {inimigo.nome} apareceu! Vida: {inimigo.vida}\n")

    while jogador.esta_vivo() and inimigo.esta_vivo():
        jogador.regenerar_mana()

        print(f"Seu turno | Vida: {jogador.vida} | Mana: {jogador.mana}")
        print(f"Inimigo: {inimigo.nome} | Vida: {inimigo.vida}\n")

        print("1 - Atacar")
        print("2 - Inventário")
        print("3 - Fugir")
        escolha = input("Escolha uma ação: ").strip()

        if escolha == "1":

            jogador.listar_ataques()
            try:
                idx = int(input("Escolha seu ataque (número): ")) - 1
            except ValueError:
                print("Entrada inválida. Voltando...")
                time.sleep(1)
                continue
            dano = jogador.atacar(idx)
            if dano > 0:
                inimigo.receber_dano(dano)
                if not inimigo.esta_vivo():
                    print(f"\n{inimigo.nome} foi derrotado!")

                    jogador.ganhar_xp(inimigo.xp_drop)
                    jogador.adicionar_item(inimigo.drop)
                    break

        elif escolha == "2":

            while True:
                print("\n1 - Ver inventário\n2 - Usar item\n3 - Voltar")
                op = input("→ ").strip()
                if op == "1":
                    jogador.mostrar_inventario()
                elif op == "2":
                    jogador.mostrar_inventario()
                    item = input("Digite o nome do item para usar: ").strip()
                    msg = jogador.usar_item(item)
                    print(msg)
                elif op == "3":

                    jogador.regenerar_mana()
                    break
                else:
                    print("Opção inválida.")

        elif escolha == "3":
            import random
            chance_fuga = random.randint(1, 100)
            if chance_fuga <= 40:
                print("Você fugiu com sucesso!")
                return
            else:
                print("O inimigo te impede de fugir!")
        else:
            print("Ação inválida. Tente novamente.")
            continue

        if inimigo.esta_vivo():
            dano_inimigo = inimigo.atacar()
            jogador.receber_dano(dano_inimigo)
            if not jogador.esta_vivo():
                print("\nVocê foi derrotado. Fim de jogo.")
                return
        time.sleep(1)