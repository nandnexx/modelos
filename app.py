from modelos.restaurante import Restaurante
from modelos.cardapios.bebida import Bebida
from modelos.cardapios.prato import Prato

restaurante_praca = Restaurante("praça", "Gourmet")
bebida_suco = Bebida ("Suco de melencia" 5.0, "grande")
prato_paozinho = Prato ("Paozinho", 2,00, "O melhor pão da cidade")

def main():
    print(bebida_suco)
    print(prato_paozinho)

if __name__ == '__main__':
    main()
