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
tabulate.PRESERVE_WHITESPACE = False
import traceback

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
#Funciones auxiliares

def crear_lista_con_datos(data_estructure):
    lista= []
    for datos in data_estructure:
        interno= {}
        interno["Año"] = datos["Año"]
        interno["Código actividad\neconómica"] = datos["Código actividad económica"]
        interno["Nombre actividad\neconómica"] = datos["Nombre actividad económica"]
        interno["Código sector\neconómico"] = datos["Código sector económico"]
        interno["Nombre sector\neconómico"] = datos["Nombre sector económico"]
        interno["Código subsector\neconómico"] = datos["Código subsector económico"]
        interno["Nombre subsector\neconómico"] = datos["Nombre subsector económico"]
        interno["Total ingresos\nnetos"] = datos["Total ingresos netos"]
        interno["Total\ncostos y gastos"] = datos["Total costos y gastos"]
        interno["Total\nsaldo a pagar"] = datos["Total saldo a pagar"]
        interno["Total\nsaldo a favor"] = datos["Total saldo a favor"]
        lista.append(interno)
    return lista


def filtrar_dic_con_por_llaves(dic, lista_de_columnas_aMostrar):
    dic_filt ={}
    for llave in lista_de_columnas_aMostrar:
        dic_filt[llave]=dic[llave]

    return dic_filt

def filtrar_lista_dics_por_columnas(lista_dics,lista_columnas):
    lista_filt = []

    tamanio_lista = len(lista_dics)
    i = 0

    while i<tamanio_lista:
        dic_filt_dado = filtrar_dic_con_por_llaves(lista_dics[i],lista_columnas)
        lista_filt.append(dic_filt_dado)
        i+=1
    return lista_filt


