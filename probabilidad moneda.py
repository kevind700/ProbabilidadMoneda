import random
import matplotlib.pyplot as plt
import numpy as np
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

probSello = (float(cSello) / i) * 100
probCara = (float(cCara) / i) * 100

resultado = "probabilidad de Sello: " + str(probSello) + "\nProbabilidad de Cara: " + str(probCara)
resultado2 = "Veces que cayo Sello: " + str(cSello) + "\nVeces que cayo Cara: " + str(cCara)

print(resultado)
print(resultado2)

titulo = ["% Sello", "% Cara"]
posicion_y = np.arange(len(titulo))
unidades = (probSello, probCara)
plt.barh(posicion_y, unidades, align = "center")
plt.yticks(posicion_y, titulo)
plt.xlabel('Valores')
plt.title("Grafica de Probabilidad al arrojar una moneda")
plt.show()

