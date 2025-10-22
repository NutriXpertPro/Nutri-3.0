from django.db import connections
from django.db.utils import OperationalError


def test_database_connection():
    try:
        connections["default"].cursor()
        db_connected = True
    except OperationalError:
        db_connected = False
    assert db_connected, (
        "Não foi possível conectar ao banco de dados PostgreSQL. "
        "Verifique as configurações."
    )