#Esqueleto

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
    respuesta= controller.req_1(control)
    dicc_final= crear_lista_con_datos(respuesta)
    print(tabulate(dicc_final, headers="keys", tablefmt= "grid", stralign= "None", maxcolwidths=15))


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    respuesta= controller.req_2(control)
    dicc_final= crear_lista_con_datos(respuesta)
    print(dicc_final)
    print(tabulate(dicc_final, headers="keys", tablefmt= "grid", stralign= "None", maxcolwidths=15))


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    """
    """

    dates= controller.req_3(control)
    dac= lt.newList("ARRAY_LIST")
    for uno in dates["elements"]:
        interno= {}
        for datos in uno["elements"]:
            reten= 0
            netos= 0
            costos_y_gastos= 0
            saldos_a_pagar= 0
            saldo_a_favor= 0
            interno["Año"]= datos["Año"]
            interno["Código sector\neconómico"] = datos["Código sector económico"]
            interno["Nombre sector\neconómico"] = datos["Nombre sector económico"]
            interno["Código subsector\neconómico"] = datos["Código subsector económico"]
            interno["Nombre subsector\neconómico"] = datos["Nombre subsector económico"]
            reten+= int(datos["Total retenciones"])
            netos+= int(datos["Total ingresos netos"])
            costos_y_gastos+= int(datos["Total costos y gastos"])
            saldos_a_pagar+= int(datos["Total saldo a pagar"])
            saldo_a_favor+= int(datos["Total saldo a favor"])
        interno["Total de retenciones\ndel subsector\neconómico"]= str(reten)
        interno["Total ingresos\nnetos del\nsubsector económico"]= str(netos)
        interno["Total\ncostos y gastos\ndel subsector\neconómico"]= str(costos_y_gastos)
        interno["Total\nsaldo a pagar\ndel subsector\neconómico"]= str(saldos_a_pagar)
        interno["Total\nsaldo a favor\ndel subsector\neconómico"]= str(saldo_a_favor)
        lt.addLast(dac,interno)
    dis= controller.organizar_anio(dac)
    anios= dis.keys()
    anios= sorted(anios)
    for_anios= lt.newList("ARRAY_LIST")
    for fecha in anios:
        for dicc_final in dis[fecha]["elements"]:
            lt.addLast(for_anios,dicc_final)
    print(tabulate(for_anios["elements"], headers="keys", tablefmt= "grid", stralign= "None", maxcolwidths=14))

    
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
    anio =input('Ingrse año a buscar  ')
    req_6 = controller.req_6(control,anio)
    req_6_lista = req_6[0]['elements']
    req_6_tamanio = req_6[1]
    req_6_time = req_6[2]
    respuesta_filtrada =filtrar_lista_dics_por_columnas( req_6_lista,['Código sector económico',
                                              'Nombre sector económico','Total ingresos netos',
                                          'Total costos y gastos','Total saldo a pagar','Total saldo a favor'])
    tabulate_respuesta = tabulate(respuesta_filtrada, headers='keys', tablefmt= "grid", maxcolwidths =[15]*6, maxheadercolwidths=[15]*6)
    print(tabulate_respuesta,"\n")
    tamanio_lista = len(req_6_lista)
    i = 0
    while i< tamanio_lista:
        sector=req_6_lista[i]
        nombre_sector = sector['Nombre sector económico']
        print('Para el sector ',nombre_sector,' , el subsector económico que más aportó es:\n')
        subsector_mayor = sector['Subsector que más contribuyó']
        subsector_mayor_filt = filtrar_dic_con_por_llaves(subsector_mayor,['Código subsector económico',
                                              'Nombre subsector económico','Total ingresos netos',
                                          'Total costos y gastos','Total saldo a pagar','Total saldo a favor'])
        subsect_mayor_tab = tabulate([subsector_mayor_filt], headers='keys', tablefmt= "grid", maxcolwidths =[15]*6, maxheadercolwidths=[15]*6)
        print(subsect_mayor_tab,"\n")
        print('Para el subsector anteriormente presentado que más aporto, las actividades que más y menos aportaron respectivamente son:\n')
        actividad_mas_subsector_mayor = subsector_mayor['Actividad que más contribuyó']
        actividad_menos_subsector_mayor = subsector_mayor['Actividad que menos contribuyó']
        actividad_mas_subsector_mayor_filt = filtrar_dic_con_por_llaves(actividad_mas_subsector_mayor,['Código actividad económica',
                                              'Nombre actividad económica','Total ingresos netos',
                                          'Total costos y gastos','Total saldo a pagar','Total saldo a favor'])
        actividad_menos_subsector_mayor_filt = filtrar_dic_con_por_llaves(actividad_menos_subsector_mayor,['Código actividad económica',
                                              'Nombre actividad económica','Total ingresos netos',
                                          'Total costos y gastos','Total saldo a pagar','Total saldo a favor'])
        tab_mayor_mayor = tabulate([actividad_mas_subsector_mayor_filt], headers='keys', tablefmt= "grid", maxcolwidths =[15]*6, maxheadercolwidths=[15]*6)
        tab_mayor_menor = tabulate([actividad_menos_subsector_mayor_filt], headers='keys', tablefmt= "grid", maxcolwidths =[15]*6, maxheadercolwidths=[15]*6)
        print(tab_mayor_mayor,"\n")
        print(tab_mayor_menor,"\n")
        print('Para el sector ',nombre_sector,' , el subsector económico que MENOS aportó es:\n')
        subsector_menor = sector['subsector que menos aportó']
        subsector_menor_filt = filtrar_dic_con_por_llaves(subsector_menor,['Código subsector económico',
                                              'Nombre subsector económico','Total ingresos netos',
                                          'Total costos y gastos','Total saldo a pagar','Total saldo a favor'])
        subsect_menor_tab = tabulate([subsector_menor_filt], headers='keys', tablefmt= "grid", maxcolwidths =[15]*6, maxheadercolwidths=[15]*6)
        print(subsect_menor_tab,"\n")
        print('Para el subsector anteriormente presentado que MENOS aporto, las actividades que MÁS y MENOS aportaron respectivamente son:\n')
        actividad_mas_subsector_menor = subsector_menor['Actividad que más contribuyó']
        actividad_menos_subsector_menor = subsector_menor['Actividad que menos contribuyó']
        actividad_mas_subsector_menor_filt = filtrar_dic_con_por_llaves(actividad_mas_subsector_menor,['Código actividad económica',
                                              'Nombre actividad económica','Total ingresos netos',
                                          'Total costos y gastos','Total saldo a pagar','Total saldo a favor'])        
        actividad_menos_subsector_menor_filt = filtrar_dic_con_por_llaves(actividad_menos_subsector_menor,['Código actividad económica',
                                              'Nombre actividad económica','Total ingresos netos',
                                          'Total costos y gastos','Total saldo a pagar','Total saldo a favor'])
        

        tab_menor_mayor = tabulate([actividad_mas_subsector_menor_filt], headers='keys', tablefmt= "grid", maxcolwidths =[15]*6, maxheadercolwidths=[15]*6)
        tab_menor_menor = tabulate([actividad_menos_subsector_menor_filt], headers='keys', tablefmt= "grid", maxcolwidths =[15]*6, maxheadercolwidths=[15]*6)
        print(tab_menor_mayor,"\n")
        print(tab_menor_menor,"\n")
        i+=1
    print('TAMAÑO: ',req_6_tamanio,"\n")
    print('TIEMPO: ', req_6_time,"\n")


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    anio_in = input("Ingrese el año inial " )
    anio_fin = input("Ingrese el año final ")
    numero = input("Numero de actividades a identificar ")
    print(controller.req_7(control, numero, anio_in, anio_fin))


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    print(controller.req_8(control))

