"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs(type):
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    data_structs = {
        "data": None,
    }

    data_structs["data"] = lt.newList(datastructure=type,
                                     cmpfunction=compare)

    return data_structs


# Funciones para agregar informacion al modelo

def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    d = new_data(data["Año"],data["Código actividad económica"],data["Nombre actividad económica"],data["Código sector económico"],
                 data["Nombre sector económico"],data["Código subsector económico"],data["Nombre subsector económico"],
                 data["Costos y gastos nómina"],data["Aportes seguridad"],data["Aportes a entidades"],data["Efectivo y equivalentes"],
                 data["Inversiones e instrumentos"],data["Cuentas y otros por cobrar"],data["Inventarios"],data["Propiedades"],
                 data["Otros activos"],data["Total patrimonio bruto"],data["Pasivos"],data["Total patrimonio líquido"],
                 data["Ingresos ordinarios"],data["Ingresos financieros"],data["Otros ingresos"],data["Total ingresos brutos"],
                 data["Devoluciones, rebajas"],data["Ingresos no renta"],data["Total ingresos netos"],data["Costos"],
                 data["Gastos administración"],data["Gastos distribución"],data["Gastos financieros"],data["Otros gastos"],
                 data["Total costos y gastos"],data["Renta líquida ordinaria"],data["Pérdida líquida"],data["Compensaciones"],
                 data["Renta líquida"],data["Renta presuntiva"],data["Renta exenta"],data["Rentas gravables"],data["Renta líquida gravable"],
                 data["Ingresos ganancias ocasionales"],data["Costos ganancias ocasionales"],data["Ganancias ocasionales no gravadas"],
                 data["Ganancias ocasionales gravables"],data["Impuesto RLG"],data["Descuentos tributarios"],data["Impuesto neto de renta"],
                 data["Impuesto ganancias ocasionales"],data["Total Impuesto a cargo"],data["Anticipo renta año anterior"],data["Saldo a favor año anterior"],
                 data["Autorretenciones"],data["Otras retenciones"],data["Total retenciones"],data["Anticipo renta siguiente año"],
                 data["Saldo a pagar por impuesto"],data["Sanciones"],data["Total saldo a pagar"],data["Total saldo a favor"])
    lt.addLast(data_structs["data"], d)
    return data_structs

# Funciones para creacion de datos

