chars = []
vogal = []
consoante = []
count = 0
while count < 10:
    x = input('Digite uma letra do alfabeto:\n').lower()
    chars.append(x)
    if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
        vogal.append(x)
    else:
        consoante.append(x)
    count = count + 1
print(f'A sua lista de caracteres foi: {chars} e teve {len(vogal)} vogais e {len(consoante)} consoantes.')