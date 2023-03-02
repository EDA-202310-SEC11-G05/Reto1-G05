"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
assert cf
from tabulate import tabulate
import traceback

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller(type):
    """
        Se crea una instancia del controlador
    """
    control = controller.new_controller(type)
    return control


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("10- Obtener dato dado un ID")
    print("11- Escoger estructuras de datos para carga de archivo")
    print("0- Salir")


def load_data(control):
    """
    Carga los datos
    """
    
    print("Por favor, escoga una opción para la muestra de datos:")
    print("1- 5%")
    print("2- 10%")
    print("3- 20%")
    print("4- 30%")
    print("5- 50%")
    print("6- 80%")
    print("7- Archivo pequeño \"-small\"")
    print("8- Archivo completo \"-large\"")

    sample = int(input("Su elección: ")) 

    if sample == 1:

        data = controller.load_data(control, cf.data_dir+"\DIAN\Salida_agregados_renta_juridicos_AG-5pct.csv")

    elif sample == 2:

        data = controller.load_data(control, cf.data_dir+"\DIAN\Salida_agregados_renta_juridicos_AG-10pct.csv")

    elif sample == 3:

        data = controller.load_data(control, cf.data_dir+"\DIAN\Salida_agregados_renta_juridicos_AG-20pct.csv")

    elif sample == 4:

        data = controller.load_data(control, cf.data_dir+"\DIAN\Salida_agregados_renta_juridicos_AG-30pct.csv")

    elif sample == 5:

        data = controller.load_data(control, cf.data_dir+"\DIAN\Salida_agregados_renta_juridicos_AG-50pct.csv")

    elif sample == 6:

        data = controller.load_data(control, cf.data_dir+"\DIAN\Salida_agregados_renta_juridicos_AG-80pct.csv")

    elif sample == 7:

        data = controller.load_data(control, cf.data_dir+"\DIAN\Salida_agregados_renta_juridicos_AG-small.csv")

    elif sample == 8:

        data = controller.load_data(control, cf.data_dir+"\DIAN\Salida_agregados_renta_juridicos_AG-large.csv")
    return data


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    data = controller.get_data(control, id)
    print("El dato con el ID", id, "es:", data)

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    print(controller.req_1(control))


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    print(controller.req_2(control))


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    print(controller.req_3(control))


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    print(controller.req_4(control))


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    print(controller.req_5(control))


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    print(controller.req_6(control))


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    print(controller.req_7(control))


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    print(controller.req_8(control))

def printSortResults(sort_books, sample=3):
    size = lt.size(sort_books)
    lista_1 =lt.iterator(sort_books)
    
    if size<= sample*2:
        lista= []
        print('Los',size,'primeros impuestos son:')
        for impuesto in lista_1:
            lista.append(impuesto)
        print(tabulate(lista, tablefmt='grid'))

    else:
        print('Los',sample, 'primeros impuestos son:')
        i=1
        lista1= []
        while i <=sample:
            impuesto = lt.getElement(sort_books, i)
            lista1.append(impuesto)
            i+=1
        print(tabulate(lista1, tablefmt='grid'))
        print('los',sample, 'últimos libros ordenados son:')
        i= size- sample +1
        lista2= []
        while i <=size:
            impuesto = lt.getElement(sort_books, i)
            lista2.append(impuesto)
            i+=1
        print(tabulate(lista2, tablefmt='grid'))

# Se crea el controlador asociado a la vista
control = new_controller("ARRAY_LIST")

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        try:
            if int(inputs) == 1:
                print("Cargando información de los archivos ....\n")
                data = load_data(control)
                sort_data_result = controller.sort(control)
                printSortResults(sort_data_result[0])
                "[]"
                print("El tiempo en milisegundo transcurridos fue de: ",str(sort_data_result[1]))
            
            elif int(inputs) == 2:
                print_req_1(control)

            elif int(inputs) == 3:
                print_req_2(control)

            elif int(inputs) == 4:
                print_req_3(control)

            elif int(inputs) == 5:
                print_req_4(control)

            elif int(inputs) == 6:
                print_req_5(control)

            elif int(inputs) == 7:
                print_req_6(control)

            elif int(inputs) == 8:
                print_req_7(control)

            elif int(inputs) == 9:
                print_req_8(control)

            elif int(inputs) == 10:
                id = input("Ingrese un id: ")
                print_data(control, id)

            elif int(inputs) == 0:
                working = False
                print("\nGracias por utilizar el programa")
                
            else:
                print("Opción errónea, vuelva a elegir.\n")
        except ValueError:
            print("Ingrese una opción válida.\n")
            traceback.print_exc()
    sys.exit(0)
