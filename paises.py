listado = set()
continuar = 'S'

while continuar == 'S':
    pais = input('Dime un país: ').upper()
    listado.add(pais)
    continuar = input('Continuar? S/N: ').upper()
else:
    print(sorted(listado))
