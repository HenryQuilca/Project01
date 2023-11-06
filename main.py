# Vamos a traer la función "suma", de la siguiente manera:
# A esto se le llama "Módulos".
from mi_primer_paquete.calculadora import suma
print(suma(2, 4, 6))

print("----------------")

# Importamos desde otra carpeta, en este caso: 1er_paquete
from mi_primer_paquete.calculadora_cientifica import tangente
print(tangente("Esta es mi tangente."))

print("-------------------------------------------")

# Mostraremos la suma hecha en el paquete: mi_segundo_paquete
from mi_segundo_paquete.resultados_calculadora import resultado_suma
print(resultado_suma)