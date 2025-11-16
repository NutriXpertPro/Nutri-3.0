# Nutri Xpert Pro

Sistema de gestão nutricional para nutricionistas e pacientes, desenvolvido com Django + MariaDB.

## 🏗️ Arquitetura

- **Framework**: Django 5.2.7 + Django REST Framework
- **Banco de Dados**: MariaDB com Django ORM
- **Frontend**: Django Templates + HTMX + Tailwind CSS
- **Autenticação**: Django Auth + JWT

## 🚀 Configuração de Desenvolvimento

### 1. Pré-requisitos

- Python 3.8+
- Node.js 16+
- MariaDB/MySQL
- pip e npm

### 2. Instalação

```bash
# Clone o repositório
git clone <repo-url>
cd nutri-xpert-pro

# Instale dependências Python
pip install -r requirements.txt

# Instale dependências Node.js
npm install

# Configure variáveis de ambiente
cp .env.example .env
# Edite o arquivo .env com suas configurações
```

### 3. Configuração do Banco de Dados

```bash
# Configure o MariaDB (execute como root)
python setup_mariadb.py

# Execute as migrações Django
python manage.py makemigrations
python manage.py migrate

# Crie um superusuário
python manage.py createsuperuser
```

### 4. Executar em Desenvolvimento

```bash
# Inicia Django + Tailwind em modo watch
npm run dev

# Ou separadamente:
python manage.py runserver    # Django na porta 8000
npm run start:tailwind        # Tailwind CSS watch mode
```

### 5. Comandos Úteis

```bash
# Migrações
npm run migrate               # makemigrations + migrate

# Testes
npm run test                 # Executa testes Django

# Build CSS para produção
npm run build

# Privilégios de teste do banco
python grant_privs.py
```

## 📁 Estrutura do Projeto

```
nutri-xpert-pro/
├── setup/                   # Configurações Django
├── users/                   # App de usuários
├── patients/                # App de pacientes
├── anamnesis/               # App de anamnese
├── evaluations/             # App de avaliações
├── diets/                   # App de dietas
├── appointments/            # App de agendamentos
├── payments/                # App de pagamentos
├── notifications/           # App de notificações
├── messages/                # App de mensagens
├── lab_exams/               # App de exames
├── theme/                   # App de tema/CSS
├── templates/               # Templates Django
├── static/                  # Arquivos estáticos
├── REGRAS/                  # Documentação do projeto
└── requirements.txt         # Dependências Python
```

## 🗄️ Banco de Dados

O projeto usa MariaDB com as seguintes tabelas principais:

- `users` - Usuários unificados (admin, nutricionista, paciente)
- `patient_profiles` - Perfis específicos de pacientes
- `anamneses` - Fichas de anamnese
- `evaluations` - Avaliações corporais
- `diets` - Planos alimentares
- `appointments` - Agendamentos
- `payments` - Pagamentos
- `notifications` - Notificações

Ver `REGRAS/SCHEMA.md` para detalhes completos.

## 🔐 Autenticação

O sistema possui três tipos de usuários:

1. **Admin** - Acesso total via /admin/
2. **Nutricionista** - Dashboard principal, gerencia pacientes
3. **Paciente** - Dashboard simplificado, acesso a seus dados

## 📱 Apps Django

### Core Apps
- **users** - Autenticação e gerenciamento de usuários
- **patients** - Gerenciamento de pacientes
- **theme** - Configurações de tema e Tailwind

### Feature Apps  
- **anamnesis** - Fichas de anamnese
- **evaluations** - Avaliações corporais e fotos
- **diets** - Criação e gestão de dietas
- **appointments** - Sistema de agendamentos
- **payments** - Processamento de pagamentos
- **notifications** - Sistema de notificações
- **messages** - Mensagens internas
- **lab_exams** - Gestão de exames laboratoriais

## 🧪 Testes

```bash
# Executar todos os testes
python manage.py test

# Testes de um app específico
python manage.py test users

# Com coverage
pip install coverage
coverage run --source='.' manage.py test
coverage report
```

## 🚀 Deploy

### Produção

1. Configure as variáveis de ambiente de produção
2. Execute `npm run build` para compilar CSS
3. Configure servidor web (nginx/apache)
4. Execute `python manage.py collectstatic`
5. Configure banco de dados de produção
6. Execute migrações em produção

### Docker (Opcional)

```bash
# TODO: Adicionar Dockerfile e docker-compose.yml
```

## 📚 Documentação

- `REGRAS/PRD.md` - Product Requirements Document
- `REGRAS/SCHEMA.md` - Schema do banco de dados
- `REGRAS/CHECKLIST.md` - Checklist de desenvolvimento
- `REGRAS/STACK_TECH.md` - Detalhes do stack tecnológico

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📄 Licença

[Adicionar licença]

## 🆘 Suporte

Para dúvidas e suporte, consulte a documentação em `REGRAS/` ou abra uma issue.