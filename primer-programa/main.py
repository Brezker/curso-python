print("Mi", "nombre", "es", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")

print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")

print(0o123)

print(0x123)

print(3E8)

print(6.62607e-34)

print(0.0000000000000000000001)

print("Me gusta \"Monty Python\"")

print('Me gusta "Monty Python"')

print(2 ** 2 ** 3)

a = 6
b = 3
a /= 2 * b
print(a)

# No puedes hacer comentario multilinea en python ya que este al carecer de llaves, lee el codigo linea por linea, tomando en cuenta los saltos como una parte nueva de un codigo.
# Esto le permite a python leer codigo e interpretarlo solo con indentado dentro del mismo para ejecutar comandos complejos(que dependen de mas de una linea de codigo)

# Uso de input
print("Dime lo que sea...")
anything = input()
print("Hmm...", anything, "... ¿en serio?")

# Como argumento
anything = int(input("Ingresa un número: "))
something = anything ** 2.0
print(anything, "al cuadrado es", something)
# Se coloca int() para convertir la cadena(str) en integer, igual podemos ocupar float() asi mismo podemos usar str() para convertir otros tipos de valores a string

# Calcular hipotenusa
leg_a = float(input("Ingresa la longitud del primer cateto: "))
leg_b = float(input("Ingresa la longitud del segundo cateto: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("La longitud de la hipotenusa es:", hypo)
# Tambien podemos mostrar respuestas o resultados de operaciones sin tener que guardarlos en variables optimizando memoria
print("La longitud de la hipotenusa es:", (leg_a**2 + leg_b**2) ** .5)

# Multiplicar strings
print(3*"hola")
print("hola"*4)

# Imprimir cadenas
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

# Operaciones complejas
x = float(input("Ingresa el valor para x: "))
y = 1./(x + 1./(x + 1./(x + 1./x)))
print("y =", y)

# Encontrar la hora de salida de una reunion
hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))
mins = mins + dura # encuentra el número total de minutos
hour = hour + mins // 60 # encuentra el número de horas ocultas en los minutos y actualiza las horas
mins = mins % 60 # corrige los minutos para que estén en un rango de (0..59)
hour = hour % 24 # corrige las horas para que estén en un rango de (0..23) 
print(hour, ":", mins, sep='')

