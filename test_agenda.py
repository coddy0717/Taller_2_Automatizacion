"""Pruebas unitarias de la agenda telefonica."""

import pytest

from agenda import (
    Agenda,
    ContactoInvalidoError,
    validar_nombre,
    validar_telefono,
)


# ----------------------------------------------------------------------
# Validaciones de nombre (Desarrollador A)
# ----------------------------------------------------------------------
class TestValidarNombre:
    @pytest.mark.parametrize(
        "nombre",
        ["Juan", "Maria Perez", "Ana Sofia", "Nuñez", "José Andrés"],
    )
    def test_nombres_validos(self, nombre):
        assert validar_nombre(nombre) is True

    @pytest.mark.parametrize(
        "nombre",
        ["Juan123", "Pedro9", "", "   ", "!!!", "Ana_Perez", "1234"],
    )
    def test_nombres_invalidos(self, nombre):
        assert validar_nombre(nombre) is False

    def test_nombre_no_string(self):
        assert validar_nombre(1234) is False
        assert validar_nombre(None) is False

    def test_nombre_con_espacios_alrededor(self):
        assert validar_nombre("  Juan  ") is True


# ----------------------------------------------------------------------
# Validaciones de telefono (Desarrollador A)
# ----------------------------------------------------------------------
class TestValidarTelefono:
    @pytest.mark.parametrize("telefono", ["0991234567", "1234567890"])
    def test_telefonos_validos(self, telefono):
        assert validar_telefono(telefono) is True

    def test_telefono_como_entero(self):
        assert validar_telefono(1234567890) is True

    @pytest.mark.parametrize(
        "telefono",
        ["123456789", "12345678901", "099123456a", "", "abcdefghij"],
    )
    def test_telefonos_invalidos(self, telefono):
        assert validar_telefono(telefono) is False

    def test_telefono_corto_como_entero(self):
        assert validar_telefono(12345) is False

    def test_telefono_no_string_ni_int(self):
        assert validar_telefono(None) is False
        assert validar_telefono(True) is False


# ----------------------------------------------------------------------
# Registro de contactos (Desarrollador A)
# ----------------------------------------------------------------------
class TestRegistrarContacto:
    def test_registro_exitoso(self):
        agenda = Agenda()
        contacto = agenda.registrar_contacto("Juan Perez", "0991234567")
        assert contacto == {"nombre": "Juan Perez", "telefono": "0991234567"}
        assert agenda.total_contactos() == 1

    def test_registro_normaliza_espacios(self):
        agenda = Agenda()
        contacto = agenda.registrar_contacto("  Ana  ", "  0991234567  ")
        assert contacto["nombre"] == "Ana"
        assert contacto["telefono"] == "0991234567"

    def test_registro_nombre_invalido(self):
        agenda = Agenda()
        with pytest.raises(ContactoInvalidoError):
            agenda.registrar_contacto("Juan123", "0991234567")

    def test_registro_telefono_invalido(self):
        agenda = Agenda()
        with pytest.raises(ContactoInvalidoError):
            agenda.registrar_contacto("Juan", "12345")

    def test_registro_duplicado(self):
        agenda = Agenda()
        agenda.registrar_contacto("Juan", "0991234567")
        with pytest.raises(ContactoInvalidoError):
            agenda.registrar_contacto("juan", "0997654321")


# ----------------------------------------------------------------------
# Busqueda de contactos (Desarrollador B)
# ----------------------------------------------------------------------
class TestBuscarContacto:
    @pytest.fixture
    def agenda(self):
        agenda = Agenda()
        agenda.registrar_contacto("Juan Perez", "0991234567")
        agenda.registrar_contacto("Maria Lopez", "0987654321")
        return agenda

    def test_busqueda_existente(self, agenda):
        contacto = agenda.buscar_contacto("Juan Perez")
        assert contacto is not None
        assert contacto["telefono"] == "0991234567"

    def test_busqueda_sin_distinguir_mayusculas(self, agenda):
        assert agenda.buscar_contacto("juan perez") is not None

    def test_busqueda_inexistente(self, agenda):
        assert agenda.buscar_contacto("Pedro") is None

    def test_busqueda_no_string(self, agenda):
        assert agenda.buscar_contacto(123) is None

    def test_busqueda_por_coincidencia(self, agenda):
        resultados = agenda.buscar_por_coincidencia("perez")
        assert len(resultados) == 1
        assert resultados[0]["nombre"] == "Juan Perez"

    def test_coincidencia_vacia(self, agenda):
        assert agenda.buscar_por_coincidencia("") == []

    def test_coincidencia_sin_resultados(self, agenda):
        assert agenda.buscar_por_coincidencia("xyz") == []
