"""Señales de baile que bajan por las cuatro columnas."""

import pygame
import ajustes


def dibujar_flecha(pantalla, columna, y, color):
    """Dibuja una flecha usando líneas, sin depender de símbolos de una fuente."""
    x = ajustes.COLUMNAS[columna]
    # Cada lista tiene el inicio, la punta y los extremos de la flecha.
    formas = [
        [(x + 12, y), (x - 12, y), (x, y - 12), (x, y + 12)],
        [(x, y - 12), (x, y + 12), (x - 12, y), (x + 12, y)],
        [(x, y + 12), (x, y - 12), (x - 12, y), (x + 12, y)],
        [(x - 12, y), (x + 12, y), (x, y - 12), (x, y + 12)],
    ]
    puntos = formas[columna]
    pygame.draw.line(pantalla, color, puntos[0], puntos[1], ajustes.GROSOR_FLECHA)
    pygame.draw.line(pantalla, color, puntos[1], puntos[2], ajustes.GROSOR_FLECHA)
    pygame.draw.line(pantalla, color, puntos[1], puntos[3], ajustes.GROSOR_FLECHA)


class Nota:
    """Guarda la columna y la altura de una señal de ritmo."""

    def __init__(self, columna, velocidad=ajustes.VELOCIDAD_NOTA):
        """Crea una señal en la parte superior de su columna."""
        self.velocidad = velocidad
        self.columna = columna
        self.y = ajustes.NOTA_INICIO_Y

    def mover(self):
        """Hace bajar la señal en cada cuadro."""
        self.y = self.y + self.velocidad

    def dibujar(self, pantalla):
        """Dibuja una flecha del color de su columna."""
        dibujar_flecha(pantalla, self.columna, self.y, ajustes.COLORES_NOTAS[self.columna])
