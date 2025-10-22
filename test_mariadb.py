import pymysql
from pymysql import Error

def testar_conexao_mariadb():
    """
    Testa a conexão com o MariaDB usando PyMySQL
    """
    try:
        # Configurações de conexão - XAMPP MariaDB
        conexao = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='',
            database='nutri_db',
            charset='utf8mb4'
        )
        
        print("✅ Conexão bem-sucedida com o MariaDB!")
        
        with conexao.cursor() as cursor:
            # Obter versão do servidor
            cursor.execute("SELECT VERSION();")
            versao = cursor.fetchone()
            print(f"📊 Versão do servidor: {versao[0]}")
            
            # Obter banco de dados atual
            cursor.execute("SELECT DATABASE();")
            banco_atual = cursor.fetchone()
            print(f"🗄️  Banco de dados conectado: {banco_atual[0]}")
            
            # Listar tabelas
            cursor.execute("SHOW TABLES;")
            tabelas = cursor.fetchall()
            
            if tabelas:
                print(f"\n📋 Tabelas encontradas ({len(tabelas)}):")
                for tabela in tabelas:
                    print(f"   - {tabela[0]}")
            else:
                print("\n📋 Nenhuma tabela encontrada no banco de dados")
            
    except Error as e:
        print("❌ Erro ao conectar ao MariaDB:")
        print(f"   {e}")
        
    except Exception as e:
        print("❌ Erro inesperado:")
        print(f"   {e}")
        
    finally:
        if 'conexao' in locals():
            conexao.close()
            print("\n🔌 Conexão fechada")

if __name__ == "__main__":
    print("🔍 Testando conexão com MariaDB usando PyMySQL...\n")
    testar_conexao_mariadb()