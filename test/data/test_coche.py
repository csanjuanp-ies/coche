import pytest

from src.data.coche import Coche


@pytest.mark.parametrize(
	("direccion", "representacion"),
	[
		(Coche.Direccion.NORTE, "\u2191"),
		(Coche.Direccion.ESTE, "\u2190"),
		(Coche.Direccion.SUR, "\u2193"),
		(Coche.Direccion.OESTE, "\u2192"),
	],
)
def test_string_returns_arrow_for_each_direction(direccion: Coche.Direccion, 
                                                representacion: str):
	coche = Coche(0.0, 0.0, direccion)

	assert str(coche) == representacion


def test_constructor_stores_position_and_defaults_to_north():
	coche = Coche(-3.7, 40.4)

	assert coche.posicion.longitud == -3.7
	assert coche.posicion.latitud == 40.4
	assert coche.direccion == Coche.Direccion.NORTE


@pytest.mark.parametrize(
	("direccion", "representacion"),
	[
		(Coche.Direccion.NORTE, "\u2191"),
		(Coche.Direccion.ESTE, "\u2190"),
		(Coche.Direccion.SUR, "\u2193"),
		(Coche.Direccion.OESTE, "\u2192"),
	],
)
def test_log_includes_position_and_direction(direccion: Coche.Direccion,
												 representacion: str):
	coche = Coche(-3.7, 40.4, direccion)

	assert coche.log() == f"Coche en (-3.7, 40.4) mirando hacia {representacion}"
