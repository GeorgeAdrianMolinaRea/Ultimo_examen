import pygame
from datos import lista
from biblioteca_parcial import *
from pygame.locals import *
'''
Nombre del estudiante: George Adrian Molina Rea
DNI: 46.705.198
'''
pygame.init()
# Se asigna un nombre al juego
pygame.display.set_caption("Mi primer juego")
# Sonido
pygame.mixer.init()
pygame.mixer.music.set_volume(0.9)
# sonido de fondo
sonido_fondo = pygame.mixer.Sound("00-Unidades/Programacion_clases/segundo_parcial/sonido.fondo.mp3")
sonido_fondo.set_volume(0.2)
# sonido incorrecto momentaneo
sonido_incorrecto = pygame.mixer.Sound("00-Unidades/Programacion_clases/segundo_parcial/sonido_incorrecto.mp3")
sonido_incorrecto.set_volume(0.9)
# sonido correcto momentaneo
sonido_correcto = pygame.mixer.Sound("00-Unidades/Programacion_clases/segundo_parcial/sonido_correcto.mp3")
sonido_correcto.set_volume(0.9)

# Creacion de la ventana principal
screen = pygame.display.set_mode([1280, 720])

# Ubicacion y tamaño de rectangulos
# Se le asigna la ubicacion(x, y), el largo y el ancho del rectangulo que vamos a colocar en pantalla
#                            Ubicacion x, y| Largo y ancho
rect_boton_puntuaciones = pygame.Rect(490, 100, 290, 400)

rect_boton_empezar = pygame.Rect(490, 300, 290, 70)
rect_boton_puntaje = pygame.Rect(490, 390, 290, 70)
rect_boton_salir = pygame.Rect(490, 480, 290, 70)

rect_boton_insertar_nombre = pygame.Rect(450, 330, 500, 70)

rect_boton_pregunta = pygame.Rect(490, 10, 290, 70)
rect_boton_reiniciar = pygame.Rect(490, 600, 290, 70)
rect_boton_a = pygame.Rect(136, 492, 200, 50)
rect_boton_b = pygame.Rect(445, 492, 200, 50)
rect_boton_c = pygame.Rect(845, 492, 200, 50)
rect_boton_menu = pygame.Rect(1070, 15, 200, 50)

# Se asigna el tipo de fuente y texto que se utilizara
font = pygame.font.SysFont("8-bit-wonder.TTF", 50)
text_empezar = font.render("Start", True, (0, 0, 0))
text_puntuaciones = font.render("Scores", True, (0, 0, 0))
text_salir = font.render("Salir", True, (0, 0, 0))
text_inicial = font.render("Pregunta", True, (0, 0, 0))
text_puntaje = font.render("Puntaje", True, (0, 0, 0))
text_reiniciar = font.render("Reiniciar", True, (0, 0, 0))
text_menu = font.render("Menu", True, (0, 0, 0))

#  Se guarda la imagen dentro de una variable para luego utilizar esa misma variable para cambiar a un tamaño preferible
imagen = pygame.image.load("C:/Users/User/Downloads/Curso_de_ingreso_PYTHON-main/Curso_de_ingreso_PYTHON-main/00-Unidades/Programacion_clases/segundo_parcial/img.fondo.jpg.gif")
#                ancho | alto
nuevo_tamañoimg = (1280, 720)
imagen_redimensionada = pygame.transform.scale(imagen, nuevo_tamañoimg)

