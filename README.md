# Grooving

Juego de ritmo de baile urbano para el Obligatorio 1 de Programación 2.

## Versión jugable

Esta versión permite elegir los colores de una bailarina o un bailarín de pixel art, con
gorra, remera corta, pantalón amplio y zapatillas. La estética toma como
inspiración los arcades de pelea de los años 90, con un personaje original. La partida ya incluye señales que bajan, puntaje y pantallas de victoria y
derrota. Incluye dos efectos de sonido arcade y cinco pistas instrumentales originales. El informe está pendiente.

## Instalación y ejecución

Necesitás Python 3 y pygame. En la terminal:

```bash
python3 -m pip install pygame
```

Abrí la carpeta `Grooving` en VS Code y, en su terminal, ejecutá:

```bash
python3 main.py
```

## Controles actuales

- `1`: cambiar el color de la remera y la gorra.
- `2`: cambiar el color del pantalón.
- `3`: cambiar el color del pelo.
- `4`: elegir bailarina o bailarín. Conserva los colores elegidos.
- `5`: elegir sin accesorio, lentes, cadena o auriculares.
- Campo `Nombre`: escribí directamente al abrir el juego, sin presionar una
  tecla para activar el campo. `Enter` confirma y muestra el nombre arriba del
  personaje. `Retroceso` borra. Podés volver a editar haciendo clic en el campo.
  El máximo es de 12 caracteres. Mientras escribís, los números son parte del
  nombre; después de confirmar, las teclas 1 a 5 personalizan el personaje.
- `Esc` o la X de la ventana: salir.

## Cómo jugar

1. Escribí el nombre y confirmalo con `Enter`.
2. Personalizá el personaje y presioná `Espacio` para elegir la canción.
   Escuchá las pistas con izquierda/derecha y presioná `Enter` para empezar.
3. Presioná izquierda, abajo, arriba o derecha cuando la señal de esa columna
   esté sobre la flecha fija, en la zona clara.
4. Cada acierto suma 100 puntos. Una señal perdida o una flecha pulsada fuera
   de tiempo cuenta como error. Las demás teclas no suman errores.
5. Ganás con 20 aciertos y perdés con cinco errores.
6. Al terminar, `Enter` reinicia conservando tu personaje y `P` vuelve a la
   personalización. `C` permite elegir otra canción. `Esc` o la X cierran el juego.

El personaje hace un paso por cada flecha con poses de pixel art distintas:
izquierda y derecha extienden un brazo y abren las piernas, abajo hace un
groove con rodillas flexionadas y arriba levanta los brazos y una pierna. La animación no suma puntos:
para acertar hay que pulsar a tiempo.

La canción elegida define la dificultad de toda la partida: fácil, medio,
difícil, súper difícil o experto. Los niveles más altos tienen música más rápida,
menos tiempo para anticipar las señales y más pasos por segundo. Podés elegir
cualquier nivel desde el comienzo. La meta es de 20 aciertos y el límite es de
cinco errores en todos los niveles.
Un sonido agudo señala cada acierto y uno grave señala los errores, incluidas
las señales que se pasan. Antes de jugar podés elegir entre cinco pistas instrumentales en bucle:

| Nivel | Canción | Ritmo | Estilo |
| --- | --- | --- | --- |
| Fácil | Barrio Groove | 80 BPM | Boom bap |
| Medio | Neon Steps | 100 BPM | Electro |
| Difícil | Cypher Night | 120 BPM | Funk arcade |
| Súper difícil | Rooftop Flow | 140 BPM | Trap |
| Experto | Final Battle | 160 BPM | Drum & bass |

Cada pista tiene su propia melodía, bajo, percusión y timbre. BPM significa
pulsos por minuto. Las señales llegan sobre pulsos o medios pulsos musicales.
Fácil y medio tienen un paso por pulso; desde difícil, uno por medio pulso.
La canción reinicia junto con la partida.

## Archivos

- `audio.py`: carga de efectos y canciones, reproducción y canal reservado.
- `main.py`: ventana, eventos, estados y bucle principal.
- `ajustes.py`: colores, medidas y opciones de personalización.
- `jugador.py`: clase `Jugador`, nombre, apariencia y dibujo del personaje.
- `poses.py`: dibujos de brazos y piernas para los cuatro pasos de cada personaje.
- `nota.py`: clase `Nota`, movimiento y dibujo de las flechas.
- `partida.py`: creación de partidas, reglas, aciertos, errores y puntaje.
- `pantallas.py`: dibujo de la personalización, pista y resultados.

## Recursos

El personaje original se dibuja con una lista de filas y rectángulos de pygame.
Cada letra indica un color de la paleta; no se usan sprites de otros juegos.

- `assets/acierto.wav`: efecto agudo de dos notas.
- `assets/error.wav`: efecto grave descendente.

- `assets/barrio.wav`, `assets/neon.wav`, `assets/cypher.wav`,
  `assets/rooftop.wav` y `assets/final.wav`: pistas instrumentales
  con percusión, bajo y melodías sintetizadas.

Los siete archivos de audio fueron sintetizados específicamente para Grooving con ayuda de
ChatGPT/Codex; no se descargaron de bancos de audio ni contienen grabaciones
ajenas. Se permite reutilizarlos bajo licencia CC0 1.0. Se cargan una sola vez
antes del bucle principal; la selección cambia cuál se reproduce. El volumen se configura en `ajustes.py`.

La única biblioteca externa es pygame. También se usa `random` para las columnas
aleatorias y `os` para ubicar los sonidos junto a `main.py`; ambos vienen con Python.

Conservá la carpeta `assets` junto a `main.py`, también al descargar o entregar el juego.

## Uso de inteligencia artificial

Se utilizó ChatGPT/Codex como apoyo para organizar y generar y modificar
el código, las poses, los efectos de sonido y la documentación, siguiendo los materiales de las clases.
La revisión por parte de la estudiante y los comentarios personales están pendientes.

## Repositorio

https://github.com/pipicea-bit/Obligatorio-programaci-n-2-Maria-Pia-Cea-282539

## Autora

María Pía Cea — 282539.

## Cómo funciona el ritmo

Se usa `pygame.time.get_ticks()` para medir los milisegundos desde que empezó la
canción. Con `60000 / bpm` se calcula cuánto dura un pulso. La altura de cada
señal se calcula con ese tiempo, para que su llegada coincida con el pulso y
no dependa de contar cuadros. Son operaciones, listas, diccionarios y clases
simples; no se agregan bibliotecas externas para reproducir la música.
