import pytest

from src.agenda import Agenda, ContactoInvalidoError


# ----------------------------------------------------------------------
# Registro de contactos (Desarrollador A)
# ----------------------------------------------------------------------
def test_registro_exitoso():
    agenda = Agenda()
    contacto = agenda.registrar_contacto("Juan Perez", "0991234567")
    assert contacto == {"nombre": "Juan Perez", "telefono": "0991234567"}
    assert agenda.total_contactos() == 1


def test_registro_normaliza_espacios():
    agenda = Agenda()
    contacto = agenda.registrar_contacto("  Ana  ", "  0991234567  ")
    assert contacto["nombre"] == "Ana"
    assert contacto["telefono"] == "0991234567"


def test_registro_nombre_invalido():
    agenda = Agenda()
    with pytest.raises(ContactoInvalidoError):
        agenda.registrar_contacto("Juan123", "0991234567")


def test_registro_telefono_invalido():
    agenda = Agenda()
    with pytest.raises(ContactoInvalidoError):
        agenda.registrar_contacto("Juan", "12345")


def test_registro_duplicado():
    agenda = Agenda()
    agenda.registrar_contacto("Juan", "0991234567")
    with pytest.raises(ContactoInvalidoError):
        agenda.registrar_contacto("juan", "0997654321")


# ----------------------------------------------------------------------
# Busqueda de contactos (Desarrollador B)
# ----------------------------------------------------------------------
@pytest.fixture
def agenda():
    agenda = Agenda()
    agenda.registrar_contacto("Juan Perez", "0991234567")
    agenda.registrar_contacto("Maria Lopez", "0987654321")
    return agenda


def test_busqueda_existente(agenda):
    contacto = agenda.buscar_contacto("Juan Perez")
    assert contacto is not None
    assert contacto["telefono"] == "0991234567"


def test_busqueda_sin_distinguir_mayusculas(agenda):
    assert agenda.buscar_contacto("juan perez") is not None


def test_busqueda_inexistente(agenda):
    assert agenda.buscar_contacto("Pedro") is None


def test_busqueda_no_string(agenda):
    assert agenda.buscar_contacto(123) is None


def test_busqueda_por_coincidencia(agenda):
    resultados = agenda.buscar_por_coincidencia("perez")
    assert len(resultados) == 1
    assert resultados[0]["nombre"] == "Juan Perez"


def test_coincidencia_vacia(agenda):
    assert agenda.buscar_por_coincidencia("") == []


def test_coincidencia_sin_resultados(agenda):
    assert agenda.buscar_por_coincidencia("xyz") == []


def test_listar_contactos(agenda):
    contactos = agenda.listar_contactos()
    assert len(contactos) == 2
    nombres = [c["nombre"] for c in contactos]
    assert "Juan Perez" in nombres
    assert "Maria Lopez" in nombres


def test_listar_contactos_vacia():
    agenda = Agenda()
    assert agenda.listar_contactos() == []