def printSortResults(sort_books):
    anos= lt.newList("ARRAY_LIST")
    for datos in sort_books["elements"]:
        interno= {}
        interno["Año"] = datos["Año"]
        interno["Código actividad\neconómica"] = datos["Código actividad económica"]
        interno["Nombre actividad\neconómica"] = datos["Nombre actividad económica"]
        interno["Código sector\neconómico"] = datos["Código sector económico"]
        interno["Nombre sector\neconómico"] = datos["Nombre sector económico"]
        interno["Código subsector\neconómico"] = datos["Código subsector económico"]
        interno["Nombre subsector\neconómico"] = datos["Nombre subsector económico"]
        interno["Total ingresos\nnetos"] = datos["Total ingresos netos"]
        interno["Total\ncostos y gastos"] = datos["Total costos y gastos"]
        interno["Total\nsaldo a pagar"] = datos["Total saldo a pagar"]
        interno["Total\nsaldo a favor"] = datos["Total saldo a favor"]
        lt.addFirst(anos,interno)
    anios= controller.organizar_anio(anos)
    anes= anios.keys()
    anes= sorted(anes)
    for fecha in anes:
        dicc_final= lt.newList("ARRAY_LIST")
        union= lt.newList("ARRAY_LIST")
        anios_for= controller.organizar_for_codigo(anios[fecha])
        size = lt.size(anios[fecha])
        if size>=6:
            first= 0
            last= size-3
            print("Las 3 primeras y 3 ultimas actividades economicas del",fecha,"son:\n")
            while last<size:
                datos= anios_for["elements"][last]
                lt.addLast(dicc_final,datos)
                last+= 1
            while first<3:
                datos1= anios_for["elements"][first]
                lt.addFirst(union,datos1)
                first+= 1
            if union!=0:
                for agregar in union["elements"]:
                    lt.addFirst(dicc_final,agregar)
        else:
            i=0
            print("Las",size,"actividades economicas del",fecha,"son:\n")
            while i<size:
                datos= anios_for["elements"][i]
                lt.addLast(dicc_final,datos)
                i+=1
        print(tabulate(dicc_final["elements"], headers="keys", tablefmt= "grid", stralign= "None", maxcolwidths=14))
                

# Se crea el controlador asociado a la vista
control = new_controller("ARRAY_LIST")

"""losimp =[]
    first= 0
    last= size-3
    while last<size:
        datos= dicc_final[last]
        losimp.append(datos)
        last+=1
    while first<sample:
        datos= dicc_final[first]
        losimp.append(datos)
        first+= 1"""

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
                ordenado =printSortResults(sort_data_result[0])
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
