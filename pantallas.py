"""Dibujo de la personalización, la pista y los resultados."""

import pygame
import ajustes
import nota
import partida
import modos


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


def personalizacion(pantalla, fuentes, personaje, nombre_confirmado, editando_nombre, campo_nombre, rival=False):
    """Muestra los controles de apariencia y el campo de nombre."""
    dibujar_escenario(pantalla)
    encabezado = "URBAN DANCE ARCADE"
    if rival:
        encabezado = "PERSONALIZÁ AL JUGADOR 2"
    dibujar_texto(pantalla, fuentes["chica"], encabezado, ajustes.MENTA, 40, 25)
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
    dibujar_texto(pantalla, fuentes["chica"], "ESPACIO: ELEGIR MODO", ajustes.MENTA, 50, 520)


def juego(pantalla, fuentes, personaje, datos, estado):
    """Muestra la pista durante la partida o las instrucciones para reiniciar."""
    dibujar_escenario(pantalla)
    dibujar_texto(pantalla, fuentes["texto"], "GROOVING", ajustes.AMARILLO, 40, 25)
    dibujar_texto(pantalla, fuentes["chica"], datos["modo"].upper(), ajustes.LILA, 550, 25)
    dibujar_texto(pantalla, fuentes["texto"], f"PUNTOS {datos['puntos']}", ajustes.BLANCO, 250, 25)
    meta = str(ajustes.METAS_PASOS[datos["cancion"]])
    if datos["modo"] == "survival":
        meta = "SIN FIN"
    contador = f"PASOS {datos['pasos']}/{meta}  ERRORES {datos['errores']}/{ajustes.LIMITES_ERRORES[datos['cancion']]}"
    dibujar_texto(pantalla, fuentes["chica"], contador, ajustes.ROSA, 40, 65)
    if datos["modo"] == "survival":
        segundos = int(datos["tiempo"] / 1000)
        dibujar_texto(pantalla, fuentes["chica"], f"TIEMPO: {segundos} S", ajustes.BLANCO, 550, 110)
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
        dibujar_texto(pantalla, fuentes["chica"], "M: ELEGIR MODO", ajustes.LILA, 70, 445)
    cancion = ajustes.CANCIONES[datos["cancion"]]
    dibujar_texto(pantalla, fuentes["chica"], cancion["nombre"], ajustes.MENTA, 550, 520)
    dibujar_texto(pantalla, fuentes["chica"], "ESC: SALIR", ajustes.BLANCO, 40, 560)


def elegir_cancion(pantalla, fuentes, personaje, seleccion, modo="solo"):
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
    if modo == "survival":
        limites = f"SIN META / ERRORES {ajustes.LIMITES_ERRORES[seleccion]}"
    dibujar_texto(pantalla, fuentes["chica"], limites, ajustes.MENTA, 50, 485)
    dibujar_texto(pantalla, fuentes["chica"], personaje.nombre, ajustes.AMARILLO, 545, 170)
    personaje.dibujar(pantalla)
    dibujar_texto(pantalla, fuentes["chica"], "IZQUIERDA / DERECHA: ESCUCHAR", ajustes.BLANCO, 50, 505)
    dibujar_texto(pantalla, fuentes["texto"], "ENTER: EMPEZAR", ajustes.MENTA, 50, 535)
    dibujar_texto(pantalla, fuentes["chica"], "P: PERSONALIZAR / ESC: SALIR", ajustes.BLANCO, 50, 570)


