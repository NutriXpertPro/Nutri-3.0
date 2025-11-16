#!/usr/bin/env python3
"""
Script de validação para verificar se a migração para Django + MariaDB foi bem-sucedida
Execute este script após a configuração inicial
"""

import os
import sys
import django
from django.core.management import execute_from_command_line

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from django.db import connection
from django.contrib.auth import get_user_model
from patients.models import PatientProfile
from diets.models import Diet
from anamnesis.models import Anamnesis

def check_database_connection():
    """Verifica conexão com MariaDB"""
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT VERSION()")
            version = cursor.fetchone()[0]
            print(f"✅ Conexão MariaDB: {version}")
            return True
    except Exception as e:
        print(f"❌ Erro na conexão MariaDB: {e}")
        return False

def check_models():
    """Verifica se os modelos Django estão funcionando"""
    try:
        User = get_user_model()
        
        # Conta usuários
        user_count = User.objects.count()
        print(f"✅ Modelo User: {user_count} usuários no banco")
        
        # Conta pacientes  
        patient_count = PatientProfile.objects.count()
        print(f"✅ Modelo PatientProfile: {patient_count} pacientes no banco")
        
        # Conta dietas
        diet_count = Diet.objects.count()
        print(f"✅ Modelo Diet: {diet_count} dietas no banco")
        
        # Conta anamneses
        anamnesis_count = Anamnesis.objects.count()
        print(f"✅ Modelo Anamnesis: {anamnesis_count} anamneses no banco")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro nos modelos Django: {e}")
        return False

def check_migrations():
    """Verifica status das migrações"""
    try:
        from django.core.management import execute_from_command_line
        
        print("📋 Status das migrações:")
        execute_from_command_line(['manage.py', 'showmigrations'])
        return True
        
    except Exception as e:
        print(f"❌ Erro ao verificar migrações: {e}")
        return False

def check_admin():
    """Verifica se o admin Django está acessível"""
    try:
        from django.contrib import admin
        from django.urls import reverse
        
        admin_url = reverse('admin:index')
        print(f"✅ Django Admin: {admin_url}")
        return True
        
    except Exception as e:
        print(f"❌ Erro no Django Admin: {e}")
        return False

def check_rest_framework():
    """Verifica Django REST Framework"""
    try:
        import rest_framework
        print(f"✅ Django REST Framework: v{rest_framework.VERSION}")
        return True
        
    except Exception as e:
        print(f"❌ Erro no Django REST Framework: {e}")
        return False

def main():
    """Executa todas as validações"""
    print("🔍 VALIDAÇÃO DO SETUP - NUTRI XPERT PRO")
    print("=" * 60)
    
    checks = [
        ("Conexão MariaDB", check_database_connection),
        ("Modelos Django", check_models),
        ("Django REST Framework", check_rest_framework),
        ("Django Admin", check_admin),
    ]
    
    passed = 0
    total = len(checks)
    
    for name, check_func in checks:
        print(f"\n🔹 {name}:")
        if check_func():
            passed += 1
        
    print("\n" + "=" * 60)
    print(f"📊 RESULTADO: {passed}/{total} verificações passaram")
    
    if passed == total:
        print("🎉 SUCESSO! Migração para Django + MariaDB concluída!")
        print("\n📝 Próximos passos recomendados:")
        print("   1. Execute: python manage.py createsuperuser")
        print("   2. Execute: npm run dev")
        print("   3. Acesse: http://127.0.0.1:8000/admin/")
        print("   4. Execute testes: npm run test")
    else:
        print("❌ ATENÇÃO: Algumas verificações falharam.")
        print("   Revise a configuração antes de continuar.")
        sys.exit(1)

if __name__ == "__main__":
    main()