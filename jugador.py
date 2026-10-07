"""Bailarina de pixel art con colores personalizables."""

import pygame
import ajustes


class Jugador:
    """Representa una bailarina urbana dibujada sobre una cuadrícula."""

    def __init__(self):
        """Guarda las opciones de ropa y el dibujo de píxeles del personaje."""
        self.remera = 0
        self.pantalon = 0
        self.pelo = 0
        # Cada letra es un color. Los puntos son espacios transparentes.
        # Esta lista forma una figura: gorra, pelo, rostro, ropa y zapatillas.
        self.dibujo = [
            "..........OOOOOO........",
            ".........ORRRRRRO.......",
            "........ORRRRRRRRO......",
            ".......ORRRRRRRRRRO.....",
            ".......OOOOOOOOOOOOOO...",
            ".......OHHSSSSSSO.......",
            ".......OHHSSSSSSO.......",
            ".......OHSSOSOSSO.......",
            ".......OHSSSSSSSO.......",
            ".......OHSSSSSSO........",
            ".......OHHSSSSO.........",
            ".......OHHOSSO..........",
            "......OHHORRRRO.........",
            ".....OHHORRRRRRO........",
            "....OHHORRRLRRRRO.......",
            "....OHOORRRLLRRRRO......",
            "....OO.ORRRLRRRRRRO.....",
            ".......ORRRRRRRORRRO....",
            "...OOO.ORRRRRRROORRO....",
            "..OSSSOORRRRRRROORRO....",
            "..OSSSSORRRRRRROORRO....",
            "...OSSOORRRRRRROSSO.....",
            "....OO..OSSSSSOSSSO.....",
            "........OOOOOOOOSSO.....",
            ".......OPPPPPPPOOO......",
            "......OPPPPPPPPPO.......",
            ".....OPPPTPPPTPPPO......",
            ".....OPPPTPPPTPPPO......",
            ".....OPPPPPPPPPPPO......",
            ".....OPPPPPPOPPPPO......",
            ".....OPPPPPPOPPPPO......",
            ".....OPPPTPO.OPPPO......",
            ".....OPPPTPO.OPPPO......",
            "....OPPPPPPO.OPPPPO.....",
            "....OPPPPPPO.OPPPPO.....",
            "....OOOOOOOO.OOOOOO.....",
            "...OWWWWWWO..OWWWWWO....",
            "..OWWWWWWWO..OWWWWWWO...",
            "..OOOOOOOOO..OOOOOOOO...",
        ]

    def siguiente_color(self, opcion, colores):
        """Devuelve la opción siguiente, volviendo a cero al final."""
        opcion = opcion + 1
        if opcion == len(colores):
            opcion = 0
        return opcion

    def personalizar(self, tecla):
        """Cambia remera y gorra, pantalón o pelo con las teclas 1, 2 y 3."""
        if tecla == pygame.K_1:
            self.remera = self.siguiente_color(self.remera, ajustes.COLORES_REMERA)
        elif tecla == pygame.K_2:
            self.pantalon = self.siguiente_color(self.pantalon, ajustes.COLORES_PANTALON)
        elif tecla == pygame.K_3:
            self.pelo = self.siguiente_color(self.pelo, ajustes.COLORES_PELO)

    def dibujar(self, pantalla):
        """Recorre filas y columnas y dibuja un cuadrado por cada letra."""
        colores = {
            "O": ajustes.CONTORNO,
            "R": ajustes.COLORES_REMERA[self.remera],
            "P": ajustes.COLORES_PANTALON[self.pantalon],
            "H": ajustes.COLORES_PELO[self.pelo],
            "S": ajustes.PIEL,
            "W": ajustes.BLANCO,
            "L": ajustes.AMARILLO,
            "T": ajustes.SOMBRA_ROPA,
        }
        # Son dos for como en clase: uno recorre filas y otro, cada letra.
        for fila in range(len(self.dibujo)):
            for columna in range(len(self.dibujo[fila])):
                letra = self.dibujo[fila][columna]
                if letra != ".":
                    x = ajustes.PERSONAJE_X + columna * ajustes.PIXEL
                    y = ajustes.PERSONAJE_Y + fila * ajustes.PIXEL
                    pygame.draw.rect(pantalla, colores[letra],
                                     (x, y, ajustes.PIXEL, ajustes.PIXEL))
