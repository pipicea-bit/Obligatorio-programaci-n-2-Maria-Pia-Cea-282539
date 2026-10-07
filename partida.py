"""Reglas, puntaje y lista de señales de una partida."""

import random
import pygame
import ajustes
import nota


def crear_partida():
    """Devuelve una partida nueva con la lista y los contadores vacíos."""
    return {"notas": [], "pasos": 0, "errores": 0, "puntos": 0,
            "cuadros": 0, "mensaje": "SEGUÍ EL BEAT", "aviso": 0}


def obtener_columna(tecla):
    """Devuelve la columna de una flecha o -1 si es otra tecla."""
    teclas = [pygame.K_LEFT, pygame.K_DOWN, pygame.K_UP, pygame.K_RIGHT]
    for columna in range(len(teclas)):
        if tecla == teclas[columna]:
            return columna
    return -1


def buscar_acierto(notas, columna):
    """Devuelve una señal acertable de esa columna o None si no hay ninguna."""
    for senal in notas:
        if senal.columna == columna:
            if abs(senal.y - ajustes.LINEA_ACIERTO_Y) <= ajustes.MARGEN_ACIERTO:
                return senal
    return None


def registrar_paso(datos, tecla):
    """Evalúa una pulsación y devuelve acierto, error o un texto vacío."""
    columna = obtener_columna(tecla)
    if columna == -1:
        return ""
    senal = buscar_acierto(datos["notas"], columna)
    if senal is not None:
        datos["notas"].remove(senal)
        datos["pasos"] = datos["pasos"] + 1
        datos["puntos"] = datos["puntos"] + ajustes.PUNTOS_ACIERTO
        datos["mensaje"] = "¡BUEN PASO!"
        resultado = "acierto"
    else:
        datos["errores"] = datos["errores"] + 1
        datos["mensaje"] = "FUERA DE TIEMPO"
        resultado = "error"
    datos["aviso"] = ajustes.DURACION_MENSAJE
    return resultado


def obtener_estado(datos):
    """Devuelve victoria, derrota o jugando según los contadores."""
    if datos["errores"] >= ajustes.MAX_ERRORES:
        return "derrota"
    if datos["pasos"] >= ajustes.META_PASOS:
        return "victoria"
    return "jugando"


def obtener_nivel(datos):
    """Devuelve un nivel de 1 a 4, aumentando cada cinco pasos acertados."""
    nivel = datos["pasos"] // ajustes.PASOS_POR_NIVEL + 1
    if nivel > len(ajustes.VELOCIDADES_NIVELES):
        nivel = len(ajustes.VELOCIDADES_NIVELES)
    return nivel


def actualizar(datos):
    """Mueve señales, agrega nuevas y cuenta las que se pasan de la línea."""
    datos["cuadros"] = datos["cuadros"] + 1
    nivel = obtener_nivel(datos) - 1
    if datos["cuadros"] >= ajustes.INTERVALOS_NIVELES[nivel]:
        velocidad = ajustes.VELOCIDADES_NIVELES[nivel]
        datos["notas"].append(nota.Nota(random.randint(0, 3), velocidad))
        datos["cuadros"] = 0
    # Las señales existentes conservan su velocidad: no aceleran de golpe.
    if datos["aviso"] > 0:
        datos["aviso"] = datos["aviso"] - 1
    else:
        datos["mensaje"] = "SEGUÍ EL BEAT"
    # Recorremos una copia para poder quitar elementos de la lista original.
    for senal in datos["notas"][:]:
        senal.mover()
        if senal.y > ajustes.LINEA_ACIERTO_Y + ajustes.MARGEN_ACIERTO:
            datos["notas"].remove(senal)
            datos["errores"] = datos["errores"] + 1
            datos["mensaje"] = "SE PASÓ UNA SEÑAL"
            datos["aviso"] = ajustes.DURACION_MENSAJE
