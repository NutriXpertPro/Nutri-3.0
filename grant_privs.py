import pymysql
from decouple import config
from urllib.parse import urlparse


def parse_db_url(url):
    parsed = urlparse(url)
    netloc = parsed.netloc
    last_at = netloc.rfind("@")
    if last_at == -1:
        raise ValueError("No @ in netloc")
    username_password = netloc[:last_at]
    host_port = netloc[last_at + 1 :]
    if ":" in username_password:
        username, password = username_password.split(":", 1)
    else:
        username = username_password
        password = ""
    if ":" in host_port:
        host, port = host_port.rsplit(":", 1)
    else:
        host = host_port
        port = None
    return {"username": username, "password": password, "host": host, "port": port}


db_url = config("DATABASE_URL")
parsed = parse_db_url(db_url)

# Conecta como ROOT pro privilégio (edite a senha abaixo)
connection = pymysql.connect(
    host=parsed["host"],
    user="root",
    password=config("DB_ROOT_PASSWORD"),  # Lê a senha do .env
    port=int(parsed["port"]) if parsed["port"] else 3306,
    charset="utf8mb4",
)

try:
    with connection.cursor() as cursor:
        cursor.execute("GRANT CREATE ON *.* TO 'nutri_user'@'localhost'")
        cursor.execute("FLUSH PRIVILEGES")
        print("Privilégios concedidos! 'nutri_user' agora pode criar DBs de teste.")
finally:
    connection.close()
