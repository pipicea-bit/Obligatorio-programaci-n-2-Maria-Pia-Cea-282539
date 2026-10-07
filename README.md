# Grooving

Juego de ritmo de baile urbano para el Obligatorio 1 de Programación 2.

## Versión jugable

Esta versión permite elegir los colores de una bailarina o un bailarín de pixel art, con
gorra, remera corta, pantalón amplio y zapatillas. La estética toma como
inspiración los arcades de pelea de los años 90, con un personaje original. La partida ya incluye señales que bajan, puntaje y pantallas de victoria y
derrota. Los sonidos y el informe se agregarán en próximos avances.

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
2. Personalizá el personaje y presioná `Espacio` para empezar.
3. Presioná izquierda, abajo, arriba o derecha cuando la señal de esa columna
   esté sobre la flecha fija, en la zona clara.
4. Cada acierto suma 100 puntos. Una señal perdida o una flecha pulsada fuera
   de tiempo cuenta como error. Las demás teclas no suman errores.
5. Ganás con 20 aciertos y perdés con cinco errores.
6. Al terminar, `Enter` reinicia conservando tu personaje y `P` vuelve a la
   personalización. `Esc` o la X cierran el juego.

El personaje hace un paso por cada flecha con poses de pixel art distintas:
izquierda y derecha extienden un brazo y abren las piernas, abajo hace un
groove con rodillas flexionadas y arriba levanta los brazos y una pierna. La animación no suma puntos:
para acertar hay que pulsar a tiempo.

La dificultad aumenta cada cinco aciertos, hasta el nivel 4. Las señales nuevas
bajan más rápido y aparecen más seguido. Las que ya están en pantalla conservan
su velocidad para evitar cambios bruscos. El nivel se muestra en pantalla y se
reinicia al volver a jugar.
Esta versión todavía no incluye música ni efectos de sonido.

## Archivos

- `main.py`: ventana, eventos, estados y bucle principal.
- `ajustes.py`: colores, medidas y opciones de personalización.
- `jugador.py`: clase `Jugador`, nombre, apariencia y dibujo del personaje.
- `poses.py`: dibujos de brazos y piernas para los cuatro pasos de cada personaje.
- `nota.py`: clase `Nota`, movimiento y dibujo de las flechas.
- `partida.py`: creación de partidas, reglas, aciertos, errores y puntaje.
- `pantallas.py`: dibujo de la personalización, pista y resultados.

## Recursos

El personaje original se dibuja con una lista de filas y rectángulos de pygame.
Cada letra indica un color de la paleta; no se usan sprites de otros juegos. Esta versión no usa imágenes
ni sonidos externos. La única biblioteca externa del juego es pygame.

## Uso de inteligencia artificial

Se utilizó ChatGPT/Codex como apoyo para organizar y generar la primera versión
del código y la documentación, siguiendo los materiales de las clases.
La revisión por parte de la estudiante y los comentarios personales están pendientes.

## Repositorio

https://github.com/pipicea-bit/Obligatorio-programaci-n-2-Maria-Pia-Cea-282539

## Autora

María Pía Cea — 282539.
