import random
import csv
import math

trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
todos_los_sueldos = []

def asignar_sueldos():
    sueldo = random.randint(300000,2500000)
    for i in trabajadores:
        todos_los_sueldos.append == [{"Nombre":(i),
                "Sueldo": sueldo,
                }]

           
def clasificar_sueldos():
    sueldo_bajo = []
    bajo = 0
    sueldo_medio = []
    medio = 0
    sueldo_alto = []
    alto = 0


def estadisticas():

def reporte_sueldos():
    print ("Nombre empleado: {trabajadores} Sueldo Base: ${sueldo} Descuento Salud: {salud} Descuento AFP: {afp} Sueldo Líquido: ${sueldo_liq}")

def salir():
    print("Finalizando programa… \nDesarrollado por Gissel Garcia \nRUT 26.546.495-5")
    break

def main():
    while True:
        opcion = int(input("Elige la opción que deseas ejecutar: \n1.Asignar sueldos aleatorios. \n2. Clasificar sueldos.\n3. Ver estadísticas. \n4. Reporte de sueldos. \n5. Salir del programa"))
        if opcion == 1:
            asignar_sueldos()
        elif opcion == 2:
            clasificar_sueldos()
        elif opcion == 3:
            estadisticas()
        elif opcion == 4:
            reporte_sueldos()
        elif opcion == 5:
            salir()
            break
        else:
            print ("Elige una opción válida.")

