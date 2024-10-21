# convertidor.py
from temperatura import *
from masa import *
from tiempo import *

def main():
    print("Selecciona la categoría de conversión:")
    print("1. Temperatura")
    print("2. Masa")
    print("3. Tiempo")
    categoria = input("Ingresa el número de la categoría: ")

    if categoria == '1':
        valor = float(input("Ingresa el valor: "))
        unidad_origen = input("Ingresa la unidad de origen (C, F, K): ")
        unidad_destino = input("Ingresa la unidad de destino (C, F, K): ")
        
        # Lógica de conversión para temperatura
        if unidad_origen == 'C':
            if unidad_destino == 'F':
                resultado = celsius_a_fahrenheit(valor)
            elif unidad_destino == 'K':
                resultado = celsius_a_kelvin(valor)
        elif unidad_origen == 'F':
            if unidad_destino == 'C':
                resultado = fahrenheit_a_celsius(valor)
            elif unidad_destino == 'K':
                resultado = fahrenheit_a_kelvin(valor)
        elif unidad_origen == 'K':
            if unidad_destino == 'C':
                resultado = kelvin_a_celsius(valor)
            elif unidad_destino == 'F':
                resultado = kelvin_a_fahrenheit(valor)
        
        print(f"Resultado: {resultado} {unidad_destino}")

    elif categoria == '2':
        valor = float(input("Ingresa el valor: "))
        unidad_origen = input("Ingresa la unidad de origen (kg, g, t): ")
        unidad_destino = input("Ingresa la unidad de destino (kg, g, t): ")
        
        # Lógica de conversión para masa
        if unidad_origen == 'kg':
            if unidad_destino == 'g':
                resultado = kg_a_g(valor)
            elif unidad_destino == 't':
                resultado = kg_a_t(valor)
        elif unidad_origen == 'g':
            if unidad_destino == 'kg':
                resultado = g_a_kg(valor)
            elif unidad_destino == 't':
                resultado = g_a_t(valor)
        elif unidad_origen == 't':
            if unidad_destino == 'kg':
                resultado = t_a_kg(valor)
            elif unidad_destino == 'g':
                resultado = t_a_g(valor)

        print(f"Resultado: {resultado} {unidad_destino}")

    elif categoria == '3':
        valor = float(input("Ingresa el valor: "))
        unidad_origen = input("Ingresa la unidad de origen (seg, min, hr): ")
        unidad_destino = input("Ingresa la unidad de destino (seg, min, hr): ")
        
        # Lógica de conversión para tiempo
        if unidad_origen == 'seg':
            if unidad_destino == 'min':
                resultado = seg_a_min(valor)
            elif unidad_destino == 'hr':
                resultado = seg_a_hr(valor)
        elif unidad_origen == 'min':
            if unidad_destino == 'seg':
                resultado = min_a_seg(valor)
            elif unidad_destino == 'hr':
                resultado = min_a_hr(valor)
        elif unidad_origen == 'hr':
            if unidad_destino == 'seg':
                resultado = hr_a_seg(valor)
            elif unidad_destino == 'min':
                resultado = hr_a_min(valor)

        print(f"Resultado: {resultado} {unidad_destino}")

if __name__ == "__main__":
    main()
