"""Sesión de juego y comparación de los turnos del duelo."""

import random
import pygame
import partida


def crear_sesion(modo, personaje):
    """Devuelve una sesión vacía y una secuencia compartida para el duelo."""
    secuencia = []
    if modo == "1vs1":
        for _ in range(512):
            secuencia.append(random.randint(0, 3))
    return {"modo": modo, "personajes": [personaje], "rondas": [],
            "resultados": [], "secuencia": secuencia}


def nueva_ronda(sesion, cancion):
    """Crea dos rondas independientes con la misma secuencia en el duelo."""
    sesion["resultados"] = []
    sesion["rondas"] = []
    cantidad = 1
    if sesion["modo"] == "1vs1":
        cantidad = 2
    for _ in range(cantidad):
        sesion["rondas"].append(partida.crear_partida(cancion, sesion["modo"], sesion["secuencia"]))
    return sesion["rondas"][0]


def registrar_duelo(sesion, tecla, tiempo):
    """Dirige las flechas al jugador 1 y WASD al jugador 2."""
    flechas = [pygame.K_LEFT, pygame.K_DOWN, pygame.K_UP, pygame.K_RIGHT]
    letras = [pygame.K_a, pygame.K_s, pygame.K_w, pygame.K_d]
    for jugador in range(2):
        teclas = flechas
        if jugador == 1:
            teclas = letras
        for columna in range(4):
            if tecla == teclas[columna]:
                datos = sesion["rondas"][jugador]
                if partida.obtener_estado(datos) == "jugando":
                    sesion["personajes"][jugador].bailar(columna)
                    return partida.registrar_paso(datos, flechas[columna], tiempo)
    return ""


def actualizar_duelo(sesion, tiempo):
    """Actualiza las dos pistas y devuelve el final cuando ambas terminaron."""
    terminados = 0
    for datos in sesion["rondas"]:
        if partida.obtener_estado(datos) == "jugando":
            partida.actualizar(datos, tiempo)
        if partida.obtener_estado(datos) != "jugando":
            terminados = terminados + 1
    if terminados == 2:
        sesion["resultados"] = []
        for datos in sesion["rondas"]:
            sesion["resultados"].append({"puntos": datos["puntos"], "errores": datos["errores"]})
        return "resultado_duelo"
    return "jugando"


def ganador(sesion):
    """Devuelve el nombre del ganador, desempatando por menor cantidad de errores."""
    a = sesion["resultados"][0]
    b = sesion["resultados"][1]
    if a["puntos"] > b["puntos"] or (a["puntos"] == b["puntos"] and a["errores"] < b["errores"]):
        return sesion["personajes"][0].nombre
    if b["puntos"] > a["puntos"] or (a["puntos"] == b["puntos"] and b["errores"] < a["errores"]):
        return sesion["personajes"][1].nombre
    return "EMPATE"
