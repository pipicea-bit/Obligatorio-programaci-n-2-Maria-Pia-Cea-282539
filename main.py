"""Arranque, eventos y estados de Grooving."""

import pygame
import ajustes
import jugador
import partida
import pantallas
import audio
import modos


def main():
    """Escucha eventos, actualiza la ronda y dibuja la pantalla actual."""
    pygame.init()
    pantalla = pygame.display.set_mode((ajustes.ANCHO, ajustes.ALTO))
    pygame.display.set_caption("Grooving")
    reloj = pygame.time.Clock()
    sonidos, canciones = audio.cargar_audio()
    fuentes = {
        "titulo": pygame.font.SysFont(ajustes.FUENTE, ajustes.TAMANIO_TITULO, bold=True),
        "texto": pygame.font.SysFont(ajustes.FUENTE, ajustes.TAMANIO_TEXTO, bold=True),
        "chica": pygame.font.SysFont(ajustes.FUENTE, ajustes.TAMANIO_CHICO, bold=True),
    }
    personaje = jugador.Jugador()
    nombre_confirmado = personaje.nombre
    personaje.nombre = ""
    editando_nombre = True
    configurando_rival = False
    campo_nombre = pygame.Rect(ajustes.CAMPO_NOMBRE)
    modo_elegido = 0
    seleccion = 0
    inicio_musica = 0
    sesion = modos.crear_sesion("solo", personaje)
    datos = partida.crear_partida()
    estado = "personalizacion"
    andando = True

    while andando:
        # 1. Escuchar: cada pantalla tiene sus propios controles.
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
                        if configurando_rival:
                            configurando_rival = False
                            personaje = sesion["personajes"][0]
                            nombre_confirmado = personaje.nombre
                            estado = "canciones"
                            audio.reproducir(canciones, seleccion)
                        else:
                            estado = "modos"
                    else:
                        personaje.personalizar(evento.key)
                elif estado == "modos":
                    if evento.key == pygame.K_UP:
                        modo_elegido = (modo_elegido - 1) % 3
                    elif evento.key == pygame.K_DOWN:
                        modo_elegido = (modo_elegido + 1) % 3
                    elif evento.key == pygame.K_RETURN:
                        nombres_modos = ["solo", "1vs1", "survival"]
                        sesion = modos.crear_sesion(nombres_modos[modo_elegido], personaje)
                        if sesion["modo"] == "1vs1":
                            personaje = jugador.Jugador()
                            sesion["personajes"].append(personaje)
                            nombre_confirmado = "PLAYER 02"
                            personaje.nombre = ""
                            editando_nombre = True
                            configurando_rival = True
                            estado = "personalizacion"
                        else:
                            estado = "canciones"
                            audio.reproducir(canciones, seleccion)
                    elif evento.key == pygame.K_p:
                        estado = "personalizacion"
                elif estado == "canciones":
                    if evento.key == pygame.K_LEFT:
                        seleccion = (seleccion - 1) % len(canciones)
                        audio.reproducir(canciones, seleccion)
                    elif evento.key == pygame.K_RIGHT:
                        seleccion = (seleccion + 1) % len(canciones)
                        audio.reproducir(canciones, seleccion)
                    elif evento.key == pygame.K_RETURN:
                        sesion["resultados"] = []
                        personaje = sesion["personajes"][0]
                        datos = modos.nueva_ronda(sesion, seleccion)
                        inicio_musica = audio.reproducir(canciones, seleccion)
                        estado = "jugando"
                    elif evento.key == pygame.K_p:
                        audio.detener()
                        estado = "modos"
                elif estado == "jugando":
                    tiempo = pygame.time.get_ticks() - inicio_musica
                    if sesion["modo"] == "1vs1":
                        resultado = modos.registrar_duelo(sesion, evento.key, tiempo)
                    else:
                        columna = partida.obtener_columna(evento.key)
                        if columna != -1:
                            personaje.bailar(columna)
                        resultado = partida.registrar_paso(datos, evento.key, tiempo)
                        estado = partida.obtener_estado(datos)
                    if resultado != "":
                        sonidos[resultado].play()
                elif evento.key == pygame.K_RETURN:
                    sesion["resultados"] = []
                    personaje = sesion["personajes"][0]
                    datos = modos.nueva_ronda(sesion, seleccion)
                    inicio_musica = audio.reproducir(canciones, seleccion)
                    estado = "jugando"
                elif evento.key == pygame.K_c:
                    personaje = sesion["personajes"][0]
                    estado = "canciones"
                    audio.reproducir(canciones, seleccion)
                elif evento.key == pygame.K_m:
                    audio.detener()
                    personaje = sesion["personajes"][0]
                    estado = "modos"
                elif evento.key == pygame.K_p:
                    audio.detener()
                    personaje = sesion["personajes"][0]
                    nombre_confirmado = personaje.nombre
                    estado = "personalizacion"
                    editando_nombre = False

        # 2. Actualizar: en el duelo cada pista tiene sus propios contadores.
        if estado == "jugando" and andando:
            tiempo = pygame.time.get_ticks() - inicio_musica
            if sesion["modo"] == "1vs1":
                errores_antes = sesion["rondas"][0]["errores"] + sesion["rondas"][1]["errores"]
                estado = modos.actualizar_duelo(sesion, tiempo)
                errores_despues = sesion["rondas"][0]["errores"] + sesion["rondas"][1]["errores"]
            else:
                errores_antes = datos["errores"]
                partida.actualizar(datos, tiempo)
                errores_despues = datos["errores"]
                estado = partida.obtener_estado(datos)
            if errores_despues > errores_antes:
                sonidos["error"].play()
        if estado in ["victoria", "derrota", "resultado_duelo"]:
            audio.detener()
        for bailarin in sesion["personajes"]:
            if estado == "jugando":
                bailarin.actualizar_baile()
            else:
                bailarin.detener_baile()

        # 3. Dibujar: el duelo amplía la ventana para mostrar las dos pistas.
        ancho = ajustes.ANCHO
        if estado == "jugando" and sesion["modo"] == "1vs1":
            ancho = ajustes.ANCHO * 2
        if pantalla.get_width() != ancho:
            pantalla = pygame.display.set_mode((ancho, ajustes.ALTO))
        if estado == "personalizacion":
            pantallas.personalizacion(pantalla, fuentes, personaje,
                                      nombre_confirmado, editando_nombre, campo_nombre, configurando_rival)
        elif estado == "modos":
            pantallas.elegir_modo(pantalla, fuentes, personaje, modo_elegido)
        elif estado == "canciones":
            pantallas.elegir_cancion(pantalla, fuentes, personaje, seleccion, sesion["modo"])
        elif estado == "resultado_duelo":
            pantallas.duelo(pantalla, fuentes, sesion, estado)
        elif estado == "jugando" and sesion["modo"] == "1vs1":
            pantallas.duelo_simultaneo(pantalla, fuentes, sesion)
        else:
            pantallas.juego(pantalla, fuentes, personaje, datos, estado)
        pygame.display.flip()
        # 4. Esperar: limitar a 60 cuadros por segundo.
        reloj.tick(ajustes.FPS)
    pygame.quit()


if __name__ == "__main__":
    main()
