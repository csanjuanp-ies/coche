import pytest

from src.data.posicion import Posicion


def test_constructor_and_properties_store_coordinates():
	posicion = Posicion(-3.7, 40.4)

	assert posicion.longitud == -3.7
	assert posicion.latitud == 40.4


def test_string_representation():
	posicion = Posicion(-3.7, 40.4)

	assert str(posicion) == "(-3.7, 40.4)"


@pytest.mark.parametrize("longitud", [-180.0, -75.5, 0.0, 120.25, 180.0])
def test_longitud_accepts_values_within_inclusive_range(longitud:float):
	posicion = Posicion(0.0, 0.0)

	posicion.longitud = longitud

	assert posicion.longitud == longitud


@pytest.mark.parametrize("latitud", [-90.0, -45.5, 0.0, 70.25, 90.0])
def test_latitud_accepts_values_within_inclusive_range(latitud:float):
	posicion = Posicion(0.0, 0.0)

	posicion.latitud = latitud

	assert posicion.latitud == latitud


@pytest.mark.parametrize("longitud", [-180.1, 180.1])
def test_longitud_rejects_values_outside_range_without_changing_value(longitud:float):
	posicion = Posicion(12.0, 34.0)

	with pytest.raises(ValueError, match="La longitud debe estar entre -180 y 180"):
		posicion.longitud = longitud

	assert posicion.longitud == 12.0


@pytest.mark.parametrize("latitud", [-90.1, 90.1])
def test_latitud_rejects_values_outside_range_without_changing_value(latitud:float):
	posicion = Posicion(12.0, 34.0)

	with pytest.raises(ValueError, match="La latitud debe estar entre -90 y 90"):
		posicion.latitud = latitud

	assert posicion.latitud == 34.0
