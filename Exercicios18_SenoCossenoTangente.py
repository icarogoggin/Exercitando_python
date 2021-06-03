import math
angulo = float(input('Digite o Angulo: '))
se = math.sin(math.radians(angulo))
print (f' O ângulo de {angulo}° tem o seno de {se:.2f}')
co = math.cos((math.radians(angulo)))
print (f' O ângulo de {angulo}° tem o cosseno de {co:.2f}')
tan = math.tan((math.radians(angulo)))
print (f' O ângulo de {angulo}° tem a tangente de {tan:.2f}')

