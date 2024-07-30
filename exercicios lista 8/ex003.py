chars = []
vogal = []
consoante = []
count = 0
while count < 10:
    x = input('Digite uma letra do alfabeto:\n').lower()
    chars.append(x)
    if x in ['a', 'e', 'i', 'o', 'u']:
        vogal.append(x)
    else:
        consoante.append(x)
    count = count + 1
print(f'A sua lista de caracteres foi: {chars} e teve {len(vogal)} vogais e {len(consoante)} consoantes.')