# Grooving

Juego de ritmo de baile urbano para el Obligatorio 1 de Programación 2.

## El nombre

Elegí Grooving por la palabra groove. Para mí es el alma del movimiento,
lo que le da estilo y personalidad al baile. Mi groove es propio y me
representa; esa misma identidad es la marca personal que busco en mis trabajos.

## Versión jugable

Esta versión permite elegir los colores de una bailarina o un bailarín de pixel art, con
gorra, remera corta, pantalón amplio y zapatillas. La estética toma como
inspiración los arcades de pelea de los años 90, con un personaje original. La partida ya incluye señales que bajan, puntaje y pantallas de victoria y
derrota. Incluye cuatro efectos de sonido arcade y cinco pistas instrumentales originales. El informe de cinco páginas y el afiche están incluidos en el ZIP de entrega.

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
- Botón **Volver**: regresa a la pantalla anterior sin cerrar el juego.
  Desde una partida se vuelve a la selección; al empezar de nuevo se reinicia.
- `Esc` o la X de la ventana: salir.

## Cómo jugar

1. Escribí el nombre y confirmalo con `Enter`.
2. Personalizá el personaje y presioná `Espacio` para elegir el modo con
   arriba/abajo. Confirmá con `Enter`; en 1vs1 personalizá también al jugador 2.
   Luego escuchá las pistas con izquierda/derecha y presioná `Enter` para empezar.
3. Presioná izquierda, abajo, arriba o derecha cuando la señal de esa columna
   esté sobre la flecha fija, en la zona clara.
4. Cada acierto suma 100 puntos. Una señal perdida o una flecha pulsada fuera
   de tiempo cuenta como error. Las demás teclas no suman errores.
5. En solo, ganás al alcanzar la meta de aciertos del nivel y perdés al alcanzar su
   límite de errores. Ambos se muestran en pantalla.
6. Al terminar, `Enter` reinicia conservando tu personaje y `P` vuelve a la
   personalización. `C` permite elegir otra canción. `Esc` o la X cierran el juego.

El personaje hace un paso por cada flecha con poses de pixel art distintas:
izquierda y derecha extienden un brazo y abren las piernas, abajo hace un
groove con rodillas flexionadas y arriba levanta los brazos y una pierna. La animación no suma puntos:
para acertar hay que pulsar a tiempo.

La canción elegida define la dificultad de toda la partida: fácil, medio,
difícil, súper difícil o experto. Los niveles más altos tienen música más rápida,
menos tiempo para anticipar las señales y más pasos por segundo. Podés elegir
cualquier nivel desde el comienzo. Las metas y los límites aumentan para que los niveles más difíciles también
sean más largos:

| Nivel | Aciertos para ganar | Errores para perder |
| --- | --- | --- |
| Fácil | 20 | 5 |
| Medio | 30 | 6 |
| Difícil | 40 | 7 |
| Súper difícil | 50 | 8 |
| Experto | 60 | 9 |

La derrota ocurre al alcanzar el número indicado, no después de superarlo.
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
Fácil tiene un paso por pulso. Medio y difícil alternan separaciones de un
pulso y medio pulso; medio da menos tiempo para anticipar que antes y difícil
espacia más sus señales. Súper difícil y experto tienen un paso por medio pulso.
La canción reinicia junto con la partida.

## Archivos

- `audio.py`: carga de efectos y canciones, reproducción y canal reservado.
- `main.py`: punto de entrada y bucle principal de 23 líneas.
- `controles.py`: funciones para los eventos de cada pantalla.
- `gestion.py`: estado inicial, actualización y selección de pantalla.
- `ajustes.py`: colores, medidas y opciones de personalización.
- `jugador.py`: clase `Jugador`, nombre, apariencia y dibujo del personaje.
- `poses.py`: dibujos de brazos y piernas para los cuatro pasos de cada personaje.
- `nota.py`: clase `Nota`, movimiento y dibujo de las flechas.
- `navegacion.py`: determina la pantalla anterior y el personaje a editar.
- `modos.py`: sesión, secuencia compartida, controles y ganador del duelo.
- `partida.py`: creación de partidas, reglas, aciertos, errores y puntaje.
- `pantallas.py`: dibujo de la personalización, pista y resultados.

## Recursos

El personaje original se dibuja con una lista de filas y rectángulos de pygame.
Cada letra indica un color de la paleta; no se usan sprites de otros juegos.

