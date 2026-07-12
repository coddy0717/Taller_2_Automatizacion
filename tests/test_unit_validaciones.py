import pytest

from src.validaciones import validar_nombre, validar_telefono


@pytest.mark.parametrize(
    "nombre",
    ["Juan", "Maria Perez", "Ana Sofia", "Nuñez", "José Andrés"],
)
def test_nombres_validos(nombre):
    assert validar_nombre(nombre) is True


@pytest.mark.parametrize(
    "nombre",
    ["Juan123", "Pedro9", "", "   ", "!!!", "Ana_Perez", "1234"],
)
def test_nombres_invalidos(nombre):
    assert validar_nombre(nombre) is False


def test_nombre_no_string():
    assert validar_nombre(1234) is False
    assert validar_nombre(None) is False


def test_nombre_con_espacios_alrededor():
    assert validar_nombre("  Juan  ") is True


@pytest.mark.parametrize("telefono", ["0991234567", "1234567890"])
def test_telefonos_validos(telefono):
    assert validar_telefono(telefono) is True


def test_telefono_como_entero():
    assert validar_telefono(1234567890) is True


@pytest.mark.parametrize(
    "telefono",
    ["123456789", "12345678901", "099123456a", "", "abcdefghij"],
)
def test_telefonos_invalidos(telefono):
    assert validar_telefono(telefono) is False


def test_telefono_corto_como_entero():
    assert validar_telefono(12345) is False


def test_telefono_no_string_ni_int():
    assert validar_telefono(None) is False
    assert validar_telefono(True) is False
