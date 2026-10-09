"""Dibujo de la personalización, la pista y los resultados."""

import pygame
import ajustes
import nota
import partida


def dibujar_texto(pantalla, fuente, texto, color, x, y):
    """Convierte un texto en una imagen y lo muestra en pantalla."""
    imagen = fuente.render(texto, False, color)
    pantalla.blit(imagen, (x, y))


def dibujar_escenario(pantalla):
    """Dibuja una pared de ladrillos y un piso de arcade con figuras simples."""
    pantalla.fill(ajustes.FONDO)
    pygame.draw.rect(pantalla, ajustes.PARED, (460, 150, 310, 330))
    for y in range(150, ajustes.PISO_Y, ajustes.ALTO_LADRILLO):
        pygame.draw.line(pantalla, ajustes.LADRILLO, (460, y), (770, y), ajustes.GROSOR_LINEA)
        for x in range(460, 771, ajustes.ANCHO_LADRILLO):
            pygame.draw.line(pantalla, ajustes.LADRILLO, (x, y),
                             (x, y + ajustes.ALTO_LADRILLO), ajustes.GROSOR_LINEA)
    pygame.draw.rect(pantalla, ajustes.PISO, (0, ajustes.PISO_Y, ajustes.ANCHO, 120))
    for x in range(0, ajustes.ANCHO, ajustes.ANCHO_LADRILLO):
        pygame.draw.line(pantalla, ajustes.LINEA_PISO, (400, ajustes.PISO_Y),
                         (x, ajustes.ALTO), ajustes.GROSOR_LINEA)
    for y in range(ajustes.PISO_Y, ajustes.ALTO, ajustes.ALTO_LADRILLO):
        pygame.draw.line(pantalla, ajustes.LINEA_PISO, (0, y),
                         (ajustes.ANCHO, y), ajustes.GROSOR_LINEA)
    pygame.draw.line(pantalla, ajustes.ROSA, (40, 152), (760, 152), ajustes.GROSOR_LINEA)


def personalizacion(pantalla, fuentes, personaje, nombre_confirmado, editando_nombre, campo_nombre):
    """Muestra los controles de apariencia y el campo de nombre."""
    dibujar_escenario(pantalla)
    dibujar_texto(pantalla, fuentes["chica"], "1 PLAYER  /  URBAN DANCE ARCADE", ajustes.MENTA, 40, 25)
    dibujar_texto(pantalla, fuentes["titulo"], "GROOVING", ajustes.CONTORNO, 44, 57)
    dibujar_texto(pantalla, fuentes["titulo"], "GROOVING", ajustes.AMARILLO, 40, 53)
    dibujar_texto(pantalla, fuentes["chica"], "TU ESTILO. TU RITMO.", ajustes.ROSA, 43, 130)
    dibujar_texto(pantalla, fuentes["texto"], "ELEGÍ TU ESTILO", ajustes.BLANCO, 50, 180)
    dibujar_texto(pantalla, fuentes["texto"], "1  REMERA + GORRA", ajustes.LILA, 50, 225)
    dibujar_texto(pantalla, fuentes["texto"], "2  PANTALÓN", ajustes.MENTA, 50, 260)
    dibujar_texto(pantalla, fuentes["texto"], "3  PELO", ajustes.ROSA, 50, 295)
    dibujar_texto(pantalla, fuentes["texto"], "4  BAILARINA / BAILARÍN", ajustes.AMARILLO, 50, 330)
    dibujar_texto(pantalla, fuentes["texto"], "5  ACCESORIOS", ajustes.MENTA, 50, 365)
    dibujar_texto(pantalla, fuentes["chica"], ajustes.ACCESORIOS[personaje.accesorio], ajustes.BLANCO, 85, 395)
    dibujar_texto(pantalla, fuentes["chica"], "NOMBRE", ajustes.ROSA, 50, 425)
    pygame.draw.rect(pantalla, ajustes.CONTORNO, campo_nombre)
    borde = ajustes.ROSA
    texto_nombre = personaje.nombre
    if editando_nombre:
        borde = ajustes.MENTA
        texto_nombre = texto_nombre + "_"
    pygame.draw.rect(pantalla, borde, campo_nombre, ajustes.GROSOR_LINEA)
    dibujar_texto(pantalla, fuentes["chica"], texto_nombre, ajustes.BLANCO, 60, 455)
    dibujar_texto(pantalla, fuentes["chica"], "ENTER: CONFIRMAR / CLIC: EDITAR", ajustes.BLANCO, 50, 490)
    dibujar_texto(pantalla, fuentes["chica"], nombre_confirmado, ajustes.AMARILLO, 545, 170)
    personaje.dibujar(pantalla)
    dibujar_texto(pantalla, fuentes["chica"], "PERSONALIZACIÓN  /  ESC: SALIR", ajustes.BLANCO, 50, 552)
    dibujar_texto(pantalla, fuentes["chica"], "ESPACIO: ELEGIR NIVEL", ajustes.MENTA, 50, 520)


