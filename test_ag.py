import pytest
from ag import Materia, AlgoritmoGenetico, obtener_calif_cuatrimestre, obtener_calif_seriacion, obtener_calif_holgura
import random

@pytest.fixture
def materias_fixture():
    return [
        Materia("Matemáticas", 1, "A", [8, 9], [], [8, 9], [], []),
        Materia("Física", 2, "B", [], [10, 11], [], [], [12]),
        Materia("Química", 3, "C", [7], [9], [], [], []),
    ]

def test_materia_equality():
    materia1 = Materia("Matemáticas", 1, "A", [8, 9], [], [8, 9], [], [])
    materia2 = Materia("Matemáticas", 1, "A", [8, 9], [], [8, 9], [], [])
    assert materia1 == materia2

def test_materia_calif_cuatrimestre(materias_fixture):
    obtener_calif_cuatrimestre(materias_fixture)
    assert materias_fixture[0].calif_cuatrimestre == 3
    assert materias_fixture[1].calif_cuatrimestre == 2

def test_calif_seriacion(materias_fixture):
    mapa_curricular = [
        {"nombre": "Matemáticas", "seriacion": [0, 1, 0], "cuatrimestre": 1, "holgura": 2},
        {"nombre": "Física", "seriacion": [1, 0, 1], "cuatrimestre": 2, "holgura": 1},
    ]
    obtener_calif_seriacion(materias_fixture)
    assert materias_fixture[0].calif_seriacion == 2
    assert materias_fixture[1].calif_seriacion == 1

def test_choque_materias():
    materia1 = Materia("Matemáticas", 1, "A", [8, 9], [], [8, 9], [], [])
    materia2 = Materia("Física", 1, "B", [8], [], [], [], [])
    ag = AlgoritmoGenetico(0.8, 0.1, 10, 5, 10, [materia1, materia2])
    choque = ag.evaluar_choque_materias(materia2, {materia1})
    assert choque is True

def test_algoritmo_genetico_crear_poblacion(materias_fixture):
    ag = AlgoritmoGenetico(0.8, 0.1, 10, 5, 10, materias_fixture)
    ag.crear_pob_inicial()
    assert len(ag.poblacion) == 5
    assert all(len(horario) > 0 for horario in ag.poblacion)