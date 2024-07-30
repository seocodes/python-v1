times = {1: "Criciuma", 2: "Avai", 3: "Marcilio Dias", 4: "Joinville", 5: "Figueirense",
6: "Chapecoense", 7: "Brusque", 8: "Metropolitano",
9: "Hercílio Luz", 10: "Inter de Lages"}

times.update({11: 'THE SIGMAS'})
if 'Joinville' in times.values():
    print('ESTÁ')
else:
    print('NÃO TÁ')
del times[2]
print(times)

