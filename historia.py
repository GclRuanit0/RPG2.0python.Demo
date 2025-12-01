import time
import sys

def print_lento(texto: str, velocidade: float = 0.03):
    for c in texto:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(velocidade)
    print()

def introducao():
    print_lento("\nZumbido... escuridão.")
    print_lento("\nSua cabeça explode de dor. Mil martelos batem dentro de você.")
    print_lento("\nVocê acorda em uma cela fria e úmida, preso por correntes de gelo.")
    print_lento("\nLuz fraca entra pelas frestas de uma porta enferrujada.")
    print_lento("\nCom esforço, você quebra as correntes e rasteja até a porta.")
    print_lento("\nAo empurrá-la, um rangido ecoa pelo corredor vazio...")
    print_lento("\nVocê não está sozinho.")
    print_lento("\nÀ frente, um som estranho rompe o silêncio.")
    print_lento("....")