- `assets/acierto.wav`: efecto agudo de dos notas.
- `assets/error.wav`: efecto grave descendente.
- `assets/victoria.wav`: melodía alegre de festejo cuando aparece «¡GANASTE!».
- `assets/derrota.wav`: melodía triste descendente cuando aparece «¡PERDISTE!».

Las melodías de resultado suenan una sola vez al terminar y se detienen si
reiniciás. El sonido de derrota también se usa al terminar survival.

- `assets/barrio.wav`, `assets/neon.wav`, `assets/cypher.wav`,
  `assets/rooftop.wav` y `assets/final.wav`: pistas instrumentales
  con percusión, bajo y melodías sintetizadas.

Los nueve archivos de audio fueron sintetizados específicamente para Grooving con ayuda de
ChatGPT/Codex; no se descargaron de bancos de audio ni contienen grabaciones
ajenas. Se permite reutilizarlos bajo licencia CC0 1.0. Se cargan una sola vez
antes del bucle principal; la selección cambia cuál se reproduce. El volumen se configura en `ajustes.py`.

La única biblioteca externa es pygame. También se usa `random` para las columnas
aleatorias y `os` para ubicar los sonidos junto a `main.py`; ambos vienen con Python.

Conservá la carpeta `assets` junto a `main.py`, también al descargar o entregar el juego.

## Uso de inteligencia artificial

Se utilizó ChatGPT/Codex como apoyo para organizar, generar y modificar
el código, las poses, los efectos de sonido, las canciones y la documentación,
siguiendo los materiales de las clases y las decisiones de la estudiante.
Los comentarios se elaboraron propiamente y con apoyo de IA.
La revisión y comprensión del resto del código fue por parte de la estudiante.

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

## Modos

Después de personalizar, `Espacio` abre la selección de modo. Elegí con arriba
y abajo y confirmá con `Enter`.

- **Solo:** completá la meta de la canción antes de agotar los errores.
- **1vs1:** dos jugadores al mismo tiempo en la misma computadora. Después de elegir
  el modo se personaliza el personaje del jugador 2. Ambos juegan con la misma
  canción, dificultad y secuencia de flechas. Cada jugador termina al alcanzar la
  meta o el límite de errores; el rival puede seguir hasta terminar. Gana quien tenga más puntos; si empatan, quien
  tenga menos errores. Si ambos valores coinciden, hay empate.
- **Survival:** empieza siempre en fácil. Al completar 20 aciertos, pasa
  automáticamente a medio; luego exige 30, 40, 50 y 60 aciertos para avanzar
  por difícil, súper difícil y experto. Al cambiar de nivel cambia la canción,
  se renuevan los errores y se conservan puntos, aciertos totales y tiempo.
  Después de experto sigue con rondas de 60 aciertos cada vez más rápidas
  (Experto + 1, + 2, etc.). Solo termina cuando agotás los errores. `Enter`
  reinicia desde fácil. No hace falta elegir canción en este modo.


El jugador 1 usa las flechas. El jugador 2 usa `A` (izquierda), `S` (abajo),
`W` (arriba) y `D` (derecha). La ventana se amplía para mostrar las dos pistas
lado a lado, con personajes, puntos y errores independientes.

Al terminar ambos jugadores, `Enter`
inicia una revancha, `C` cambia el nivel y `M` vuelve a elegir el modo.

`modos.py` guarda la sesión, los personajes, las dos rondas, la secuencia compartida y los
resultados del duelo. Todas las estructuras son listas y diccionarios.

## Personalizar al segundo jugador

Al elegir 1vs1 aparece **Personalizá al jugador 2**. El segundo jugador puede
usar directamente 1 a 5 para elegir ropa, pelo, bailarina/bailarín y accesorios.
Para su nombre, hace clic en el campo Nombre, escribe y confirma con Enter.
Luego presiona Espacio para confirmar su personaje y elegir la canción.
Los cambios no modifican el personaje del jugador 1. Desde las canciones,
**Volver** regresa a esta personalización conservando las elecciones.

En 1vs1 hay una cuenta regresiva de **3, 2, 1** antes de empezar y en cada
revancha. Durante esos tres segundos no corre la música, no bajan señales y
las flechas/WASD no suman errores. El botón Volver y Esc siguen funcionando.
