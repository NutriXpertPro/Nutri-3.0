# Checklist - Nutri Xpert Pro (Visão do Produto)

## Etapa 1: Fundação Técnica (CONCLUÍDA)

- [x] 1.1: Decidir stack de tecnologia (Django, HTMX, Tailwind CSS, MariaDB).
- [x] 1.2: Criar projeto Django e todos os 8 apps.
- [x] 1.3: Criar todos os 8 modelos de dados (`User`, `Patient`, etc.).
- [x] 1.4: Configurar `settings.py` (apps, `AUTH_USER_MODEL`).
- [x] 1.5: Resetar e recriar o banco de dados com a estrutura final.
- [x] 1.6: Registrar todos os modelos no painel de Admin do Django.

## Etapa 2: Layout Global e Configurações (Próximos Passos)

- [x] 2.1: Instalar e configurar o Tailwind CSS no projeto.
- [x] 2.2: Criar os templates base do projeto (ex: `base.html` com menu lateral e topo).
- [x] 2.3: Configurar a API (Django REST Framework) e a autenticação por Token (JWT).

## Etapa 3: Construção do "Dashboard do Nutricionista" (Tela Principal)

- [x] 3.1: Criar a View e o Template principal para o Dashboard.
- [x] 3.2: **Bloco "Meus Pacientes"**:
    - [x] Criar a API para listar e buscar pacientes.
    - [x] Integrar a lista de pacientes no Dashboard.
    - [x] Adicionar busca e paginação com HTMX (sem recarregar a página).
- [x] 3.3: **Bloco "Notificações"**:
    - [x] Criar a API para buscar notificações não lidas.
    - [x] Integrar um resumo das notificações no Dashboard.

## Etapa 4: Autenticação e Fluxos de Usuário

- [ ] 4.1: **Estrutura de Usuários:**
    - [x] Estender o modelo de usuário (`User`) com um campo `user_type` (Nutricionista/Paciente).
    - [x] Definir as novas URLs para login/cadastro (`/login/nutricionista/`, etc.).
- [ ] 4.2: **Fluxo do Nutricionista:**
    - [ ] Criar as páginas de Cadastro e Login do Nutricionista.
    - [ ] Implementar a lógica de "pagamento pendente" para liberar o acesso.
    - [ ] Configurar o envio de email de boas-vindas após a confirmação do pagamento.
- [ ] 4.3: **Fluxo do Paciente:**
    - [ ] Implementar a funcionalidade para o nutricionista convidar/cadastrar pacientes.
    - [ ] Criar a página de login profissional para o paciente.
    - [ ] Criar a view e o template para o dashboard do paciente.
- [ ] 4.4: **Conectar Página Inicial:**
    - [ ] Atualizar os links dos botões "Sou Nutricionista" e "Sou Paciente".

## Etapa 5: Construção da Subpágina "Detalhes do Paciente"

- [ ] 5.1: Criar a View e o Template para a página de detalhes de um paciente.
- [ ] 5.2: **Bloco "Anamnese"**:
    - [ ] Criar a API para buscar os dados da anamnese do paciente.
    - [ ] Exibir os dados da anamnese na tela.
- [ ] 5.3: **Bloco "Histórico de Avaliações"**:
    - [ ] Criar a API para o histórico de avaliações.
    - [ ] Exibir a lista de avaliações passadas.
    - [ ] Integrar uma biblioteca de gráficos (Chart.js) para os gráficos de evolução.
- [ ] 5.4: **Bloco "Nova Avaliação"**:
    - [ ] Criar o formulário para adicionar uma nova avaliação.
    - [ ] Implementar o envio do formulário com HTMX.

## Etapa 6: Construção da Subpágina "Gestão de Dietas"

- [ ] 6.1: Criar a View e o Template para a criação/edição de dietas.
- [ ] 6.2: Criar a API para salvar e carregar os dados de uma dieta.
- [ ] 6.3: Implementar a funcionalidade de gerar o PDF da dieta.

## Etapa 7: Funcionalidades Adicionais

- [ ] 7.1: **Agendamentos:** Implementar a API e a interface do calendário.
- [ ] 7.2: **Pagamentos:** Integrar com a API da Asaas.
- [ ] 7.3: **Tarefas Automáticas:** Configurar o Celery/Redis para o envio de e-mails agendados.

## Etapa 8: Finalização

- [ ] 8.1: Escrever testes para as principais funcionalidades.
- [ ] 8.2: Preparar o projeto para o ambiente de produção.