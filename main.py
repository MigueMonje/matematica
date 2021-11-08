# Conseguir datos del usuario
x0 = int(input("X #1: "))
y0 = int(input("Y #1: "))
r0 = int(input("Resultado #1: "))
x1 = int(input("X #2: "))
y1 = int(input("Y #2: "))
r1 = int(input("Resultado #2: "))
print(f"{x0}X + {y0}Y = {r0}\n{x1}X + {y1}Y = {r1}")
# Calcular numero por el que se multiplica segunda ecuacion
mult = -x0/x1
print(f"*{mult}")
# Multiplicar la segunda ecuacion por mult
y1 *= mult
r1 *= mult 
# No se multiplica x1 porque ya se elimina
# Sumar las ecuaciones y encontrar y
yr = y0+y1
rr = r0+r1
y = rr/yr
# Encontar x
x = (r0 - y*y0)/x0
# Mostrar Resultados
print(f"X={x}, Y={y}")