# Se crean variables para luego ser utilizadas dentro del bucle 
running = True
pregunta = -1
puntaje = 0
errores = 0
esta_jugando = False
menu_principal = True
variable_a_incorrecta = 0 
variable_b_incorrecta = 0
variable_c_incorrecta = 0
bandera_correcta = False
bandera_incorrecta = False
bandera_sonido = False
bandera_score = False
lista_diccionario_scores = []
indice = 0
while running:
    # Si la bandera sonido es igual a false entonces se repetira el sonido de fondo de forma indefinida una sola vez hasta que se cierre el juego
    if bandera_sonido == False: 
        sonido_fondo.play(-1)
        bandera_sonido = True
    text_puntaje = font.render(f"Puntaje: {puntaje}", True, (0, 0, 0))
    screen.blit(imagen_redimensionada, (0, 0))
  
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
           running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # print(f"Mouse down: {event.pos}") # Determina la ubicacion del puntero una vez presionado en determinado lugar
            # Colision del boton empezar y las consecuencias de lo que sucedera en caso de que tenga la colision
            if rect_boton_empezar.collidepoint(event.pos):
                menu_principal = False
                nombre = ""
                pregunta = -1
            

            # Si la bandera menu principal es igual a True entonces va haber las siguientes colisiones y sus posibles consecuencias:
            elif menu_principal == True:
                if rect_boton_salir.collidepoint(event.pos):
                    running = False

                elif rect_boton_puntaje.collidepoint(event.pos):
                    menu_principal = False
                    bandera_score = True
                    pregunta = -1

            # Colision del boton pregunta y lo que pasara en caso de que se le haga click
            elif rect_boton_pregunta.collidepoint(event.pos):
                esta_jugando = True
                pregunta +=1
                rect_boton_a = pygame.Rect(136, 492, 200, 50)
                rect_boton_b = pygame.Rect(445, 492, 200, 50)
                rect_boton_c = pygame.Rect(845, 492, 200, 50)
               
                bandera_incorrecta = False
                bandera_correcta = False
                #print("Apreto start")

            # Colision del boton reiniciar y lo que pasara en caso de que se le haga click
            elif rect_boton_reiniciar.collidepoint(event.pos):
                pregunta = -1
                puntaje = 0
                esta_jugando = False
                bandera_correcta = False
            
            # Colision del boton menu que nos trae de vuelta al inicio del juego y lo que pasara en caso de que se le haga click
            elif rect_boton_menu.collidepoint(event.pos):
                menu_principal = True
                pregunta = -1
                puntaje = 0
                bandera_correcta = False
                bandera_score = False
                esta_jugando = False

            # Menu de respuestas 
            elif esta_jugando == True: 
                match pregunta_actual[2][0]:
                    case "a":
                        if rect_boton_a.collidepoint(event.pos):
                            puntaje += 10
                            errores = 0
                            esta_jugando = False
                            bandera_correcta = "a"
                            bandera_sonido = False
                            sonido_correcto.play()
                            # sonido_momentaneo("00-Unidades/Programacion_clases/segundo_parcial/sonido_correcto.mp3")
                        elif rect_boton_b != None and rect_boton_b.collidepoint(event.pos):
                            errores +=1
                            rect_boton_b = None
                            bandera_incorrecta = "b"
                            sonido_incorrecto.play()
                        elif rect_boton_c != None and rect_boton_c.collidepoint(event.pos):
                            errores +=1
                            rect_boton_c = None
                            bandera_incorrecta = "c"
                    case "b":
                        if rect_boton_a != None and rect_boton_a.collidepoint(event.pos):
                            errores +=1
                            rect_boton_a = None
                            
                            bandera_incorrecta = "a"
                        elif rect_boton_b.collidepoint(event.pos):
                            puntaje +=10
                            errores = 0
                            esta_jugando = False
                            bandera_correcta = "b"

                        elif rect_boton_c != None and rect_boton_c.collidepoint(event.pos):
                            errores +=1
                            rect_boton_c = None
                         
                            bandera_incorrecta = "c"
                    case "c":
                        if rect_boton_a != None and rect_boton_a.collidepoint(event.pos):
                            errores +=1
                            rect_boton_a = None

                            bandera_incorrecta = "a"
                        elif rect_boton_b != None and rect_boton_b.collidepoint(event.pos):
                            errores +=1
                            rect_boton_b = None
                            
                            bandera_incorrecta = "b"
                        elif rect_boton_c.collidepoint(event.pos):
                            puntaje +=10
                            errores = 0
                            esta_jugando = False
                            bandera_correcta = "c"
    lista_nueva = guarda_sublistas(lista)
    if errores == 2:
        esta_jugando = False
        errores = 0         

    if pregunta == len(lista_nueva):
        escribiendo = True
        while escribiendo:
            pressed_keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                screen.blit(imagen_redimensionada, (0, 0))
                pygame.draw.rect(screen, (185, 42, 42), rect_boton_insertar_nombre)
                text_insertar_nombre = font.render(f"Inserte nombre: {nombre}", True, (0, 0, 0))
                screen.blit(text_insertar_nombre,(550, 346))
                if event.type == pygame.TEXTINPUT:
                    nombre += event.text
                    

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        nombre = nombre[:-1]


                if True in pressed_keys:
                    if pressed_keys[K_RETURN]:
                        scores = ({"nombre":nombre, "puntaje":puntaje})
                        lista_diccionario_scores.append(scores)
                        escribiendo = False
                        menu_principal = True
                        esta_jugando = True
                        pregunta = 0
                        puntaje = 0
                guardar_datajson(lista_diccionario_scores)
                pygame.display.flip()


    # Menu principal 
    # Sale en cuanto inicializas con el juego.
    elif menu_principal == True:
        pygame.draw.rect(screen, (185, 42, 42), rect_boton_empezar)
        pygame.draw.rect(screen, (185, 42, 42), rect_boton_puntaje)
        pygame.draw.rect(screen, (185, 42, 42), rect_boton_salir)
        screen.blit(text_empezar,(590, 316))
        screen.blit(text_puntuaciones,(576, 406))
        screen.blit(text_salir,(590, 500))
    # Se encarga de comparar scores de mayor a menor y guardar los nombresbb
    elif bandera_score == True:
        if len(lista_diccionario_scores) > 0:
            pygame.draw.rect(screen, (185, 42, 42), rect_boton_puntuaciones)
            ordenar_mayor_menor(lista_diccionario_scores)
            txt_puntaje_1 = font.render(f"{lista_diccionario_scores[0]["nombre"]}: {lista_diccionario_scores[0]["puntaje"]}", True, (0, 0, 0))
            screen.blit(txt_puntaje_1,(560, 100))
            if len(lista_diccionario_scores) > 1:
                txt_puntaje_2 = font.render(f"{lista_diccionario_scores[1]["nombre"]}: {lista_diccionario_scores[1]["puntaje"]}", True, (0, 0, 0))
                screen.blit(txt_puntaje_2,(560, 200))
                if len(lista_diccionario_scores) > 2:
                    txt_puntaje_3 = font.render(f"{lista_diccionario_scores[2]["nombre"]}: {lista_diccionario_scores[2]["puntaje"]}", True, (0, 0, 0))
                    screen.blit(txt_puntaje_3,(560, 300))
        pygame.draw.rect(screen,(185, 42, 42), rect_boton_menu)
        screen.blit(text_menu,(1127, 25))


    else:
        if esta_jugando == True:
            text_puntaje = font.render(f"Puntaje: {puntaje}", True, (0, 0, 0))
            screen.blit(imagen_redimensionada, (0, 0))
            pygame.draw.rect(screen,(185, 42, 42), rect_boton_pregunta)
            pygame.draw.rect(screen,(185, 42, 42), rect_boton_reiniciar)
            pygame.draw.rect(screen,(185, 42, 42), rect_boton_menu)
            screen.blit(text_menu,(1127, 25))
            screen.blit(text_puntaje,(565, 220))
            screen.blit(text_inicial,(560, 26))
            screen.blit(text_reiniciar,(560, 620))
            pregunta_actual = lista_nueva[pregunta]
            text_pregunta = font.render(pregunta_actual[0][0], True, (0,0,0))
            screen.blit(text_pregunta,(250, 140))
            # Aparece en cuanto inicializas con el juego al tener colision con el rectangulo "Pregunta"
            if bandera_incorrecta == False:
                pygame.draw.rect(screen,(185, 42, 42), rect_boton_a)
                pygame.draw.rect(screen,(185, 42, 42), rect_boton_b)
                pygame.draw.rect(screen,(185, 42, 42), rect_boton_c)
                text_respuesta_a = font.render(pregunta_actual[1][0][0], True, (0,0,0))
                text_respuesta_b = font.render(pregunta_actual[1][0][1], True, (0,0,0))
                text_respuesta_c = font.render(pregunta_actual[1][0][2], True, (0,0,0))
                screen.blit(text_respuesta_a,(150, 500))
                screen.blit(text_respuesta_b,(450, 500))
                screen.blit(text_respuesta_c,(850, 500))
            
        #   Bandera de verificacion de opcion incorrecta
        #   Se usa una bandera para que en caso de que se elija una opcion incorrecta, solo se muestren dos opciones, la correcta e incorrecta y se borre la opcion incorrecta que seleccionaste
            elif bandera_incorrecta != False:
                match bandera_incorrecta:
                    case "a":
                        pygame.draw.rect(screen,(185, 42, 42), rect_boton_b)
                        pygame.draw.rect(screen,(185, 42, 42), rect_boton_c)
                        text_respuesta_c = font.render(pregunta_actual[1][0][2], True, (0,0,0))
                        text_respuesta_b = font.render(pregunta_actual[1][0][1], True, (0,0,0))
                        screen.blit(text_respuesta_b,(450, 500))
                        screen.blit(text_respuesta_c,(850, 500))
                    case "b":
                        pygame.draw.rect(screen,(185, 42, 42), rect_boton_a)
                        pygame.draw.rect(screen,(185, 42, 42), rect_boton_c)
                        text_respuesta_a = font.render(pregunta_actual[1][0][0], True, (0,0,0))
                        text_respuesta_c = font.render(pregunta_actual[1][0][2], True, (0,0,0))
                        screen.blit(text_respuesta_a,(150, 500))
                        screen.blit(text_respuesta_c,(850, 500))
                    case "c":
                        pygame.draw.rect(screen,(185, 42, 42), rect_boton_a)
                        pygame.draw.rect(screen,(185, 42, 42), rect_boton_b)
                        text_respuesta_a = font.render(pregunta_actual[1][0][0], True, (0,0,0))
                        text_respuesta_b = font.render(pregunta_actual[1][0][1], True, (0,0,0)) 
                        screen.blit(text_respuesta_a,(150, 500))
                        screen.blit(text_respuesta_b,(450, 500))

        # Este es el submenu que aparece en cuanto clickeas la opcion de "Start"
        else:
            pygame.draw.rect(screen,(185, 42, 42), rect_boton_pregunta)
            pygame.draw.rect(screen,(185, 42, 42), rect_boton_reiniciar)
            pygame.draw.rect(screen,(185, 42, 42), rect_boton_menu)
            screen.blit(text_menu,(1127, 25))
            screen.blit(text_puntaje,(565, 220))
            screen.blit(text_inicial,(560, 26))
            screen.blit(text_reiniciar,(560, 620))
            # Bandera_correcta verifica si la opcion es correcta, y si lo es, entonces se borraran las dos opciones incorrecta y solo se dejara a plena vista la opcion incorrecta.
            match bandera_correcta:
                case "a":
                    pygame.draw.rect(screen,(185, 42, 42), rect_boton_a)
                    text_respuesta_a = font.render(pregunta_actual[1][0][0], True, (0,0,0))
                    screen.blit(text_respuesta_a,(150, 500))
                case "b":
                    pygame.draw.rect(screen,(185, 42, 42), rect_boton_b)
                    text_respuesta_b = font.render(pregunta_actual[1][0][1], True, (0,0,0))
                    screen.blit(text_respuesta_b,(450, 500))
                case "c":
                    pygame.draw.rect(screen,(185, 42, 42), rect_boton_c)
                    text_respuesta_c = font.render(pregunta_actual[1][0][2], True, (0,0,0))
                    screen.blit(text_respuesta_c,(850, 500))
    
    pygame.display.flip()

pygame.quit()
