# Grooving

Juego de ritmo de baile urbano para el Obligatorio 1 de Programación 2.

## Primera versión

Esta versión permite elegir los colores de una bailarina o un bailarín de pixel art, con
gorra, remera corta, pantalón amplio y zapatillas. La estética toma como
inspiración los arcades de pelea de los años 90, con un personaje original. La partida de ritmo,
el puntaje, los sonidos y las pantallas finales se agregarán en próximos avances.

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

## Reglas previstas

Presionar las flechas cuando las señales lleguen a la línea de baile.
Ganar al completar 20 pasos y perder al cometer cinco errores.
Poder reiniciar sin cerrar la ventana.

## Archivos

- `main.py`: ventana, eventos, textos y bucle principal.
- `ajustes.py`: colores, medidas y opciones de personalización.
- `jugador.py`: clase `Jugador`, elección de colores y dibujo del personaje.

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
