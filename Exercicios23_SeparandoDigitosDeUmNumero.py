nome = input('Digite seu nome completo: ').strip()
print(f'Seu nome em maiúsculo é :{nome.upper()}')
print(f'Seu nome em minusculo é :{nome.lower()}')
print(f"Seu nome em minusculo é :{len(nome)-nome.count(' ')}")
separa = nome.split()
print(f'Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras.')
print(f'Seu primeiro nome é {separa[1]} e ele tem {len(separa[1])} letras.')