def elegir_modo(pantalla, fuentes, personaje, seleccion):
    """Muestra los tres modos después de personalizar el personaje."""
    dibujar_escenario(pantalla)
    dibujar_texto(pantalla, fuentes["titulo"], "GROOVING", ajustes.AMARILLO, 40, 53)
    dibujar_texto(pantalla, fuentes["texto"], "ELEGÍ EL MODO", ajustes.MENTA, 50, 175)
    nombres = ["SOLO", "1VS1", "SURVIVAL"]
    detalles = ["ALCANZÁ LA META DEL NIVEL", "FLECHAS VS WASD / A LA VEZ", "RESISTÍ HASTA AGOTAR ERRORES"]
    for i in range(3):
        color = ajustes.BLANCO
        marca = "  "
        if i == seleccion:
            color = ajustes.AMARILLO
            marca = "> "
        y = 240 + i * 85
        dibujar_texto(pantalla, fuentes["texto"], marca + nombres[i], color, 50, y)
        dibujar_texto(pantalla, fuentes["chica"], detalles[i], ajustes.LILA, 75, y + 30)
    dibujar_texto(pantalla, fuentes["chica"], personaje.nombre, ajustes.AMARILLO, 545, 170)
    personaje.dibujar(pantalla)
    dibujar_texto(pantalla, fuentes["chica"], "ARRIBA / ABAJO: ELEGIR", ajustes.BLANCO, 50, 510)
    dibujar_texto(pantalla, fuentes["texto"], "ENTER: CONTINUAR", ajustes.MENTA, 50, 540)
    dibujar_texto(pantalla, fuentes["chica"], "P: PERSONALIZAR / ESC: SALIR", ajustes.BLANCO, 50, 575)


def duelo(pantalla, fuentes, sesion, estado):
    """Muestra el cambio de turno o el marcador final de dos jugadores."""
    dibujar_escenario(pantalla)
    dibujar_texto(pantalla, fuentes["titulo"], "GROOVING", ajustes.AMARILLO, 40, 53)
    dibujar_texto(pantalla, fuentes["texto"], "DUELO 1VS1", ajustes.MENTA, 50, 180)
    nombre = modos.ganador(sesion)
    dibujar_texto(pantalla, fuentes["texto"], "RESULTADO DEL DUELO", ajustes.AMARILLO, 50, 240)
    anuncio = "GANADOR: " + nombre
    if nombre == "EMPATE":
        anuncio = "¡EMPATE!"
    dibujar_texto(pantalla, fuentes["chica"], anuncio, ajustes.MENTA, 50, 280)
    if nombre == "EMPATE":
        dibujar_texto(pantalla, fuentes["chica"], "MISMO PUNTAJE Y ERRORES", ajustes.BLANCO, 50, 310)
    for i in range(2):
        resultado = sesion["resultados"][i]
        nombre = sesion["personajes"][i].nombre
        dibujar_texto(pantalla, fuentes["chica"], nombre, ajustes.AMARILLO, 50, 340 + i * 55)
        texto = f"{resultado['puntos']} PUNTOS / {resultado['errores']} ERRORES"
        dibujar_texto(pantalla, fuentes["chica"], texto, ajustes.BLANCO, 50, 365 + i * 55)
    sesion["personajes"][0].dibujar(pantalla)
    dibujar_texto(pantalla, fuentes["chica"], "ENTER: REVANCHA / C: NIVEL", ajustes.MENTA, 50, 480)
    dibujar_texto(pantalla, fuentes["chica"], "M: MODO / P: PERSONAJE / ESC: SALIR", ajustes.BLANCO, 50, 550)


def duelo_simultaneo(pantalla, fuentes, sesion):
    """Dibuja dos pistas lado a lado con sus personajes y marcadores."""
    for i in range(2):
        panel = pantalla.subsurface((i * ajustes.ANCHO, 0, ajustes.ANCHO, ajustes.ALTO))
        datos = sesion["rondas"][i]
        estado_ronda = partida.obtener_estado(datos)
        juego(panel, fuentes, sesion["personajes"][i], datos, "jugando")
        pygame.draw.rect(panel, ajustes.FONDO, (0, 500, ajustes.ANCHO, 100))
        controles = "JUGADOR 1: FLECHAS"
        if i == 1:
            controles = "JUGADOR 2: A / S / W / D"
        dibujar_texto(panel, fuentes["texto"], controles, ajustes.AMARILLO, 40, 525)
        if estado_ronda != "jugando":
            aviso = "META COMPLETA / ESPERANDO RIVAL"
            if estado_ronda == "derrota":
                aviso = "SIN VIDAS / ESPERANDO RIVAL"
            dibujar_texto(panel, fuentes["chica"], aviso, ajustes.ROSA, 40, 560)
        else:
            dibujar_texto(panel, fuentes["chica"], "ESC: SALIR", ajustes.BLANCO, 40, 560)
