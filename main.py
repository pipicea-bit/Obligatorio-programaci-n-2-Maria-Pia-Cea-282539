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
    nombre_confirmado = personaje.nombre
    personaje.nombre = ""
    editando_nombre = True
    campo_nombre = pygame.Rect(ajustes.CAMPO_NOMBRE)
    andando = True

    while andando:
        # 1. Escuchar: cada pulsación cambia el color una sola vez.
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                andando = False
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                editando_nombre = campo_nombre.collidepoint(evento.pos)
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    andando = False
                elif editando_nombre:
                    # El nombre se muestra sobre el personaje solo al confirmarlo.
                    if evento.key == pygame.K_RETURN:
                        if personaje.nombre.strip() != "":
                            personaje.nombre = personaje.nombre.strip()
                            nombre_confirmado = personaje.nombre
                        else:
                            personaje.nombre = nombre_confirmado
                        editando_nombre = False
                    else:
                        personaje.editar_nombre(evento)
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
        dibujar_texto(pantalla, fuente, "ELEGÍ TU ESTILO", ajustes.BLANCO, 50, 180)
        dibujar_texto(pantalla, fuente, "1  REMERA + GORRA", ajustes.LILA, 50, 225)
        dibujar_texto(pantalla, fuente, "2  PANTALÓN", ajustes.MENTA, 50, 260)
        dibujar_texto(pantalla, fuente, "3  PELO", ajustes.ROSA, 50, 295)
        dibujar_texto(pantalla, fuente, "4  BAILARINA / BAILARÍN", ajustes.AMARILLO, 50, 330)
        dibujar_texto(pantalla, fuente, "5  ACCESORIOS", ajustes.MENTA, 50, 365)
        dibujar_texto(pantalla, chica, ajustes.ACCESORIOS[personaje.accesorio], ajustes.BLANCO, 85, 395)
        dibujar_texto(pantalla, chica, "NOMBRE", ajustes.ROSA, 50, 425)
        pygame.draw.rect(pantalla, ajustes.CONTORNO, campo_nombre)
        borde = ajustes.ROSA
        texto_nombre = personaje.nombre
        if editando_nombre:
            borde = ajustes.MENTA
            texto_nombre = texto_nombre + "_"
        pygame.draw.rect(pantalla, borde, campo_nombre, ajustes.GROSOR_LINEA)
        dibujar_texto(pantalla, chica, texto_nombre, ajustes.BLANCO, 60, 455)
        dibujar_texto(pantalla, chica, "ENTER: CONFIRMAR / CLIC: EDITAR", ajustes.BLANCO, 50, 490)
        dibujar_texto(pantalla, chica, nombre_confirmado, ajustes.AMARILLO, 545, 170)
        personaje.dibujar(pantalla)
        dibujar_texto(pantalla, chica, "PERSONALIZACIÓN  /  ESC: SALIR", ajustes.BLANCO, 50, 552)
        pygame.display.flip()

        # 4. Esperar: limitar la velocidad del bucle a 60 cuadros por segundo.
        reloj.tick(ajustes.FPS)

    pygame.quit()


if __name__ == "__main__":
    main()

