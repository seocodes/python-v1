times = {1: "Criciuma",  2: "Avai",  3: "Marcilio Dias", 4: "Joinville", 
                5: "Figueirense",  6: "Chapecoense",  7: "Brusque", 8: "Metropolitano",
                9: "Hercílio Luz", 10: "Inter de Lages" }


timenovo = input('nome ')
times[len(times.keys() )+ 1] = timenovo


if "Joinville" in times.keys():
    print(True)
else:
    print(False)

times.pop(2)

for i, o in times.items():
    print(f'{i} - {o}')
