import pytest

from src.clases_datos.datosmundo import DatosMundo


def test_inicializacion_guarda_las_tres_direcciones() -> None:
    # La instancia conserva los valores recibidos para cada dirección.
    datos = DatosMundo(True, False, True)

    assert datos.izquierda is True
    assert datos.derecha is False
    assert datos.frente is True


@pytest.mark.parametrize(
    ("izquierda", "derecha", "frente", "esperado"),
    [
        (False, False, False, False),
        (False, False, True, False),
        (False, True, False, False),
        (False, True, True, False),
        (True, False, False, False),
        (True, False, True, False),
        (True, True, False, False),
        (True, True, True, True),
    ],
)
def test_all_es_verdadero_solo_si_todas_las_direcciones_lo_son(
    izquierda: bool,
    derecha: bool,
    frente: bool,
    esperado: bool,
) -> None:
    # El resultado debe ser la conjunción de las tres señales.
    datos = DatosMundo(izquierda, derecha, frente)

    assert datos.all() is esperado