km = float(input('Km percorridos: '))
d = int(input('Dias alugados: '))
t = (60 * d) + (0.15 * km)

print(f'Preço a pagar: R${t: .2f}')
