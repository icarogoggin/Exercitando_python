print('Escolha uma temperatura para converter!')
print('[1] °C para °F')
print('[2] °F para °C')
op = input('Digite apenas o numero: ')
if op == '1':
    c = float(input('Digite aqui a temperatura em °C : '))
    f = (c*9/5)+32
    print(f'{c}°C = {f:.2f}°F')
elif op == '2':
    f = float(input('Digite aqui a temperatura em °F : '))
    c = (f-32)*5/9
    print(f'{f}°F = {c:.2f}°C')
else:
    print('Escolha uma opção válida!')