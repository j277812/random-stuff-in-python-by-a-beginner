'''
Esse programa simula uma batalha Pokemon:
1. O usuário escolhe o nome, a saúde e a velocidade de ataque de dois Pokemons.
2. Os Pokemons se 'cumprimentam' e um evento aleatório acontece.
3. A equipe Rocket tem uma chance de 2% de aparecer e roubar os Pokemons.
4. Os Pokemons se atacam até que um deles fique com a saúde menor ou igual a zero.
5. O programa informa o vencedor e a saúde final dos Pokemons.
6. O usuário pode escolher se deseja jogar novamente.
7. O usuário joga repetidamente até morrer de inanição.
'''

from random import randint,random

def listadepokemons():
    pokemons = ["Pikachu", "Charmander", "Bulbasaur", "Squirtle", "Jigglypuff", "Meowth",
                 "Psyduck", "Machop", "Geodude", "Gastly", "Onix", 
                 "Krabby", "Voltorb", "Cubone", "Hitmonlee", "Hitmonchan", 
                 "Lickitung", "Koffing", "Rhyhorn", "Chansey", "Tangela", "Kangaskhan", 
                 "Horsea", "Goldeen", "Staryu", "Mr. Mime", "Scyther", "Jynx", "Electabuzz", 
                 "Magmar", "Pinsir", "Tauros", "Magikarp", "Lapras", "Ditto", "Eevee", "Porygon", 
                 "Omanyte", "Kabuto", "Aerodactyl", "Snorlax", "Articuno", "Zapdos", "Moltres", 
                 "Dratini", "Dragonair", "Dragonite", "Mewtwo", "Mew"]
    return pokemons
def listadeacontecimentos(nome1,nome2):
    listadeacontecimentos = ["{1} olha para {0} com um olhar desafiador.\n".format(nome1, nome2), 
                             "{0} olha para {1} com um olhar amigável.\n".format(nome1, nome2), 
                             "{1} olha para {0} com um olhar de desdém.\n".format(nome1, nome2), 
                             "{0} acaba de mandar um beijinho para {1}.\n".format(nome1, nome2), 
                             "{0} acaba de xingar a mãe de {1}.\n".format(nome1, nome2), 
                             "{1} olha para {0} com um olhar de indiferença.\n".format(nome1, nome2),
                             "{1} acaba de morder a patinha de {0}!\n".format(nome1, nome2),]
    return listadeacontecimentos

def listadeacontecimentosdurantepartida(nome1,nome2):
    listadeacontecimentos = ["{0} está aflito com a situação.".format(nome1),
                             "{0} ainda está confiante.".format(nome2),
                             "{0} está com medo de algo dar errado.".format(nome1),
                             "{0} ainda não perdeu a confiança.".format(nome2),
                             "{0} ainda se sente confiante".format(nome1),
                             "{0} está zonzo do ataque.".format(nome2),
                             "{0} se machucou por conta do ataque, mas não tem problema.".format(nome1),""]
    print(listadeacontecimentos[randint(0,6)],end="\n\n")

def interrogatorio_pokemon():
    nome = input("Nome do Pokemon: ")
    if nome == "":
        nome = listadepokemons()[randint(0,48)]
    saude = input("Número de saúde de {}: ".format(nome))
    if nome == "Magikarp":
        saude = 1
    if nome == "Mewtwo":
        saude = 2000
    if saude == "":
        saude = randint(50,2000)
        print("A saúde de {} é {}.".format(nome, saude))
    velocidade = input("Velocidade de ataque de {}: ".format(nome))
    if velocidade == "":
        velocidade = randint(1,4)
        print("A velocidade de ataque de {} é {}.".format(nome, velocidade))
    print()
    return nome, int(saude), int(velocidade)

def saudacao(nome1, nome2):
    print("{0} e {1} acabam de se cumprimentar.".format(nome1, nome2))
    print(listadeacontecimentos(nome1, nome2)[randint(0,6)])

def contagemdeturnos(turno):
    turno += 1
    print("[Turno {}]".format(int(turno)))
    return turno

def equiperocket():
    probabilidade_equiperocket = 0.02
    if random() < probabilidade_equiperocket:
        print("A equipe Rocket apareceu e roubou os dois Pokemons!")
        return True

def ataque():
    forca = [10, 30, 50, 100]
    efetividade = [0, 0.5, 1, 2]
    return forca[randint(0,3)] * efetividade[randint(0,3)]

def ataquedesfeito(nome):
    if randint(1,8) == 1:
        print("{0} ficou zonzo com o ataque sofrido!".format(nome))
        return False
    else:
        return True

def combate(nome1, nome2, saude1, saude2, velocidade1, velocidade2):
    estatistica1 = saude1
    estatistica2 = saude2
    if velocidade1 > velocidade2:
        saude2 -= ataque()
        if ataquedesfeito(nome2):
            saude1 -= ataque()
    elif velocidade1 < velocidade2:
        saude1 -= ataque()
        if ataquedesfeito(nome1):
            saude2 -= ataque()
    else:
        if randint(1,2) == 1:
            saude1 -= ataque()
            if ataquedesfeito(nome1):
                saude2 -= ataque()
        elif randint(1,2) == 2:
            saude2 -= ataque()
            if ataquedesfeito(nome2):
                saude1 -= ataque()

    if saude1 <= 0 and saude2 <= 0:
        print("Os dois Pokemons desmaiaram!")
        return saude1, saude2, estatistica1, estatistica2

    elif saude1 <= 0 or saude2 <= 0:
        if estatistica1 == saude1:
            print("{0} bloqueou o ataque!".format(nome1, saude1))
        if estatistica2 == saude2:
            print("{0} bloqueou o ataque!".format(nome2, saude2))
        return saude1, saude2, estatistica1, estatistica2
    
    if estatistica1 == saude1:
        print("{0} bloqueou o ataque!".format(nome1, saude1))
    if estatistica2 == saude2:
        print("{0} bloqueou o ataque!".format(nome2, saude2))

    return saude1, saude2, estatistica1, estatistica2

def resultado(nome, nome2, saude, saude2, estatistica1, estatistica2):
    if saude <= 0 and saude2 <= 0:
        saude = 0
        saude2 = 0
        print("EMPATE!") 
    else:   
        if saude <= 0:
            print("O vencedor foi {}\n".format(nome2))
            saude = 0
        if saude2 <= 0:
            print("O vencedor foi {}\n".format(nome))
            saude2 = 0
    print(f"HP final de {nome} foi {saude} ({saude - estatistica1}),\nHP final de {nome2} foi {saude2} ({saude2 - estatistica2}).\n")


def partida():
    turno = 0
    nome, saude, velocidade = interrogatorio_pokemon()
    nome2, saude2, velocidade2 = interrogatorio_pokemon()
    saudacao(nome, nome2)
    resposta = input("Iniciar a partida [Enter]? ")
    while saude > 0 and saude2 > 0:
        if equiperocket():
            break
        turno = contagemdeturnos(turno)
        saude, saude2, estatistica1, estatistica2 = combate(nome, nome2, saude, saude2, velocidade, velocidade2)
        if saude > 0 and saude2 > 0:
            listadeacontecimentosdurantepartida(nome, nome2)
            print()
        resultado(nome, nome2, saude, saude2, estatistica1, estatistica2)
        input("Próximo turno [Enter]\n")
    print("Fim da partida!\n")

def main():
    try:
        partida()
        resposta = input("Outra partida [Enter]? (Caso a resposta seja não, qualquer tecla menos [Enter]) ")
        if resposta == "":
            main()
    except ValueError:
        print("Mais cuidado com os valores inseridos!\n")
        main()
main()