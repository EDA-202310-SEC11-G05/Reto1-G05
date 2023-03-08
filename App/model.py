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


#Funciones de busqueda y arreglos en los requerimientos.

def organizar_anio (data_structs, categoria):
    # Complejidad: O(n)
    tamanio = lt.size(data_structs)
    i=0
    anios= {}
    while i < tamanio:
        variable= lt.getElement(data_structs,i)
        momento= variable[categoria]
        if variable[categoria] not in anios.keys():
            anios[momento] = lt.newList(datastructure="ARRAY_LIST")
            lt.addLast(anios[momento], variable )
        elif variable[categoria] in anios.keys():
            lt.addLast(anios[momento], variable)
        i+=1
    return anios


def ayuda_req_1_y_2(data_structs,dato_a_comparar):
    # Complejidad: O(nlogn)
    anios= organizar_anio(data_structs["data"], "Año")
    mayor= lt.newList(datastructure="ARRAY_LIST")
    for fecha in anios.keys():
        i=0
        b=0
        tamanio= lt.size(anios[fecha])
        while i < tamanio:
            exacto= lt.getElement(anios[fecha],i)
            if int(exacto[dato_a_comparar])>b:
                alto= exacto
                b= int(exacto[dato_a_comparar])
            i+=1
        lt.addLast(mayor, alto)
    
    respuesta= lt.newList("ARRAY_LIST")
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

    # Complejidad total: O(nlogn)
    datos=  ayuda_req_1_y_2(data_structs,"Total saldo a pagar")
    return datos


def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # Complejidad total: O(nlogn)
    datos= ayuda_req_1_y_2(data_structs,"Total saldo a favor")
    return datos


def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    anios= organizar_anio(data_structs["data"], "Año")
    mayor= lt.newList(datastructure="ARRAY_LIST")
    for fecha in anios.keys():
        i=0
        b=9999999999999999999
        tamanio= lt.size(anios[fecha])
        alto= lt.newList("ARRAY_LIST")
        while i < tamanio:
            exacto= lt.getElement(anios[fecha],i)
            if int(exacto["Otras retenciones"])<b:
                lt.addLast(alto,exacto)
                b= int(exacto["Otras retenciones"])
            i+=1
        seg_tamanio= lt.size(alto)
        datos= lt.newList("ARRAY_LIST")
        n= 0
        info_inter= lt.newList("ARRAY_LIST")
        for menor in alto["elements"]:
            b=9999999999999999999999
            necesary= None
            if int(menor["Otras retenciones"])<b:
                b= menor["Otras retenciones"]
                necesary= menor
        lt.addFirst(info_inter,necesary)
        infe= info_inter["elements"]
        while n<tamanio:
            codigo= lt.getElement(anios[fecha],n)
            if (int(infe[0]["Código actividad económica"]!=int(codigo["Código actividad económica"]))) and (int(infe[0]["Código sector económico"])==int(codigo["Código sector económico"])) and (int(infe[0]["Código subsector económico"])==int(codigo["Código subsector económico"])):
                darko= codigo
                lt.addLast(datos,darko)
            n+=1
        lt.addLast(mayor,datos)
    return mayor

