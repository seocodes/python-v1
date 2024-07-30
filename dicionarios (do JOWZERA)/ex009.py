estados = {"Acre" : "Capital Rio Branco",  "Alagoas" :  "Capital Maceió", 
                    "Amazonas": "Capital Manaus",  "Bahia" : "Capital Salvador", 
                    "Distrito Federal" : "Capital Brasília",  "Santa Catarina" : "Capital Florianópolis", 
                    "Rio Grande do Sul" : "Capital Porto Alegre",
                    "Paraná" : "Capital Curitiba", "São Paulo" : "Capital São Paulo",
                    "Minas Gerais" : "Cuiabá", "Rio de Janeiro" : "Rio de Janeiro",
                    "Tocantins": "Capital Palmas"}

cidade = input('nova cidade: ')
capital = input('capital: ')
estados[cidade] = capital

if "Distrito Federal" in estados.keys():
    print("true")
else:
    print("false")

estados.update({"Minas Gerais": "Belo Horizonte"})

for i, o in estados.items():
    print(f'{i} = {o}')