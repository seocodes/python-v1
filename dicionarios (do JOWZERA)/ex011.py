atletas = { "Cristiano Ronaldo" : "Futebol", "LeBron James" : "Basquete",
                    "Lionel Messi" : "Futebol", "Neymar" : "Futebol",
                    "Conor McGregor" : "MMA", "Roger Federer" : "Tênis",
                     "Rafael Nadal" : "Tênis",  "Stephen Curry" : "Basquete",
                     "Tiger Woods" : "Golfe",  "Kevin Durant" : "Basquete",
                      "Lewis Hamilton" : "Fórmula 1", "Sun Yang" : "Natação" }

name = input('name: ')
esporte = input('esporte: ')
atletas[name] = esporte
if "Roger Federer" in atletas:
    print(True)
else:
    print(False)

atletas.pop("Tiger Woods")
# Infelizmente o atleta "Tiger Woods" : "Golfe"  não faz mais parte da lista e deve ser removido.
