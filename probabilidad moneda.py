import random
i = 10000
opciones =  [0, 1]
contador = 0
cSello = 0
cCara = 0
while i != contador:
	aleatorio = random.choice(opciones)
	contador = contador + 1
	if (aleatorio == 0):
		cSello += 1
	else:
		cCara += 1

probSello = cSello / i
probCara = cCara / i

resultado = "probabilidad de Sello: " + str(probSello) + "\nProbabilidad de Cara: " + str(probCara)
resultado2 = "Veces que cayo Sello: " + str(cSello) + "\nVeces que cayo Cara: " + str(cCara)

print(resultado)
print(resultado2)
