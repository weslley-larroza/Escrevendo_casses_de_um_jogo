class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        if self.tipo == "mago":
            ataque = "usou magia"
        elif self.tipo == "guerreiro":
            ataque = "usou espada"
        elif self.tipo == "monge":
            ataque = "usou artes marciais"
        elif self.tipo == "ninja":
            ataque = "usou shuriken"
        else:
            ataque = "usou um ataque desconhecido"

        print(f"O {self.tipo} atacou usando {ataque}")


# Função para solicitar ao usuário que escolha o tipo de herói
def escolher_tipo():
    print("Escolha o tipo de herói:")
    print("1 - Guerreiro")
    print("2 - Monge")
    opcao = input("Digite o número correspondente ao tipo desejado: ")
    if opcao == "1":
        return "guerreiro"
    elif opcao == "2":
        return "monge"
    else:
        print("Opção inválida. Escolha novamente.")
        return escolher_tipo()


# Exemplo de uso
nome = input("Digite o nome do herói: ")
idade = int(input("Digite a idade do herói: "))
tipo = escolher_tipo()

heroi = Heroi(nome, idade, tipo)
heroi.atacar()
