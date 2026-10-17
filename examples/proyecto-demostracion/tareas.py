"""Dominio pequeño y puro para ejemplificar checkpoints."""


def agregar_tarea(tareas, titulo):
    if not isinstance(titulo, str) or not titulo.strip():
        raise ValueError("El título debe ser un texto no vacío")
    if not isinstance(tareas, list):
        raise TypeError("Las tareas deben ser una lista")
    return [*tareas, {"titulo": titulo.strip(), "estado": "pendiente"}]
