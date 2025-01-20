''' --- CASA DE CAMBIOS ---

2. La casa de cambios se queda un 10% en concepto de ‘tasas de gestión’. Calcula el monto
recibido, el cambio en dólares, la cantidad que se queda la casa de cambios y la cantidad de
dólares restante que recibirá el usuario. Imprime el desglose por pantalla formateado de tal
forma que quede claro para el usuario.'''

# --- Pedimos al usuario la cantidad en euros ---
print("--- BIENVENIDO A LA CASA DE CAMBIOS ---")
euros = float((input("\nIntroduce la cantidad en euros que desea convertir en dólares: ")))

# --- Calculamos la conversión ---
dolares = euros * 1.2

# --- Calculamos la cantidad que se queda la casa de cambios ---
tasas_gestion = dolares * 10 / 100

# --- Calculamos la cantidad de dólares que recibe el usuario ---
dolares_recibidos = dolares - tasas_gestion

# --- Imprimimos el desglose de la operación ---

print("\nMonto ingresado en euros por el usuario:", euros, "€.")
print("Cantidad convertida a dólares:", dolares, "$.")
print("Gastos de gestión:", tasas_gestion, "$.")
print("Total a retirar:", dolares_recibidos, "$.")