def juego(pantalla, fuentes, personaje, datos, estado):
    """Muestra la pista durante la partida o las instrucciones para reiniciar."""
    dibujar_escenario(pantalla)
    dibujar_texto(pantalla, fuentes["texto"], "GROOVING", ajustes.AMARILLO, 40, 25)
    dibujar_texto(pantalla, fuentes["texto"], f"PUNTOS {datos['puntos']}", ajustes.BLANCO, 250, 25)
    dibujar_texto(pantalla, fuentes["chica"], f"PASOS {datos['pasos']}/{ajustes.METAS_PASOS[datos['cancion']]}   ERRORES {datos['errores']}/{ajustes.LIMITES_ERRORES[datos['cancion']]}", ajustes.ROSA, 40, 65)
    dibujar_texto(pantalla, fuentes["chica"], ajustes.CANCIONES[datos["cancion"]]["nivel"], ajustes.MENTA, 550, 65)
    dibujar_texto(pantalla, fuentes["chica"], personaje.nombre, ajustes.AMARILLO, 545, 170)
    personaje.dibujar(pantalla)
    if estado == "jugando":
        for columna in range(len(ajustes.COLUMNAS)):
            x = ajustes.COLUMNAS[columna]
            pygame.draw.line(pantalla, ajustes.LADRILLO, (x, ajustes.NOTA_INICIO_Y), (x, ajustes.PISO_Y), ajustes.GROSOR_LINEA)
            pygame.draw.rect(pantalla, ajustes.SOMBRA_ROPA, (x - 30, ajustes.LINEA_ACIERTO_Y - ajustes.MARGEN_ACIERTO, 60, ajustes.MARGEN_ACIERTO * 2))
            nota.dibujar_flecha(pantalla, columna, ajustes.LINEA_ACIERTO_Y, ajustes.BLANCO)
        for senal in datos["notas"]:
            senal.dibujar(pantalla)
        dibujar_texto(pantalla, fuentes["texto"], datos["mensaje"], ajustes.MENTA, 40, 110)
        dibujar_texto(pantalla, fuentes["chica"], "FLECHAS: ACERTAR EN LA ZONA CLARA", ajustes.BLANCO, 40, 520)
    else:
        mensaje = "¡GANASTE!"
        if estado == "derrota":
            mensaje = "¡PERDISTE!"
        dibujar_texto(pantalla, fuentes["texto"], mensaje, ajustes.AMARILLO, 70, 260)
        dibujar_texto(pantalla, fuentes["chica"], "ENTER: VOLVER A JUGAR", ajustes.MENTA, 70, 325)
        dibujar_texto(pantalla, fuentes["chica"], "C: CAMBIAR NIVEL", ajustes.ROSA, 70, 365)
        dibujar_texto(pantalla, fuentes["chica"], "P: CAMBIAR PERSONAJE", ajustes.BLANCO, 70, 405)
    cancion = ajustes.CANCIONES[datos["cancion"]]
    dibujar_texto(pantalla, fuentes["chica"], cancion["nombre"], ajustes.MENTA, 550, 520)
    dibujar_texto(pantalla, fuentes["chica"], "ESC: SALIR", ajustes.BLANCO, 40, 560)


def elegir_cancion(pantalla, fuentes, personaje, seleccion):
    """Muestra las cinco pistas y los controles para escucharlas y elegir."""
    dibujar_escenario(pantalla)
    dibujar_texto(pantalla, fuentes["titulo"], "GROOVING", ajustes.AMARILLO, 40, 53)
    dibujar_texto(pantalla, fuentes["texto"], "ELEGÍ CANCIÓN / NIVEL", ajustes.MENTA, 50, 165)
    for i in range(len(ajustes.CANCIONES)):
        datos = ajustes.CANCIONES[i]
        y = 210 + i * 55
        color = ajustes.BLANCO
        marca = "  "
        if i == seleccion:
            color = ajustes.AMARILLO
            marca = "> "
        dibujar_texto(pantalla, fuentes["texto"], marca + datos["nivel"], color, 50, y)
        dibujar_texto(pantalla, fuentes["chica"], f"{datos['nombre']} / {datos['bpm']} BPM", ajustes.LILA, 75, y + 25)
    limites = f"META {ajustes.METAS_PASOS[seleccion]} / ERRORES {ajustes.LIMITES_ERRORES[seleccion]}"
    dibujar_texto(pantalla, fuentes["chica"], limites, ajustes.MENTA, 50, 485)
    dibujar_texto(pantalla, fuentes["chica"], personaje.nombre, ajustes.AMARILLO, 545, 170)
    personaje.dibujar(pantalla)
    dibujar_texto(pantalla, fuentes["chica"], "IZQUIERDA / DERECHA: ESCUCHAR", ajustes.BLANCO, 50, 505)
    dibujar_texto(pantalla, fuentes["texto"], "ENTER: EMPEZAR", ajustes.MENTA, 50, 535)
    dibujar_texto(pantalla, fuentes["chica"], "P: PERSONALIZAR / ESC: SALIR", ajustes.BLANCO, 50, 570)
