"""Medidas, colores y opciones del arcade Grooving."""

ANCHO = 800
ALTO = 600
FPS = 60
FONDO = (21, 18, 37)
BLANCO = (255, 238, 210)
LILA = (169, 126, 236)
ROSA = (236, 103, 131)
MENTA = (109, 204, 177)
AMARILLO = (246, 194, 94)
PIEL = (206, 143, 103)
NEGRO = (68, 58, 89)
AZUL = (78, 111, 166)
CASTANIO = (114, 71, 54)
CONTORNO = (12, 10, 23)
SOMBRA_ROPA = (53, 44, 78)
PARED = (37, 30, 56)
LADRILLO = (61, 45, 73)
PISO = (44, 39, 63)
LINEA_PISO = (76, 62, 91)

COLORES_REMERA = [LILA, ROSA, MENTA, AMARILLO]
COLORES_PANTALON = [NEGRO, AZUL, LILA]
COLORES_PELO = [CONTORNO, CASTANIO, AMARILLO]

TAMANIO_TITULO = 64
TAMANIO_TEXTO = 20
TAMANIO_CHICO = 16
FUENTE = "Courier"
PERSONAJE_X = 530
PERSONAJE_Y = 205
PIXEL = 7
ANCHO_LADRILLO = 80
ALTO_LADRILLO = 40
PISO_Y = 480
GROSOR_LINEA = 2

ACCESORIOS = ["SIN ACCESORIO", "LENTES", "CADENA", "AURICULARES"]
LARGO_NOMBRE = 12

CAMPO_NOMBRE = (50, 447, 340, 34)

# Reglas de la partida y posiciones de las señales.
METAS_PASOS = [20, 30, 40, 50, 60]
LIMITES_ERRORES = [5, 6, 7, 8, 9]
PUNTOS_ACIERTO = 100
NOTA_INICIO_Y = 170
LINEA_ACIERTO_Y = 450
MARGEN_ACIERTO = 27
COLUMNAS = [95, 195, 295, 395]
COLORES_NOTAS = [LILA, MENTA, ROSA, AMARILLO]
RADIO_NOTA = 20
GROSOR_FLECHA = 5
DURACION_MENSAJE = 35

DURACION_BAILE = 20
DESPLAZAMIENTO_BAILE = 14
SALTO_BAILE = 21

VOLUMEN_EFECTOS = 0.45

# Cada canción define un nivel. BPM significa pulsos por minuto.
CANCIONES = [
    {"nombre": "BARRIO GROOVE", "archivo": "barrio.wav", "bpm": 80, "nivel": "FÁCIL", "estilo": "BOOM BAP"},
    {"nombre": "NEON STEPS", "archivo": "neon.wav", "bpm": 100, "nivel": "MEDIO", "estilo": "ELECTRO"},
    {"nombre": "CYPHER NIGHT", "archivo": "cypher.wav", "bpm": 120, "nivel": "DIFÍCIL", "estilo": "FUNK ARCADE"},
    {"nombre": "ROOFTOP FLOW", "archivo": "rooftop.wav", "bpm": 140, "nivel": "SÚPER DIFÍCIL", "estilo": "TRAP"},
    {"nombre": "FINAL BATTLE", "archivo": "final.wav", "bpm": 160, "nivel": "EXPERTO", "estilo": "DRUM & BASS"},
]
VOLUMEN_MUSICA = 0.35
PULSOS_ANTICIPACION = [3, 2, 2.2, 1.5, 1]
# Medio y difícil alternan un pulso y medio pulso para suavizar el salto.
PULSOS_ENTRE_NOTAS = [[1], [1, 0.5], [1, 0.5], [0.5], [0.5]]
PRIMER_PULSO = 4

# Survival avanza al completar la meta de cada nivel.
ACELERACION_SURVIVAL = 0.12
AVISO_NIVEL_SUPERADO = 90
