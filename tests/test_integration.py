from src.agenda import Agenda


def test_registro_y_busqueda():
    agenda = Agenda()
    agenda.registrar_contacto("Maria Lopez", "0987654321")
    contacto = agenda.buscar_contacto("Maria Lopez")
    assert contacto is not None
    assert contacto["telefono"] == "0987654321"


def test_flujo_varios_contactos():
    agenda = Agenda()
    agenda.registrar_contacto("Juan Perez", "0991234567")
    agenda.registrar_contacto("Ana Torres", "09876543211")
    assert agenda.total_contactos() == 2
    assert agenda.buscar_contacto("Ana Torres")["telefono"] == "0987654321"
