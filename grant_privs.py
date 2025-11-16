#!/usr/bin/env python3
"""
Script para conceder privilégios adicionais ao usuário nutri_user
Usado principalmente para testes que necessitam criar/dropar bancos
"""

import pymysql
from decouple import config


def grant_test_privileges():
    """Concede privilégios para criar/dropar bancos de dados de teste"""
    
    try:
        # Conecta como root
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password=config('DB_ROOT_PASSWORD', default=''),
            charset='utf8mb4'
        )
        
        with connection.cursor() as cursor:
            # Concede privilégios para testes
            cursor.execute("GRANT CREATE ON *.* TO 'nutri_user'@'localhost'")
            cursor.execute("GRANT DROP ON *.* TO 'nutri_user'@'localhost'")
            cursor.execute("FLUSH PRIVILEGES")
            
            print("✅ Privilégios de teste concedidos!")
            print("   - nutri_user pode criar bancos de dados")
            print("   - nutri_user pode dropar bancos de dados")
            
    except pymysql.Error as e:
        print(f"❌ Erro ao conceder privilégios: {e}")
        return False
    finally:
        if 'connection' in locals():
            connection.close()
    
    return True


if __name__ == "__main__":
    print("🔧 Concedendo privilégios de teste para nutri_user...")
    print("=" * 50)
    
    if grant_test_privileges():
        print("=" * 50)
        print("✅ Privilégios concedidos com sucesso!")
    else:
        print("❌ Falha ao conceder privilégios.")