def new_data(Anio,Codigo_actividad_económica,Nombre_actividad_economica,Codigo_sector_economico,Nombre_sector_economico,Codigo_subsector_economico,Nombre_subsector_economico,Costos_y_gastos_nomina,Aportes_seguridad,Aportes_a_entidades,Efectivo_y_equivalentes,Inversiones_e_instrumentos,Cuentas_y_otros_por_cobrar,Inventarios,Propiedades,Otros_activos,Total_patrimonio_bruto,Pasivos,Total_patrimonio_liquido,Ingresos_ordinarios,Ingresos_financieros,Otros_ingresos,Total_ingresos_brutos,Devoluciones_rebajas,Ingresos_no_renta,Total_ingresos_netos,Costos,Gastos_administracion,Gastos_distribucion,Gastos_financieros,Otros_gastos,Total_costos_y_gastos,Renta_liquida_ordinaria,Perdida_liquida,Compensaciones,Renta_liquida,Renta_presuntiva,Renta_exenta,Rentas_gravables,Renta_liquida_gravable,Ingresos_ganancias_ocasionales,Costos_ganancias_ocasionales,Ganancias_ocasionales_no_gravadas,Ganancias_ocasionales_gravables,Impuesto_RLG,Descuentos_tributarios,Impuesto_neto_de_renta,Impuesto_ganancias_ocasionales,Total_Impuesto_a_cargo,Anticipo_renta_anio_anterior,Saldo_a_favor_anio_anterior,Autorretenciones,Otras_retenciones,Total_retenciones, Anticipo_renta_siguiente_anio,Saldo_a_pagar_por_impuesto,Sanciones,Total_saldo_a_pagar,Total_saldo_a_favor):
    data= {"Año":Anio,"Código actividad económica":Codigo_actividad_económica,"Nombre actividad económica":Nombre_actividad_economica,
           "Código sector económico":Codigo_sector_economico,"Nombre sector económico":Nombre_sector_economico,
           "Código subsector económico":Codigo_subsector_economico,"Nombre subsector económico":Nombre_subsector_economico,
           "Costos y gastos nómina":Costos_y_gastos_nomina,"Aportes seguridad":Aportes_seguridad,"Aportes a entidades":Aportes_a_entidades,
           "Efectivo y equivalentes":Efectivo_y_equivalentes,"Inversiones e instrumentos":Inversiones_e_instrumentos,
           "Cuentas y otros por cobrar":Cuentas_y_otros_por_cobrar,"Inventarios":Inventarios,"Propiedades":Propiedades,"Otros activos":Otros_activos,
           "Total patrimonio bruto":Total_patrimonio_bruto,"Pasivos":Pasivos,"Total patrimonio líquido":Total_patrimonio_liquido,
           "Ingresos ordinarios":Ingresos_ordinarios,"Ingresos financieros":Ingresos_financieros,"Otros ingresos":Otros_ingresos,
           "Total ingresos brutos":Total_ingresos_brutos,"Devoluciones, rebajas":Devoluciones_rebajas,"Ingresos no renta":Ingresos_no_renta,
           "Total ingresos netos":Total_ingresos_netos,"Costos":Costos,"Gastos administración":Gastos_administracion,"Gastos distribución":Gastos_distribucion,
           "Gastos financieros":Gastos_financieros,"Otros gastos":Otros_gastos,"Total costos y gastos":Total_costos_y_gastos,
           "Renta líquida ordinaria":Renta_liquida_ordinaria,"Pérdida líquida":Perdida_liquida,"Compensaciones":Compensaciones,"Renta líquida":Renta_liquida,
           "Renta presuntiva":Renta_presuntiva,"Renta exenta":Renta_exenta,"Rentas gravables":Rentas_gravables,"Renta líquida gravable":Renta_liquida_gravable,
           "Ingresos ganancias ocasionales":Ingresos_ganancias_ocasionales,"Costos ganancias ocasionales":Costos_ganancias_ocasionales,
           "Ganancias ocasionales no gravadas":Ganancias_ocasionales_no_gravadas,"Ganancias ocasionales gravables":Ganancias_ocasionales_gravables,
           "Impuesto RLG":Impuesto_RLG,"Descuentos tributarios":Descuentos_tributarios,"Impuesto neto de renta":Impuesto_neto_de_renta,
           "Impuesto ganancias ocasionales":Impuesto_ganancias_ocasionales,"Total Impuesto a cargo":Total_Impuesto_a_cargo,
           "Anticipo renta año anterior":Anticipo_renta_anio_anterior,"Saldo a favor año anterior":Saldo_a_favor_anio_anterior,"Autorretenciones":Autorretenciones,
           "Otras retenciones":Otras_retenciones,"Total retenciones":Total_retenciones,"Anticipo renta siguiente año":Anticipo_renta_siguiente_anio,
           "Saldo a pagar por impuesto":Saldo_a_pagar_por_impuesto,"Sanciones":Sanciones,"Total saldo a pagar":Total_saldo_a_pagar,"Total saldo a favor":Total_saldo_a_favor}
    return data


# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    pos_data = lt.isPresent(data_structs["data"], id)
    if pos_data > 0:
        data = lt.getElement(data_structs["data"], pos_data)
        return data
    return None


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    return lt.size(data_structs["data"])


#Funciones de busqueda y arreglos por año.

def organizar_anio (data_structs, categoria):
    tamanio = data_size(data_structs)
    i =0
    anios = {}
    while i < tamanio:
        variable = lt.getElement(data_structs["data"],i)
        momento = variable[categoria]
        if variable[categoria] not in anios.keys():
            anios[momento] = lt.newList(datastructure="ARRAY_LIST")
            lt.addLast(anios[momento], variable )
        elif variable[categoria] in anios.keys():
            lt.addLast(anios[momento], variable  )
        
        i +=1
    return anios


