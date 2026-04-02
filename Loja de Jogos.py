
class Jogos:

    def __init__(self, nome, preco):

        self.nome = nome
        self.preco = preco

    def get_info(self):

        if not self.nome:
            raise ValueError("O nome do jogo não pode ser vazio.")

        if self.preco < 0:
            raise ValueError("O preço do jogo não pode ser negativo.")

    def __str__(self):
        return f"{self.nome} - R${self.preco:.2f}"

jogo1 = Jogos("Cyberpunk 2077", 199.99)
jogo2 = Jogos("The Witcher 3", 99.99)

print(jogo1)
print(jogo2)