def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """

    # Organizar por año: O(n)
    anios= organizar_anio(data_structs["data"], "Año")

    # Organizar por costos y gastos de nómina O(nlogn)

    # Organizar por costos y gastos de nómina O(nlogn)
    mayor= lt.newList(datastructure="ARRAY_LIST")
    for fecha in anios.keys():
        i=0
        b=0
        tamanio= lt.size(anios[fecha])
        while i < tamanio:
            exacto= lt.getElement(anios[fecha],i)
            if int(exacto["Costos y gastos nómina"])>b:
                alto= exacto
                b= int(exacto["Costos y gastos nómina"])
            i+=1
        lt.addLast(mayor, alto)
    respuesta= lt.newList("ARRAY_LIST")
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

    years = {}


    # Para hacer sublistas con los años O(n)
    for anio in anios.keys():
        for element in anios[anio]["elements"]:
            if element["Año"] not in years:
                years[element["Año"]] = []
                years[element["Año"]].append(element)
            else:
                years[element["Año"]].append(element)
                

    smaller_bigger = {}

    # Code to find three first and last items O(n^2)
    # Code to find three first and last items O(n^2)
    for element in years.keys():
        data = years[element]
        if len(data)>=6:
            smaller_bigger[data[0]["Año"]] = [data[:3], data[len(data)-3:len(data)]]
        else:
            smaller_bigger[data[0]["Año"]] = data
    
    return datos, smaller_bigger


def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs, anio):
    """
    Función que soluciona el requerimiento 6
    """

    # Complejidad total: O(n)
    tamanio_data_struct = data_size(data_structs)
    dic_anios = crear_diccionario (data_structs, 'data' ,'Año',tamanio_data_struct)
    array_del_anio = dic_anios[anio]
    tamanio_array_anio = lt.size(array_del_anio)
    dic_subsectores = crear_diccionario_de_TAD(array_del_anio, 'Código subsector económico', tamanio_array_anio )
    lista_subsectores = crear_lista_subsectores_por_anio(array_del_anio)
    lista_sectores = crear_lista_sectores_totalizados_por_anio(lista_subsectores)
    for sector in lt.iterator(lista_sectores):
        codigo_sector_dado = sector['Código sector económico']
        mayor_subsector_para_sector_dado = encontrar_mayor_con_condicion(lista_subsectores,'Total ingresos netos',codigo_sector_dado)
        codigo_mayor_subsector = mayor_subsector_para_sector_dado['Código subsector económico']
        lista_actividades_subsector_MAY_dado = dic_subsectores[codigo_mayor_subsector]
        mayor_actividad_mayor_subsector = encontrar_mayor(lista_actividades_subsector_MAY_dado,'Total ingresos netos')
        menor_actividad_mayor_subsector = encontrar_menor(lista_actividades_subsector_MAY_dado, 'Total ingresos netos')
        mayor_subsector_para_sector_dado['Actividad que más contribuyó']= mayor_actividad_mayor_subsector
        mayor_subsector_para_sector_dado['Actividad que menos contribuyó']=menor_actividad_mayor_subsector
        sector['Subsector que más contribuyó'] = mayor_subsector_para_sector_dado
        menor_subsector_para_sector_dado = encontrar_menor_con_condicion(lista_subsectores, 'Total ingresos netos', codigo_sector_dado)
        codigo_menor_subsector = menor_subsector_para_sector_dado['Código subsector económico']
        lista_actividades_subsector_menor = dic_subsectores[codigo_menor_subsector]
        mayor_actividad_menor_subsector = encontrar_mayor(lista_actividades_subsector_menor,'Total ingresos netos')
        menor_actividad_menor_subsector = encontrar_menor(lista_actividades_subsector_menor,'Total ingresos netos')
        menor_subsector_para_sector_dado['Actividad que más contribuyó']=mayor_actividad_menor_subsector
        menor_subsector_para_sector_dado['Actividad que menos contribuyó']= menor_actividad_menor_subsector
        sector['subsector que menos aportó'] = menor_subsector_para_sector_dado
    return lista_sectores


def req_7(data_structs, numero, anio_inicial, anio_final):
    """
    Función que soluciona el requerimiento 7
    """
    tamanio = data_size(data_structs)
    anios = crear_diccionario(data_structs,"data", "Año", tamanio)
    orden_anios = ordenar_dic(anios)
    
    por_anio = lt.newList()
    for fecha in orden_anios.keys():
        
        if int(fecha) >= int(anio_inicial) and int(fecha)<= int(anio_final):
            
            lt.addLast(por_anio, orden_anios[fecha])
    i = 0
    listas_org = lt.newList(datastructure="ARRAY_LIST")
    while i<lt.size(por_anio):
        inicial = lt.getElement(por_anio,i)
        merg.sort(inicial, sort_criteria_total_costos)
        lt.addLast(listas_org, inicial)

        i +=1
    e = 0
    
    final = lt.newList("SINGLE_LINKED")
    while e < int(numero):
        menor_primer = lt.newList(datastructure="ARRAY_LIST")
    
        for pos_lista in lt.iterator(listas_org):
            prim = lt.firstElement(pos_lista)
            lt.addLast(menor_primer, prim)
        
        men = encontrar_menor_pos(menor_primer, "Total costos y gastos")
        lt.addLast(final, men[0])
        elim = lt.getElement(listas_org, men[1])
        lt.removeFirst(elim)
        e+=1
        
    return final


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

# Funciones de busqueda

def encontrar_mayor(lista, criterio):
    i =0
    tamanio = lt.size(lista)
    mayor = 0
    respuesta ={}
    while i < tamanio:
        exacto = lt.getElement(lista,i)
        if float(exacto[criterio])>float(mayor):
            mayor = exacto[criterio]
            respuesta = exacto
        i+=1
    return respuesta

def encontrar_mayor_con_condicion(lista, criterio, condicion):
    i =0
    tamanio = lt.size(lista)
    mayor = 0
    respuesta ={}
    while i < tamanio:
        exacto = lt.getElement(lista,i)

        if exacto['Código sector económico'] ==  condicion:
        
             if float(exacto[criterio])>float(mayor):
                mayor = exacto[criterio]
                respuesta = exacto
        i+=1
    return respuesta

def encontrar_menor_con_condicion(lista, criterio, condicion):
    i =0
    tamanio = lt.size(lista)
    menor = 9999999999999
    respuesta ={}
    while i < tamanio:
        exacto = lt.getElement(lista,i)

        if exacto['Código sector económico'] ==  condicion:
        
             if float(exacto[criterio])<float(menor):
                menor = exacto[criterio]
                respuesta = exacto
        i+=1
    return respuesta

# encontrar menor en TAD lista de diccionarios
def encontrar_menor(lista, criterio):
    
    i =0
    tamanio = lt.size(lista)
    respuesta ={}
    menor = 9999999999999
    while i <= tamanio:
        exacto = lt.getElement(lista,i)
        if float(exacto[criterio])<float(menor):
            respuesta = exacto
            menor = exacto[criterio]
        i+=1
    return respuesta

def encontrar_menor_pos(lista, criterio):
    i =0
    tamanio = lt.size(lista)
    respuesta ={}
    pos = 0
    menor = 9999999999999
    while i <= tamanio:
        exacto = lt.getElement(lista,i)
        if float(exacto[criterio])<float(menor):
            respuesta = exacto
            menor = exacto[criterio]
            pos = i
        i+=1
    return respuesta, pos

def crear_diccionario (data_structs, tipo ,categoria,tamanio):

    # Complejidad: O(n)
    
    i =0
    dic = {}
    while i < tamanio:
        variable = lt.getElement(data_structs[tipo],i)
        momento = variable[categoria]
        if variable[categoria] not in dic.keys():
            dic[momento] = lt.newList(datastructure="ARRAY_LIST")
            lt.addLast(dic[momento], variable )
        elif variable[categoria] in dic.keys():
            lt.addLast(dic[momento], variable  )
        
        i +=1
    return dic

### Crea diccionario a partir de TAD lista(ARRAY o LINKED), no DataStructs:
def crear_diccionario_de_TAD (TAD ,categoria,tamanio):
    
    i =0
    dic = {}
    
    while i < tamanio:
        variable = lt.getElement(TAD,i)
        momento = variable[categoria]
        if variable[categoria] not in dic.keys():
            dic[momento] = lt.newList(datastructure="ARRAY_LIST")
            lt.addLast(dic[momento], variable )
        elif variable[categoria] in dic.keys():
            lt.addLast(dic[momento], variable  )
        
        i +=1
    return dic


#ordenar la lista en orden
def ordenar(lista, criterio, repeticiones, donde ):
    #organiza por años de menor a mayor
    respuesta = lt.newList("SINGLE_LINKED")
    for x in range( repeticiones):
        inicio = lt.getElement(lista,donde)
        superior = int(inicio[criterio])
        dict = inicio
        a = 0
        elim = 0
        while a < lt.size(lista):
            pos = lt.getElement(lista,a)
            if  int(pos[criterio])>int(superior) and int(pos[criterio]) != int(superior):
                superior = int(pos[criterio])
                elim = a
                dict = pos
            a+=1
        lt.addFirst(respuesta, dict)
        lt.deleteElement(lista, elim)
    return respuesta 


def ordenar_dic(dic):
    dic_keys = dic.keys()
    keys = sorted(dic_keys)
    orden_keys = {}
    for key in keys:
        orden_keys[key] = dic[key]
    return orden_keys


#suma la variable dentro de una lista con un criterio expecifico

def suma_variable(dic, suma):
    tamanio = lt.size(dic)
    i = 0
    valor = 0
    while i < tamanio:
        pos = lt.getElement(dic, i)
        valor += int(pos[suma])
        i+=1
    return valor


# Crea lista TAD ARRAY de subsectores por año
def crear_lista_subsectores_por_anio(lista_actividades):
   
    dic_subsecs ={}
    lista_actividades = lt.iterator(lista_actividades)
    
    for impuesto in lista_actividades:
        llave_subsector_dado =impuesto['Código subsector económico']
        if llave_subsector_dado not in dic_subsecs.keys():
            
            dict_subsector_dado = {}
            dict_subsector_dado['Año']=impuesto['Año']
            dict_subsector_dado['Código sector económico']=impuesto['Código sector económico']
            dict_subsector_dado['Nombre sector económico']=impuesto['Nombre sector económico']
            dict_subsector_dado['Código subsector económico']=impuesto['Código subsector económico']
            dict_subsector_dado['Nombre subsector económico']=impuesto['Nombre subsector económico']
            dict_subsector_dado['Total retenciones']=float(impuesto['Total retenciones'])
            dict_subsector_dado['Total ingresos netos']=float(impuesto['Total ingresos netos'])
            dict_subsector_dado['Total costos y gastos']=float(impuesto['Total costos y gastos'])
            dict_subsector_dado['Total saldo a pagar']=float(impuesto['Total saldo a pagar'])
            dict_subsector_dado['Total saldo a favor']=float(impuesto['Total saldo a favor'])
            dict_subsector_dado['Primeras y últimas 3 actividades en contribuir'] = 0

            dic_subsecs[llave_subsector_dado]=dict_subsector_dado
        else:
            dict_subsector_dado =dic_subsecs[llave_subsector_dado]
            dict_subsector_dado['Total retenciones']+=float(impuesto['Total retenciones'])
            dict_subsector_dado['Total ingresos netos']+=float(impuesto['Total ingresos netos'])
            dict_subsector_dado['Total costos y gastos']+=float(impuesto['Total costos y gastos'])
            dict_subsector_dado['Total saldo a pagar']+=float(impuesto['Total saldo a pagar'])
            dict_subsector_dado['Total saldo a favor']+=float(impuesto['Total saldo a favor'])
          
    lista_subsects=lt.newList(datastructure="ARRAY_LIST")
    for llave in dic_subsecs.keys():
        lt.addLast(lista_subsects,dic_subsecs[llave])

    return lista_subsects


#Lista de subsectores completos por año
def crear_lista_sectores_totalizados_por_anio(lista_subsects):
       
    dic_secs ={}
    lista_subsects = lt.iterator(lista_subsects)
    for subsector in lista_subsects:
        llave_sector_dado =subsector['Código sector económico']
        if subsector not in dic_secs.values():
            dict_sector_dado = {}
            dict_sector_dado['Nombre sector económico']=subsector['Nombre sector económico']
            dict_sector_dado['Código sector económico']=subsector['Código sector económico']
            dict_sector_dado['Total ingresos netos']=float(subsector['Total ingresos netos'])
            dict_sector_dado['Total costos y gastos']=float(subsector['Total costos y gastos'])
            dict_sector_dado['Total saldo a pagar']=float(subsector['Total saldo a pagar'])
            dict_sector_dado['Total saldo a favor']=float(subsector['Total saldo a favor'])
            dic_secs[llave_sector_dado]=dict_sector_dado
        else:
            dict_sector_dado =dic_secs[llave_sector_dado]
            dict_sector_dado['Total retenciones']+=float(subsector['Total retenciones'])
            dict_sector_dado['Total ingresos netos']+=float(subsector['Total ingresos netos'])
            dict_sector_dado['Total costos y gastos']+=float(subsector['Total costos y gastos'])
            dict_sector_dado['Total saldo a pagar']+=float(subsector['Total saldo a pagar'])
            dict_sector_dado['Total saldo a favor']+=float(subsector['Total saldo a favor'])
    lista_sects=lt.newList(datastructure="ARRAY_LIST")
    for llave in dic_secs.keys():
        lt.addLast(lista_sects,dic_secs[llave])
    return lista_sects


# Funciones de ordenamiento

def sort_req4(tax1, tax2):
    if tax1["Año"] != tax2["Año"]:
        return tax1["Año"] > tax2["Año"]
    else:
        return tax1["Costos y gastos nómina"] > tax2["Costos y gastos nómina"]


def sort_criteria_of_codigo(impuesto_1,impuesto_2):
    if impuesto_1['Código sector\neconómico']!= impuesto_2['Código sector\neconómico']:
        cod_1 = impuesto_1['Código sector\neconómico'].split()[0].split('/')[0]
        cod_2 = impuesto_2['Código sector\neconómico'].split()[0].split('/')[0]
        return(float(cod_1)<float(cod_2))
    

def sort_criteria_total_costos(a,b):
        cod_1 = a["Total costos y gastos"].split()[0].split('/')[0]
        cod_2 = b["Total costos y gastos"].split()[0].split('/')[0]
        return(float(cod_1)<float(cod_2))
    

def sort_criteria_of_codigo_req3(impuesto_1,impuesto_2):
    if impuesto_1['Código actividad económica']!= impuesto_2['Código actividad económica']:
        cod_1 = impuesto_1['Código actividad economica'].split()[0]
        cod_2 = impuesto_2['Código actividad economica'].split()[0]
        return(float(impuesto_1['Código actividad economica'])< float(impuesto_2['Código actividad economica']))


def datos_organizar_para_cada_anio(anios,anes):
    info_for_anios=lt.newList("ARRAY_LIST")
    for fecha in anes:
        dicc_final= lt.newList("ARRAY_LIST")
        union= lt.newList("ARRAY_LIST")
        print(anios)
        anios_for= organizar_for_codigo_req3(anios[fecha])
        size = lt.size(anios[fecha])
        if size>=6:
            first= 0
            last= size-3
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
            while i<size:
                datos= anios_for["elements"][i]
                lt.addLast(dicc_final,datos)
                i+=1
        lt.addLast(info_for_anios,dicc_final)
    return info_for_anios


def organizar_for_codigo(data_structs):
    lista = merg.sort(data_structs, sort_criteria_of_codigo)
    return lista


def organizar_for_codigo_req3(data_structs):
    tamanio= lt.size(data_structs)
    if tamanio>1:
        lista = merg.sort(data_structs, sort_criteria_of_codigo_req3)
        return lista
    else:
        return data_structs


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
