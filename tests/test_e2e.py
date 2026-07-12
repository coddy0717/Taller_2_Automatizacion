import subprocess
import sys


def test_app_e2e():
    # Simula la interaccion del usuario con el menu:
    # registrar -> buscar -> listar -> salir.
    entradas = "\n".join(
        [
            "1",            # opcion: registrar
            "Juan Perez",   # nombre
            "0991234567",   # telefono
            "2",            # opcion: buscar
            "Juan Perez",   # nombre a buscar
            "3",            # opcion: listar
            "0",            # opcion: salir
        ]
    ) + "\n"

    resultado = subprocess.run(
        [sys.executable, "app.py"],
        input=entradas,
        capture_output=True,
        text=True,
    )

    assert "AGENDA TELEFONICA" in resultado.stdout
    assert "Contacto registrado: Juan Perez - 0991234567" in resultado.stdout
    assert "Encontrado: Juan Perez - 0991234567" in resultado.stdout
    assert "Juan Perez: 0991234567" in resultado.stdout
    assert "Saliendo de la agenda" in resultado.stdout
