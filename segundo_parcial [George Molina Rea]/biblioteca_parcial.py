from datos import lista
import json
import pygame
# from segundo_parcial import *
def guarda_sublistas(lista: list):
    '''
    Recibe como parametro una lista la cual va a ser utilizada\n
    para poder manejar una lista la cual sera mas facil de utilizar
    '''
    lista_subfinal = []
    lista_final = []
    lista_preguntas = []
    lista_respuesta = []
    lista_subrespuestas = []
    lista_correcta = []
    for diccionario in lista:
        lista_preguntas.append(diccionario["pregunta"])
        lista_subrespuestas.append(diccionario["a"])
        lista_subrespuestas.append(diccionario["b"])
        lista_subrespuestas.append(diccionario["c"])
        lista_respuesta.append(lista_subrespuestas)
        lista_subrespuestas = []
        lista_correcta.append(diccionario["correcta"])
        lista_subfinal.append(lista_preguntas)
        lista_subfinal.append(lista_respuesta)
        lista_subfinal.append(lista_correcta)
        lista_final.append(lista_subfinal)
        lista_subfinal = []
        lista_preguntas = []
        lista_respuesta = []
        lista_correcta = []
    # print(lista_final[1][0])

    return(lista_final)

# def sonido_momentaneo(clave: str):
#     '''
    
#     '''
#     pygame.init()
#     pygame.mixer.init()
#     sonido_incorrecto = pygame.mixer.Sound(clave)
#     sonido_incorrecto.set_volume(0.9)
#     sonido_incorrecto.play
    


# guarda_sublistas(lista)
def guardar_datajson(lista: list):
    '''
    Recibe como parametro una lista la cual va a ser utilizada\n
    para guardar determinados datos dentro de un archivo json
    '''
    with open("C:/Users/User/Downloads/Curso_de_ingreso_PYTHON-main/Curso_de_ingreso_PYTHON-main/00-Unidades/Programacion_clases/segundo_parcial/scores.json", "w") as archivo:
        json.dump(lista,archivo,indent=4,ensure_ascii=False) 
    

def ordenar_mayor_menor(lista_diccionario_scores: list):
    '''
            Recibe como parametro una lista la cual sera utilizada en el swap\n
              o tambien llamada burbujeo para guardar datos que fueron\n
    ordenados en determinada forma, ya sea de mayor a menor o menor a mayor
    '''
    lista_scores = len(lista_diccionario_scores)

    for i in range(lista_scores):
        for j in range(lista_scores-i-1):
                if lista_diccionario_scores[j]["puntaje"] < lista_diccionario_scores[j+1]["puntaje"]:
                    #swap
                    lista_diccionario_scores[j], lista_diccionario_scores[j+1] = lista_diccionario_scores[j+1], lista_diccionario_scores[j]
    return lista_diccionario_scores


# juegos = len(lista)
# for i in range(juegos):
#     for j in range(juegos-i-1):
#             if lista[j]["puntaje"] < lista[j+1]["puntaje"]:
#                 #swap
#                 # lista[j], lista[j+1] = lista[j+1], lista[j]
#                 aux = lista[j] # Se le asigna el menor puntaje al aux
#                 lista[j] = lista[j+1] # Se le asigna el mayor puntaje a la lista[j], el cual una vez fue lista[j+1]
#                 lista[j+1] = aux # Se le asigna el menor puntaje al lista[j+1]
# print(lista)
                    


