estados = {"Acre" : "Capital Rio Branco", "Alagoas" : "Capital Maceió",
                "Amazonas": "Capital Manaus", "Bahia" : "Capital Salvador",
                "Distrito Federal" : "Capital Brasília", "Santa Catarina" : "Capital Florianópolis",
                "Rio Grande do Sul" : "Capital Porto Alegre",
                "Paraná" : "Capital Curitiba", "São Paulo" : "Capital São Paulo",
                "Minas Gerais" : "Cuiabá", "Rio de Janeiro" : "Rio de Janeiro",
                "Tocantins": "Capital Palmas"}

novoestado = 'kjfdjdogffd'
novacapital = 'Capital gdijsn gjk ghfjskjffdljhfdghjgfhffhfhfhjgfjk'
estados.update({novoestado: novacapital})

if 'Distrito Federal' in estados:
    print('DF está!')
else:
    print('DF NÃO TÁ')
estados.update({'Minas Gerais': 'Belo Horizonte'})
print(estados)