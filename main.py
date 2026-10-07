"""Abre Grooving y permite personalizar el personaje."""

import pygame
import ajustes
import jugador


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


def main():
    """Prepara la ventana y ejecuta el bucle de personalización."""
    pygame.init()
    pantalla = pygame.display.set_mode((ajustes.ANCHO, ajustes.ALTO))
    pygame.display.set_caption("Grooving")
    reloj = pygame.time.Clock()

    # Las fuentes se crean una sola vez, antes del bucle, como en clase 5.
    titulo = pygame.font.SysFont(ajustes.FUENTE, ajustes.TAMANIO_TITULO, bold=True)
    fuente = pygame.font.SysFont(ajustes.FUENTE, ajustes.TAMANIO_TEXTO, bold=True)
    chica = pygame.font.SysFont(ajustes.FUENTE, ajustes.TAMANIO_CHICO, bold=True)
    personaje = jugador.Jugador()
    andando = True

    while andando:
        # 1. Escuchar: cada pulsación cambia el color una sola vez.
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                andando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    andando = False
                else:
                    personaje.personalizar(evento.key)

        # 2. Actualizar: por ahora, la apariencia cambia con los eventos.
        # En el próximo avance agregaremos las señales que bajan solas.

        # 3. Dibujar: borrar el cuadro anterior y mostrar los colores elegidos.
        dibujar_escenario(pantalla)
        dibujar_texto(pantalla, chica, "1 PLAYER  /  URBAN DANCE ARCADE", ajustes.MENTA, 40, 25)
        dibujar_texto(pantalla, titulo, "GROOVING", ajustes.CONTORNO, 44, 57)
        dibujar_texto(pantalla, titulo, "GROOVING", ajustes.AMARILLO, 40, 53)
        dibujar_texto(pantalla, chica, "TU ESTILO. TU RITMO.", ajustes.ROSA, 43, 130)
        dibujar_texto(pantalla, fuente, "ELEGÍ TU ESTILO", ajustes.BLANCO, 50, 205)
        dibujar_texto(pantalla, fuente, "1  REMERA + GORRA", ajustes.LILA, 50, 260)
        dibujar_texto(pantalla, fuente, "2  PANTALÓN", ajustes.MENTA, 50, 300)
        dibujar_texto(pantalla, fuente, "3  PELO", ajustes.ROSA, 50, 340)
        dibujar_texto(pantalla, fuente, "4  BAILARINA / BAILARÍN", ajustes.AMARILLO, 50, 380)
        dibujar_texto(pantalla, chica, "REPETÍ LA TECLA PARA CAMBIAR", ajustes.BLANCO, 50, 440)
        dibujar_texto(pantalla, chica, personaje.personaje.upper(), ajustes.AMARILLO, 555, 170)
        personaje.dibujar(pantalla)
        dibujar_texto(pantalla, chica, "PERSONALIZACIÓN  /  ESC: SALIR", ajustes.BLANCO, 50, 552)
        pygame.display.flip()

        # 4. Esperar: limitar la velocidad del bucle a 60 cuadros por segundo.
        reloj.tick(ajustes.FPS)

    pygame.quit()


if __name__ == "__main__":
    main()

