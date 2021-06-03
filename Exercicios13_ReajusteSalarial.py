salario1 = float(input('Digite o salario inicial do funcionário: '))
aumento = float(input('Digite o aumento de salario que você ira aplicar em % :').replace('%','').replace(',','.'))/100
salarioFinal = salario1 + (salario1*aumento)
print (f'O salário inicial do funcionário era R${salario1} e sofreu eum reajuste de {aumento*100}%, o salário reajustado ficou R${salarioFinal}.')