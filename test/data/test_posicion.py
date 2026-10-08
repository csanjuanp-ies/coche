import pytest

from src.data.posicion import Posicion


def test_inicializacion_guarda_latitud_y_longitud() -> None:
    # La construcción conserva ambas coordenadas recibidas.
    posicion = Posicion(40.4168, -3.7038)

    assert posicion.latitud == 40.4168
    assert posicion.longitud == -3.7038


@pytest.mark.parametrize(
    ("valor", "esperado"),
    [
        (-181.0, -180.0),
        (-180.0, -180.0),
        (-75.5, -75.5),
        (0.0, 0.0),
        (120.25, 120.25),
        (180.0, 180.0),
        (181.0, 180.0),
    ],
)
def test_asignar_longitud_limita_al_rango_permitido(valor: float, esperado: float) -> None:
    # El setter acepta valores válidos y limita los que exceden los extremos.
    posicion = Posicion(0.0, 0.0)

    posicion.longitud = valor

    assert posicion.longitud == esperado


@pytest.mark.parametrize(
    ("valor", "esperado"),
    [
        (-91.0, -90.0),
        (-90.0, -90.0),
        (-45.5, -45.5),
        (0.0, 0.0),
        (72.25, 72.25),
        (90.0, 90.0),
        (91.0, 90.0),
    ],
)
def test_asignar_latitud_limita_al_rango_permitido(valor: float, esperado: float) -> None:
    # El setter acepta valores válidos y limita los que exceden los extremos.
    posicion = Posicion(0.0, 0.0)

    posicion.latitud = valor

    assert posicion.latitud == esperado


def test_representacion_muestra_longitud_y_latitud() -> None:
    # La representación textual coloca primero la longitud.
    posicion = Posicion(40.5, -3.7)

    assert str(posicion) == "(-3.7, 40.5)"


def test_posiciones_con_las_mismas_coordenadas_son_iguales() -> None:
    # Dos posiciones con las mismas coordenadas deben compararse como iguales.
    primera = Posicion(40.5, -3.7)
    segunda = Posicion(40.5, -3.7)

    assert primera == segunda


def test_posiciones_con_coordenadas_distintas_no_son_iguales() -> None:
    # Cambiar cualquiera de las coordenadas hace que las posiciones sean distintas.
    primera = Posicion(40.5, -3.7)
    segunda = Posicion(40.5, -3.8)

    assert primera != segunda


def test_posicion_no_es_igual_a_un_objeto_de_otro_tipo() -> None:
    # La comparación con otro tipo no debe considerar iguales los objetos.
    posicion = Posicion(40.5, -3.7)

    assert posicion != (40.5, -3.7)