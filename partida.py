"""Reglas, puntaje y lista de señales de una partida."""

import random
import pygame
import ajustes
import nota


def crear_partida(cancion=0):
    """Devuelve una partida nueva con la lista y los contadores vacíos."""
    return {"notas": [], "pasos": 0, "errores": 0, "puntos": 0,
            "cancion": cancion, "indice_ritmo": 0, "proximo_pulso": ajustes.PRIMER_PULSO,
            "mensaje": "SEGUÍ EL BEAT", "aviso": 0}


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


def registrar_paso(datos, tecla, tiempo):
    """Evalúa una pulsación y devuelve acierto, error o un texto vacío."""
    columna = obtener_columna(tecla)
    if columna == -1:
        return ""
    for senal in datos["notas"]:
        senal.mover(tiempo)
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
    if datos["errores"] >= ajustes.LIMITES_ERRORES[datos["cancion"]]:
        return "derrota"
    if datos["pasos"] >= ajustes.METAS_PASOS[datos["cancion"]]:
        return "victoria"
    return "jugando"


def obtener_nivel(datos):
    """Devuelve el nivel de la canción elegida, de 1 a 5."""
    return datos["cancion"] + 1


def actualizar(datos, tiempo):
    """Programa señales sobre los pulsos musicales y cuenta las perdidas."""
    nivel = obtener_nivel(datos) - 1
    bpm = ajustes.CANCIONES[datos["cancion"]]["bpm"]
    pulso_ms = 60000 / bpm
    duracion = pulso_ms * ajustes.PULSOS_ANTICIPACION[nivel]
    llegada = datos["proximo_pulso"] * pulso_ms
    # Las llegadas siempre caen en pulsos o medios pulsos de la canción.
    while tiempo >= llegada - duracion:
        datos["notas"].append(nota.Nota(random.randint(0, 3), llegada, duracion))
        ritmo = ajustes.PULSOS_ENTRE_NOTAS[nivel]
        intervalo = ritmo[datos["indice_ritmo"] % len(ritmo)]
        datos["proximo_pulso"] = datos["proximo_pulso"] + intervalo
        datos["indice_ritmo"] = datos["indice_ritmo"] + 1
        llegada = datos["proximo_pulso"] * pulso_ms
    # Cada señal conserva la duración con la que fue creada.
    if datos["aviso"] > 0:
        datos["aviso"] = datos["aviso"] - 1
    else:
        datos["mensaje"] = "SEGUÍ EL BEAT"
    # Recorremos una copia para poder quitar elementos de la lista original.
    for senal in datos["notas"][:]:
        senal.mover(tiempo)
        if senal.y > ajustes.LINEA_ACIERTO_Y + ajustes.MARGEN_ACIERTO:
            datos["notas"].remove(senal)
            datos["errores"] = datos["errores"] + 1
            datos["mensaje"] = "SE PASÓ UNA SEÑAL"
            datos["aviso"] = ajustes.DURACION_MENSAJE
