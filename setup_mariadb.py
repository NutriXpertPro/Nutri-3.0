#!/usr/bin/env python3
"""
Script para configurar o banco de dados MariaDB do Nutri Xpert Pro
Execute este script antes de rodar as migrações Django
"""

import pymysql
from decouple import config
import sys


def create_database():
    """Cria o banco de dados e usuário se não existirem"""
    
    try:
        # Conecta como root
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password=config('DB_ROOT_PASSWORD', default=''),
            charset='utf8mb4'
        )
        
        with connection.cursor() as cursor:
            # Cria o banco de dados
            cursor.execute("CREATE DATABASE IF NOT EXISTS nutri_xpert_pro CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
            print("✅ Banco de dados 'nutri_xpert_pro' criado com sucesso!")
            
            # Remove usuário se existir e recria
            cursor.execute("DROP USER IF EXISTS 'nutri_user'@'localhost'")
            cursor.execute("CREATE USER 'nutri_user'@'localhost' IDENTIFIED BY 'nutri_password'")
            
            # Concede privilégios
            cursor.execute("GRANT ALL PRIVILEGES ON nutri_xpert_pro.* TO 'nutri_user'@'localhost'")
            cursor.execute("GRANT CREATE, DROP ON *.* TO 'nutri_user'@'localhost'")  # Para testes
            cursor.execute("FLUSH PRIVILEGES")
            
            print("✅ Usuário 'nutri_user' criado e privilégios concedidos!")
            
    except pymysql.Error as e:
        print(f"❌ Erro ao configurar banco de dados: {e}")
        sys.exit(1)
    finally:
        if 'connection' in locals():
            connection.close()


def test_connection():
    """Testa a conexão com o banco usando as credenciais do Django"""
    
    try:
        connection = pymysql.connect(
            host='localhost',
            user='nutri_user',
            password='nutri_password',
            database='nutri_xpert_pro',
            charset='utf8mb4'
        )
        
        with connection.cursor() as cursor:
            cursor.execute("SELECT VERSION()")
            version = cursor.fetchone()[0]
            print(f"✅ Conexão testada com sucesso! MariaDB versão: {version}")
            
    except pymysql.Error as e:
        print(f"❌ Erro na conexão de teste: {e}")
        sys.exit(1)
    finally:
        if 'connection' in locals():
            connection.close()


if __name__ == "__main__":
    print("🔧 Configurando banco de dados MariaDB para Nutri Xpert Pro...")
    print("=" * 60)
    
    create_database()
    test_connection()
    
    print("=" * 60)
    print("✅ Configuração concluída!")
    print("📝 Próximos passos:")
    print("   1. Execute: python manage.py makemigrations")
    print("   2. Execute: python manage.py migrate")
    print("   3. Execute: python manage.py createsuperuser")