import cowsay
import time
import math
import csv

def convertir_a_mm(valor_cm):
    return valor_cm * 10

def volumen_tanque_cuadrado(longitud, anchura, altura):
    return longitud * anchura * altura

def volumen_tanque_cilindrico(diametro, altura):
    radio = diametro / 2
    return math.pi * radio**2 * altura

def volumen_tanque_ovalado(diametro_a, diametro_b, altura):
    radio_a = diametro_a / 2
    radio_b = diametro_b / 2
    return math.pi * radio_a * radio_b * altura

def convertir_a_litros(volumen_mm3):
    return volumen_mm3 / 1000000

def generar_csv(volumen_total_litros, altura_sensor_mm, nombre_archivo):
    num_pasos = 30
    volumen_por_paso = volumen_total_litros / (num_pasos - 1)

    with open(nombre_archivo, 'w', newline='') as csvfile:
        fieldnames = ['Milimetros', 'Litros']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for paso in range(num_pasos):
            mm = (paso * altura_sensor_mm) / (num_pasos - 1)
            litros = paso * volumen_por_paso
            writer.writerow({'Milimetros': round(mm, 2), 'Litros': f"{litros:.1f}"})

def obtener_datos_y_calcular_volumen(tipo_tanque):
    if tipo_tanque == "cuadrado":
        longitud = float(input("Largo (cm): "))
        anchura = float(input("Ancho (cm): "))
        altura = float(input("Altura (cm): "))
        altura_sensor = float(input("Tamaño del Sensor (mm): "))
        volumen_mm3 = volumen_tanque_cuadrado(convertir_a_mm(longitud), convertir_a_mm(anchura), convertir_a_mm(altura))
    elif tipo_tanque == "cilindrico":
        diametro = float(input("Diámetro (cm): "))
        altura = float(input("Altura (cm): "))
        altura_sensor = float(input("Tamaño del Sensor (mm): "))
        volumen_mm3 = volumen_tanque_cilindrico(convertir_a_mm(diametro), convertir_a_mm(altura))
    elif tipo_tanque == "ovalado":
        diametro_a = float(input("Diámetro A (cm): "))
        diametro_b = float(input("Diámetro B (cm): "))
        altura = float(input("Altura (cm): "))
        altura_sensor = float(input("Tamaño del Sensor (mm): "))
        volumen_mm3 = volumen_tanque_ovalado(convertir_a_mm(diametro_a), convertir_a_mm(diametro_b), convertir_a_mm(altura))
    else:
        raise ValueError("Tipo de tanque no válido")

    volumen_litros = convertir_a_litros(volumen_mm3)
    return volumen_mm3, volumen_litros, altura_sensor

def sub_menu():
    while True:
        print("\nSeleccione el tipo de cálculo de volumen:")
        print("1. Tanque Cuadrado")
        print("2. Tanque Cilíndrico")
        print("3. Tanque Ovalado")
        print("4. Salir")

        try:
            opcion = int(input("Ingrese el número de la opción (1, 2, 3 o 4): "))

            if opcion in [1, 2, 3]:
                nombre_archivo = input("Ingrese el nombre del archivo CSV (incluya '.csv'): ")
                tipo_tanque = ["cuadrado", "cilindrico", "ovalado"][opcion - 1]
                volumen_mm3, volumen_litros, altura_sensor = obtener_datos_y_calcular_volumen(tipo_tanque)
                cowsay.fox("Si las medidas del tanque se tomaron en centímetros, los resultados son los siguientes:")
                print(f"El volumen del tanque {tipo_tanque} es: {volumen_mm3:.2f} mm³ ({volumen_litros:.1f} litros).")
                print(f"Altura del sensor: {altura_sensor} mm")
                generar_csv(volumen_litros, altura_sensor, nombre_archivo)

            elif opcion == 4:
                cowsay.tux("¡Gracias por usar el programa!")
                time.sleep(2)
                break

            else:
                cowsay.dragon("Opción no válida. Intente nuevamente.")

        except ValueError as e:
            cowsay.fox(f"Error: {e}. Por favor, ingrese un número válido.")

def menu_principal():
    while True:
        print("\nMenú Principal:")
        print("1. Calcular Volumen de un Tanque")
        print("2. Salir")

        try:
            opcion = int(input("Seleccione una opción (1 o 2): "))

            if opcion == 1:
                sub_menu()

            elif opcion == 2:
                cowsay.dragon("¡Hasta luego!")
                time.sleep(2)
                break

            else:
                cowsay.tux("Error: Opción no válida. Intente nuevamente.")

        except ValueError:
            cowsay.cow("Error: Por favor, ingrese un número válido.")

menu_principal()
