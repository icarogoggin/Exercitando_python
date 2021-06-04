nome = input('Digite seu nome completo: ').strip().lower()
print(f'A letra a aparece {nome.count("a")} vezes')
print(f'A primeira letra A apareceu na posição {nome.find("a")+1}')
print(f'A primeira letra A apareceu na posição {nome.rfind("a")+1}')