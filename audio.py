"""Carga única de sonidos y reproducción de las pistas originales."""

import os
import pygame
import ajustes


def cargar_audio():
    """Devuelve los efectos y las cinco canciones cargados antes del bucle."""
    carpeta = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")
    efectos = {
        "acierto": pygame.mixer.Sound(os.path.join(carpeta, "acierto.wav")),
        "error": pygame.mixer.Sound(os.path.join(carpeta, "error.wav")),
        "victoria": pygame.mixer.Sound(os.path.join(carpeta, "victoria.wav")),
        "derrota": pygame.mixer.Sound(os.path.join(carpeta, "derrota.wav")),
    }
    for efecto in efectos.values():
        efecto.set_volume(ajustes.VOLUMEN_EFECTOS)
    canciones = []
    for datos in ajustes.CANCIONES:
        sonido = pygame.mixer.Sound(os.path.join(carpeta, datos["archivo"]))
        sonido.set_volume(ajustes.VOLUMEN_MUSICA)
        canciones.append(sonido)
    # Canal 0: música. Canal 1: resultado. Los otros reproducen los pasos.
    pygame.mixer.set_reserved(2)
    return efectos, canciones


def reproducir(canciones, seleccion):
    """Reinicia la canción elegida y devuelve el instante de inicio."""
    pygame.mixer.Channel(1).stop()
    pygame.mixer.Channel(0).play(canciones[seleccion], loops=-1)
    return pygame.time.get_ticks()


def detener():
    """Detiene la canción al terminar o volver a personalizar."""
    pygame.mixer.Channel(0).stop()


def reproducir_resultado(efectos, estado):
    """Reproduce una melodía de festejo o tristeza al aparecer el resultado."""
    if estado == "victoria" or estado == "derrota":
        pygame.mixer.Channel(1).play(efectos[estado])
