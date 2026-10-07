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
    }
    for efecto in efectos.values():
        efecto.set_volume(ajustes.VOLUMEN_EFECTOS)
    canciones = []
    for datos in ajustes.CANCIONES:
        sonido = pygame.mixer.Sound(os.path.join(carpeta, datos["archivo"]))
        sonido.set_volume(ajustes.VOLUMEN_MUSICA)
        canciones.append(sonido)
    # El canal 0 queda reservado para que un efecto no corte la música.
    pygame.mixer.set_reserved(1)
    return efectos, canciones


def reproducir(canciones, seleccion):
    """Reinicia la canción elegida y devuelve el instante de inicio."""
    pygame.mixer.Channel(0).play(canciones[seleccion], loops=-1)
    return pygame.time.get_ticks()


def detener():
    """Detiene la canción al terminar o volver a personalizar."""
    pygame.mixer.Channel(0).stop()
