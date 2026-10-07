"""Personajes de pixel art con colores personalizables."""

import pygame
import ajustes


class Jugador:
    """Representa un personaje de baile urbano dibujado sobre una cuadrícula."""

    def __init__(self):
        """Guarda las opciones de ropa y el dibujo de píxeles del personaje."""
        self.personaje = "bailarina"
        self.remera = 0
        self.pantalon = 0
        self.pelo = 0
        self.accesorio = 0
        self.nombre = "PLAYER 01"
        # Cada letra es un color. Los puntos son espacios transparentes.
        # Esta lista forma una figura: gorra, pelo, rostro, ropa y zapatillas.
        self.dibujo_bailarina = [
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

        # El bailarín comparte el estilo arcade, con pelo corto y remera larga.
        self.dibujo_bailarin = self.dibujo_bailarina[:]
        self.dibujo_bailarin[10] = ".......OHSSSSSO........."
        self.dibujo_bailarin[11] = "........OOSSSO.........."
        self.dibujo_bailarin[12] = "........ORRRRO.........."
        self.dibujo_bailarin[13] = ".......ORRRRRRO........."
        self.dibujo_bailarin[14] = "......ORRRRLRRRO........"
        self.dibujo_bailarin[15] = ".....ORRRRLLRRRRO......."
        self.dibujo_bailarin[16] = "....ORRORRRLRRRRRO......"
        self.dibujo_bailarin[22] = "....OO..ORRRRROSSSO....."

    def obtener_dibujo(self):
        """Devuelve el dibujo del personaje seleccionado."""
        if self.personaje == "bailarin":
            return self.dibujo_bailarin
        return self.dibujo_bailarina

    def siguiente_color(self, opcion, colores):
        """Devuelve la opción siguiente, volviendo a cero al final."""
        opcion = opcion + 1
        if opcion == len(colores):
            opcion = 0
        return opcion

    def personalizar(self, tecla):
        """Cambia remera y gorra, pantalón o pelo y el personaje con las teclas 1 a 5."""
        if tecla == pygame.K_1:
            self.remera = self.siguiente_color(self.remera, ajustes.COLORES_REMERA)
        elif tecla == pygame.K_2:
            self.pantalon = self.siguiente_color(self.pantalon, ajustes.COLORES_PANTALON)
        elif tecla == pygame.K_3:
            self.pelo = self.siguiente_color(self.pelo, ajustes.COLORES_PELO)

        elif tecla == pygame.K_4:
            if self.personaje == "bailarina":
                self.personaje = "bailarin"
            else:
                self.personaje = "bailarina"

        elif tecla == pygame.K_5:
            self.accesorio = self.siguiente_color(self.accesorio, ajustes.ACCESORIOS)

    def editar_nombre(self, evento):
        """Agrega caracteres al nombre o borra el último con Retroceso."""
        if evento.key == pygame.K_BACKSPACE:
            self.nombre = self.nombre[:-1]
        elif len(self.nombre) < ajustes.LARGO_NOMBRE and evento.unicode.isprintable():
            self.nombre = self.nombre + evento.unicode

    def dibujar_accesorio(self, pantalla):
        """Dibuja lentes, cadena o auriculares sobre la cuadrícula del personaje."""
        piezas = []
        color = ajustes.AMARILLO
        if self.accesorio == 1:
            piezas = [(10, 7, 3, 2), (14, 7, 3, 2), (13, 7, 1, 1)]
            color = ajustes.CONTORNO
        elif self.accesorio == 2:
            piezas = [(10, 13, 1, 2), (14, 13, 1, 2), (11, 15, 3, 1), (12, 16, 1, 1)]
        elif self.accesorio == 3:
            # Vincha por encima de la gorra y almohadillas a ambos lados.
            piezas = [(9, 0, 8, 2), (7, 1, 2, 5), (17, 1, 2, 5),
                      (6, 5, 4, 6), (17, 5, 4, 6)]
            color = ajustes.CONTORNO
        for columna, fila, ancho, alto in piezas:
            x = ajustes.PERSONAJE_X + columna * ajustes.PIXEL
            y = ajustes.PERSONAJE_Y + fila * ajustes.PIXEL
            pygame.draw.rect(pantalla, color,
                             (x, y, ancho * ajustes.PIXEL, alto * ajustes.PIXEL))

        if self.accesorio == 3:
            # Las zonas claras separan la vincha y las copas del pelo oscuro.
            detalles = [(9, 0, 8, 1), (8, 1, 1, 5), (17, 1, 1, 5),
                        (7, 6, 2, 4), (18, 6, 2, 4)]
            for columna, fila, ancho, alto in detalles:
                x = ajustes.PERSONAJE_X + columna * ajustes.PIXEL
                y = ajustes.PERSONAJE_Y + fila * ajustes.PIXEL
                pygame.draw.rect(pantalla, ajustes.MENTA,
                                 (x, y, ancho * ajustes.PIXEL, alto * ajustes.PIXEL))

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
        dibujo = self.obtener_dibujo()
        # Son dos for como en clase: uno recorre filas y otro, cada letra.
        for fila in range(len(dibujo)):
            for columna in range(len(dibujo[fila])):
                letra = dibujo[fila][columna]
                if letra != ".":
                    x = ajustes.PERSONAJE_X + columna * ajustes.PIXEL
                    y = ajustes.PERSONAJE_Y + fila * ajustes.PIXEL
                    pygame.draw.rect(pantalla, colores[letra],
                                     (x, y, ajustes.PIXEL, ajustes.PIXEL))
        self.dibujar_accesorio(pantalla)
