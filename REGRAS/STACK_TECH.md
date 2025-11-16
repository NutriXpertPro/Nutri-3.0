# Stack Tecnológico - Nutri Xpert Pro

## 🏗️ Arquitetura Definida

**Framework Principal**: Django + Django ORM + MariaDB

## 📚 Tecnologias Utilizadas

### Backend
- **Django 5.2.7** - Framework web principal
- **Django REST Framework** - APIs REST
- **Django ORM** - Mapeamento objeto-relacional
- **MariaDB** - Banco de dados principal
- **PyMySQL** - Driver de conexão Python-MariaDB

### Frontend
- **Django Templates** - Sistema de templates
- **HTMX** - Interações dinâmicas sem JavaScript complexo
- **Tailwind CSS** - Framework CSS utilitário
- **Chart.js** - Gráficos e visualizações

### Autenticação
- **Django Auth** - Sistema de autenticação nativo
- **JWT (djangorestframework-simplejwt)** - Tokens para API

### Desenvolvimento
- **django-browser-reload** - Reload automático em desenvolvimento
- **django-tailwind** - Integração Tailwind com Django

## 🗄️ Configuração de Banco

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nutri_xpert_pro',
        'USER': 'nutri_user',
        'PASSWORD': 'nutri_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

## 📁 Estrutura de Apps Django

- **users** - Gerenciamento de usuários e autenticação
- **patients** - Perfis e dados de pacientes
- **anamnesis** - Fichas de anamnese
- **evaluations** - Avaliações corporais e fotos
- **diets** - Planejamento e gestão de dietas
- **appointments** - Agendamentos e consultas
- **payments** - Processamento de pagamentos
- **notifications** - Sistema de notificações
- **messages** - Mensagens internas
- **lab_exams** - Exames laboratoriais
- **theme** - Configurações de tema e CSS

## 🚫 Tecnologias Removidas

- **FastAPI** - Removido (Django REST Framework suficiente)
- **SQLAlchemy** - Removido (Django ORM utilizado)
- **SQLite** - Removido (MariaDB como banco principal)
- **Alembic** - Removido (Django Migrations utilizado)

## 🔧 Scripts de Desenvolvimento

```bash
# Instalar dependências
pip install -r requirements.txt
npm install

# Desenvolvimento
npm run dev  # Inicia Django + Tailwind watch

# Migrações
npm run migrate  # Executa makemigrations + migrate

# Build para produção
npm run build  # Compila CSS para produção
```

## 📦 Dependências Principais

### Python (requirements.txt)
- Django==5.2.7
- djangorestframework==5.15.1
- PyMySQL==1.1.0
- mysqlclient==2.2.4
- Pillow==12.0.0

### Node.js (package.json)
- tailwindcss==4.1.14
- npm-run-all==4.1.5

## ✅ Vantagens da Arquitetura Escolhida

1. **Simplicidade** - Um framework principal (Django)
2. **Consistência** - ORM único para todo o projeto
3. **Maturidade** - Stack consolidado e bem documentado
4. **Escalabilidade** - MariaDB suporta crescimento
5. **Manutenibilidade** - Menos complexidade arquitetural
6. **Comunidade** - Grande suporte da comunidade Django

---

**Esta é a arquitetura oficial do projeto. Todas as implementações devem seguir este stack.**