def ayuda_req_1_y_2(data_structs,dato_a_comparar):
    anios = organizar_anio(data_structs, "Año")
    
    mayor = lt.newList(datastructure="ARRAY_LIST")
    for fecha in anios.keys():
        i =0
        b=0
        tamanio = lt.size(anios[fecha])
        while i < tamanio:
            exacto = lt.getElement(anios[fecha],i)
            if int(exacto[dato_a_comparar])>b:
                alto= exacto
                b= int(exacto[dato_a_comparar])
            i+=1
        lt.addLast(mayor, alto)
    
    respuesta = lt.newList("ARRAY_LIST")
    for x in range( lt.size(mayor)):

        superior = 0
        a = 0
        elim = 0
        while a < lt.size(mayor):
            pos = lt.getElement(mayor,a)
            if  int(pos["Año"])>superior:
                superior = int(pos["Año"])
                elim = a
                dict = pos
            a+=1
        lt.addFirst(respuesta, dict)
        lt.deleteElement(mayor, elim)
    datos = lt.iterator(respuesta)
    return datos


#Requerimientos

def req_1(data_structs):
    """
    Función que soluciona el requerimiento 1
    """
    datos=  ayuda_req_1_y_2(data_structs,"Total saldo a pagar")
    return datos


def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    datos= ayuda_req_1_y_2(data_structs,"Total saldo a favor")
    return datos


def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass


def req_4(data_structs)-> tuple:
    """Muestra los primeros y últimos 3 impuestos organizada por costos
       y gastos de nómina.
    
    Args:
        data_structs: Estructura de datos
    Returns:
        tuple: Tupla en la que el primer elemento es la sublista conteniendo
               los primeros 3 impuestos menores y el segundo es la sublista
               conteniendo los últimos 3 impuestos mayores.

    """
    # Ordenamiento por Año/Costos y gastos de nómina
    quk.sort(data_structs, sort_req4)
    
    # First three items by smaller Año/Costos y gastos de nómina
    smaller = lt.subList(data_structs, 1, 3)

    # First three items by smaller Año/Costos y gastos de nómina
    bigger = lt.subList(data_structs, (lt.size(data_structs)-3), 3) 

    return smaller, bigger
    


def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass

#* Funciones de comparación

def cmp_taxes_by_year_code(tax1, tax2):
    """Devuelve verdadero (True) si el año de impuesto1 es menor que el de impuesto2,
    en caso de que sean iguales tenga en cuenta el código de la actividad económica,
    de lo contrario devuelva falso (False).

    Args:
        tax1: información del primer registro de impuestos que incluye el “Año” y el
        “Código actividad económica”

        tax2: información del segundo registro de impuestos que incluye el “Año” y el
        “Código actividad económica”
    """
    if tax1["Año"] < tax2["Año"]:
        return True
    elif tax1["Año"] == tax2["Año"]:
        if tax1["Código actividad económica"] < tax2["Código actividad económica"]:
            return True
    else:
        return False

# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    if data_1["id"] > data_2["id"]:
        return 1
    elif data_1["id"] < data_2["id"]:
        return -1
    else:
        return 0

# Funciones de ordenamiento

def sort_req4(tax1, tax2):
    if tax1["Año"] != tax2["Año"]:
        return tax1["Año"] > tax2["Año"]
    else:
        return tax1["Costos y gastos nómina"] > tax2["Costos y gastos nómina"]

def sort_criteria(impuesto_1, impuesto_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento
    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_
    Returns:
        _type_: _description_
    """
    
    if impuesto_1['Año']!= impuesto_2['Año']:
        cod_1 = impuesto_1['Año'].split()[0]
        cod_2 = impuesto_2['Año'].split()[0]
        return(float(impuesto_1['Año'])> float(impuesto_2['Año']))
    
    else:
        cod_1 = impuesto_1['Código actividad económica'].split()[0].split('/')[0]
        cod_2 = impuesto_2['Código actividad económica'].split()[0].split('/')[0]
        return(float(cod_1)>float(cod_2))


def sort(data_structs):
    sub_list = lt.subList(data_structs['data'],1,data_size(data_structs))
    lista = merg.sort(sub_list, sort_criteria)
    return lista
