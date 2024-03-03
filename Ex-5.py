p = float(input('Valor do produto: '))
d = float(input('Desconto em porcentagem: '))
vd = p  - (p * (1 - d / 100))

print(f'O valor do desconto foi R${vd: .2f}')
print(f'Preço a pagar: R${p - vd: .2f}')