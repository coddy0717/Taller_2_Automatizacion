import subprocess
import sys


def test_app_e2e():
    resultado = subprocess.run(
        [sys.executable, "app.py"],
        capture_output=True,
        text=True,
    )

    assert "Bienvenido a la agenda telefonica" in resultado.stdout
    assert "Contacto registrado: Juan Perez - 0991234567" in resultado.stdout
    assert "Contacto encontrado: Juan Perez - 0991234567" in resultado.stdout
    assert "Final de la ejecucion del flujo" in resultado.stdout
