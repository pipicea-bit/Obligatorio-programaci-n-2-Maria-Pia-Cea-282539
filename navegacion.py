"""Regreso a la pantalla anterior sin cerrar el juego."""


def volver(estado, modo, rival):
    """Devuelve la pantalla anterior y si se está editando al jugador 2."""
    if estado == "personalizacion":
        if rival:
            return "modos", False
        return estado, False
    if estado == "modos":
        return "personalizacion", False
    if estado == "canciones":
        if modo == "1vs1":
            return "personalizacion", True
        return "modos", False
    if modo == "survival":
        return "modos", False
    return "canciones", False
