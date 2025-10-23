import mysql.connector
from mysql.connector import Error
import google.generativeai as genai
import os

# Configuração do Gemini
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-pro")


class DatabaseManager:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(
        self, host="localhost", user="root", password="", database="gemini_cli"
    ):
        """Conecta ao MariaDB do XAMPP"""
        try:
            self.connection = mysql.connector.connect(
                host=host, user=user, password=password, database=database
            )
            if self.connection.is_connected():
                self.cursor = self.connection.cursor(dictionary=True)
                print("✅ Conectado ao MariaDB!")
                return True
        except Error as e:
            print(f"❌ Erro ao conectar: {e}")
            return False

    def create_database(self, host="localhost", user="root", password=""):
        """Cria o banco de dados se não existir"""
        try:
            temp_conn = mysql.connector.connect(host=host, user=user, password=password)
            temp_cursor = temp_conn.cursor()
            temp_cursor.execute("CREATE DATABASE IF NOT EXISTS gemini_cli")
            print("✅ Database 'gemini_cli' criado/verificado!")
            temp_cursor.close()
            temp_conn.close()
        except Error as e:
            print(f"❌ Erro ao criar database: {e}")

    def setup_tables(self):
        """Cria as tabelas necessárias"""
        queries = [
            """
            CREATE TABLE IF NOT EXISTS conversations (
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS messages (
                id INT AUTO_INCREMENT PRIMARY KEY,
                conversation_id INT,
                role ENUM('user', 'assistant'),
                content TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (conversation_id)
                    REFERENCES conversations(id) ON DELETE CASCADE
            )
            """,
        ]

        try:
            for query in queries:
                self.cursor.execute(query)
            self.connection.commit()
            print("✅ Tabelas criadas com sucesso!")
        except Error as e:
            print(f"❌ Erro ao criar tabelas: {e}")

    def save_message(self, conversation_id, role, content):
        """Salva uma mensagem no banco"""
        try:
            query = (
                "INSERT INTO messages (conversation_id, role, content) "
                "VALUES (%s, %s, %s)"
            )
            self.cursor.execute(query, (conversation_id, role, content))
            self.connection.commit()
            return self.cursor.lastrowid
        except Error as e:
            print(f"❌ Erro ao salvar mensagem: {e}")
            return None

    def create_conversation(self, title="Nova Conversa"):
        """Cria uma nova conversa"""
        try:
            query = "INSERT INTO conversations (title) VALUES (%s)"
            self.cursor.execute(query, (title,))
            self.connection.commit()
            return self.cursor.lastrowid
        except Error as e:
            print(f"❌ Erro ao criar conversa: {e}")
            return None

    def get_conversation_history(self, conversation_id):
        """Recupera histórico de uma conversa"""
        try:
            query = """
                SELECT role, content, created_at
                FROM messages
                WHERE conversation_id = %s
                ORDER BY created_at ASC
            """
            self.cursor.execute(query, (conversation_id,))
            return self.cursor.fetchall()
        except Error as e:
            print(f"❌ Erro ao buscar histórico: {e}")
            return []

    def list_conversations(self):
        """Lista todas as conversas"""
        try:
            query = """
                SELECT c.id, c.title, c.created_at,
                       COUNT(m.id) as message_count
                FROM conversations c
                LEFT JOIN messages m ON c.id = m.conversation_id
                GROUP BY c.id
                ORDER BY c.created_at DESC
            """
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except Error as e:
            print(f"❌ Erro ao listar conversas: {e}")
            return []

    def close(self):
        """Fecha a conexão"""
        if self.cursor:
            self.cursor.close()
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("🔌 Conexão fechada!")


# Exemplo de uso
if __name__ == "__main__":
    db = DatabaseManager()

    # 1. Criar database
    db.create_database()

    # 2. Conectar
    if db.connect():
        # 3. Criar tabelas
        db.setup_tables()

        # 4. Testar criando uma conversa
        conv_id = db.create_conversation("Minha primeira conversa")

        if conv_id:
            # 5. Salvar mensagens
            db.save_message(conv_id, "user", "Olá Gemini!")

            # Chat com Gemini
            response = model.generate_content("Olá! Responda brevemente.")
            db.save_message(conv_id, "assistant", response.text)

            # 6. Mostrar histórico
            print("\n📜 Histórico da conversa:")
            history = db.get_conversation_history(conv_id)
            for msg in history:
                print(f"{msg['role'].upper()}: {msg['content']}")

            # 7. Listar conversas
            print("\n📋 Todas as conversas:")
            convs = db.list_conversations()
            for conv in convs:
                print(
                    f"ID: {conv['id']} | {conv['title']} | "
                    f"Mensagens: {conv['message_count']}"
                )

        db.close()
