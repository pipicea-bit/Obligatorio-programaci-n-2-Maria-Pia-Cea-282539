"""Arranque y bucle principal de Grooving."""

import pygame
import ajustes
import jugador
import partida
import pantallas
import audio


def main():
    """Escucha eventos, actualiza la partida y dibuja la pantalla actual."""
    pygame.init()
    pantalla = pygame.display.set_mode((ajustes.ANCHO, ajustes.ALTO))
    pygame.display.set_caption("Grooving")
    reloj = pygame.time.Clock()
    sonidos, canciones = audio.cargar_audio()
    # Las fuentes se crean una sola vez, antes del bucle.
    fuentes = {
        "titulo": pygame.font.SysFont(ajustes.FUENTE, ajustes.TAMANIO_TITULO, bold=True),
        "texto": pygame.font.SysFont(ajustes.FUENTE, ajustes.TAMANIO_TEXTO, bold=True),
        "chica": pygame.font.SysFont(ajustes.FUENTE, ajustes.TAMANIO_CHICO, bold=True),
    }
    personaje = jugador.Jugador()
    nombre_confirmado = personaje.nombre
    personaje.nombre = ""
    editando_nombre = True
    campo_nombre = pygame.Rect(ajustes.CAMPO_NOMBRE)
    seleccion = 0
    inicio_musica = 0
    datos = partida.crear_partida()
    estado = "personalizacion"
    andando = True

    while andando:
        # 1. Escuchar: las teclas tienen un uso distinto en cada pantalla.
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                andando = False
            elif evento.type == pygame.MOUSEBUTTONDOWN and estado == "personalizacion":
                editando_nombre = campo_nombre.collidepoint(evento.pos)
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    andando = False
                elif estado == "personalizacion":
                    if editando_nombre:
                        if evento.key == pygame.K_RETURN:
                            if personaje.nombre.strip() != "":
                                nombre_confirmado = personaje.nombre.strip()
                            personaje.nombre = nombre_confirmado
                            editando_nombre = False
                        else:
                            personaje.editar_nombre(evento)
                    elif evento.key == pygame.K_SPACE:
                        personaje.nombre = nombre_confirmado
                        estado = "canciones"
                        audio.reproducir(canciones, seleccion)
                    else:
                        personaje.personalizar(evento.key)
                elif estado == "canciones":
                    if evento.key == pygame.K_LEFT:
                        seleccion = (seleccion - 1) % len(canciones)
                        audio.reproducir(canciones, seleccion)
                    elif evento.key == pygame.K_RIGHT:
                        seleccion = (seleccion + 1) % len(canciones)
                        audio.reproducir(canciones, seleccion)
                    elif evento.key == pygame.K_RETURN:
                        datos = partida.crear_partida(seleccion)
                        inicio_musica = audio.reproducir(canciones, seleccion)
                        estado = "jugando"
                    elif evento.key == pygame.K_p:
                        audio.detener()
                        estado = "personalizacion"
                elif estado == "jugando":
                    columna = partida.obtener_columna(evento.key)
                    if columna != -1:
                        personaje.bailar(columna)
                    tiempo = pygame.time.get_ticks() - inicio_musica
                    resultado = partida.registrar_paso(datos, evento.key, tiempo)
                    if resultado != "":
                        sonidos[resultado].play()
                    # Comprobamos el final enseguida para no contar más pulsaciones.
                    estado = partida.obtener_estado(datos)
                elif evento.key == pygame.K_RETURN:
                    datos = partida.crear_partida(seleccion)
                    inicio_musica = audio.reproducir(canciones, seleccion)
                    estado = "jugando"
                elif evento.key == pygame.K_c:
                    estado = "canciones"
                    audio.reproducir(canciones, seleccion)
                elif evento.key == pygame.K_p:
                    audio.detener()
                    estado = "personalizacion"
                    editando_nombre = False

        # 2. Actualizar: las señales solo se mueven durante la partida.
        if estado == "jugando" and andando:
            errores_antes = datos["errores"]
            tiempo = pygame.time.get_ticks() - inicio_musica
            partida.actualizar(datos, tiempo)
            if datos["errores"] > errores_antes:
                sonidos["error"].play()
            estado = partida.obtener_estado(datos)

        if estado == "jugando":
            personaje.actualizar_baile()
        else:
            personaje.detener_baile()
            if estado == "victoria" or estado == "derrota":
                audio.detener()

        # 3. Dibujar: cada pantalla recibe los datos que necesita mostrar.
        if estado == "personalizacion":
            pantallas.personalizacion(pantalla, fuentes, personaje,
                                      nombre_confirmado, editando_nombre, campo_nombre)
        elif estado == "canciones":
            pantallas.elegir_cancion(pantalla, fuentes, personaje, seleccion)
        else:
            pantallas.juego(pantalla, fuentes, personaje, datos, estado)
        pygame.display.flip()
        # 4. Esperar: conservar la velocidad del juego en 60 cuadros por segundo.
        reloj.tick(ajustes.FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
