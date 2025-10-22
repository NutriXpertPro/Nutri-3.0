# PRD - Nutri Xpert Pro

## 1. Visão Geral do Produto  
O Nutri Xpert Pro é uma plataforma destinada a nutricionistas e pacientes, com o objetivo de centralizar e automatizar o acompanhamento nutricional, oferecendo uma experiência personalizada e escalável para a criação de dietas, monitoramento de progresso e gestão de avaliações.

### 1.1. Objetivo:  
Criar uma plataforma para nutricionistas que centralize _anamneses, **painel de clientes, **avaliações quinzenais (com fotos e gráficos de evolução)_ e _gestão de dietas_, otimizada para dispositivos móveis, tablets e PCs.

### 1.2. MVP:

- Ficha de _Anamnese_.
- _Painel de Clientes_.
- _Avaliação Quinzenal Básica_ (peso, medidas e fotos).
- _Banco de Alimentos_ e _Dietas_ personalizadas.
- _Exportação de relatórios PDF_.

---

## 2. Funcionalidades do Sistema

### 2.1. Gestão de Usuários, Autenticação e Papéis

#### 2.1.1. _Modelo de Usuário Unificado_
- O sistema utilizará um modelo de usuário único para todas as entidades que necessitam de autenticação (Administradores, Nutricionistas, Pacientes).
- Um campo `user_type` diferenciará os papéis e controlará as permissões de acesso.

#### 2.1.2. _Fluxo de Cadastro e Login do Nutricionista_
- **Cadastro:** Nutricionistas se cadastrarão através de um formulário próprio (email, senha, nome). Após o cadastro, a conta ficará pendente de aprovação de pagamento.
- **Login:** Acesso via email e senha a uma página de login específica para nutricionistas.
- **Aprovação:** O acesso ao dashboard principal será concedido após a confirmação do pagamento da assinatura, que pode ser aprovada manualmente pelo Superusuário.

#### 2.1.3. _Fluxo de Cadastro e Login do Paciente_
- **Cadastro:** O paciente não se cadastra diretamente. Ele é convidado ou cadastrado pelo seu nutricionista responsável através do dashboard do nutricionista. Neste momento, uma conta de usuário do tipo "paciente" é criada para ele.
- **Login:** O paciente usará seu email e uma senha (definida no momento do convite/cadastro) para acessar seu próprio dashboard através de uma página de login profissional.

### 2.2. Gestão de Pacientes

#### 2.2.1. _Criação de Pacientes_
- O nutricionista pode criar um novo paciente em seu dashboard.
- Ao criar um paciente, o sistema irá:
    1. Criar um novo registro na tabela de `users` com `user_type = 'paciente'`, definindo o email e uma senha inicial para o paciente.
    2. Criar um `patient_profile` associado a este novo usuário, contendo informações adicionais (data de nascimento, telefone, etc.).
    3. Vincular o perfil do paciente ao nutricionista responsável.
- Isso garante que cada paciente tenha suas próprias credenciais de login e um perfil de dados separado.

#### 2.2.2. _Atendimento Presencial ou Virtual_:

- O _atendimento presencial_ ocorre no consultório, e o nutricionista preenche a _Ficha de Anamnese_ junto ao paciente.
- O _atendimento virtual_ pode ser feito de forma online, com o paciente preenchendo o formulário da anamnese _online_ e enviando para o nutricionista via _email_ ou link do sistema.

### 2.3. Avaliação Quinzenal  
#### 2.3.1. _Avaliação Virtual: Envio automático de email quinzenal solicitando o preenchimento de um novo formulário com \*\*peso, medidas (pescoço, cintura e quadril) e 3 fotos_ (frente, lado e costas).

- O formulário será enviado a cada 15 dias.
- Caso o paciente não envie, o _nutricionista será notificado_ no painel de trabalho para que possa agir.

#### 2.3.2. _Avaliação Presencial: O nutricionista escolhe se a avaliação será \*\*presencial_ de acordo com o reagendamento. O histórico será atualizado de acordo com a data da consulta.

#### 2.3.3. _Histórico de Avaliações: A cada avaliação, as \*\*fotos_ e _medidas_ do paciente serão _atualizadas_ e armazenadas no histórico, com as colagens de fotos comparando a primeira entrega e a mais recente para visualização do progresso.

#### 2.3.4. _Gráficos: Gráficos de \*\*peso_ e _medidas_ serão gerados automaticamente com base nas avaliações, permitindo um acompanhamento visual da evolução do paciente.

### 2.4. Banco de Alimentos e Dietas  
#### 2.4.1. _Tabela TACo: O banco de alimentos usará a \*\*Tabela TACo_ para gerar as dietas personalizadas. O banco conterá alimentos com informações nutricionais (calorias, macronutrientes, etc.).

#### 2.4.2. _Dietas Automatizadas_:

- O sistema será capaz de sugerir dietas personalizadas com até _10 refeições_.
- O nutricionista poderá ajustar as _substituições de carboidratos e proteínas principais_ de cada refeição, usando dados do banco de alimentos.

#### 2.4.3. _Geração de Dieta_: As dietas serão geradas com base nas necessidades energéticas (TMB, fator de atividade) do paciente.

### 2.5. Relatórios  
#### 2.5.1. _Exportação em PDF: O nutricionista poderá exportar relatórios com o histórico de avaliações do paciente, \*\*fotos e gráficos de evolução_, e a dieta atualizada. Os relatórios poderão ser enviados diretamente para o paciente.

### 2.6. Notificações  
#### 2.6.1. _Notificação de Pendências: Caso o paciente não entregue o formulário de avaliação quinzenal (fotos, peso e medidas), uma \*\*notificação_ será gerada na área de trabalho do nutricionista.

### 2.7. Segurança e Privacidade  
#### 2.7.1. _LGPD_: O sistema será em conformidade com a Lei Geral de Proteção de Dados (LGPD). Os dados dos pacientes serão criptografados e acessíveis apenas pelo nutricionista responsável.

#### 2.7.2. _Autenticação: Utilização de JWT (JSON Web Tokens) ou bibliotecas como Authlib para autenticação de usuários, com controle de permissões para nutricionistas e pacientes.

#### 2.7.3. Gerenciamento de Assinaturas

- Nutricionistas devem assinar um plano para acessar funcionalidades completas.
- Suporte a pagamentos recorrentes (Cartão de Crédito, Pix, Débito).
- Processo de aprovação (manual/automático) para novos nutricionistas após pagamento.
- Gestão de status de assinatura (ativa, pendente, cancelada) com restrição de acesso.
- Notificações de vencimento/falha de pagamento.

### 2.8. Tecnologias Utilizadas  
#### 2.8.1. _Front-end_: Streamlit ou Dash (para interfaces web interativas em Python), otimizado para dispositivos móveis, tablets e PCs, com suporte a templates responsivos via Bootstrap ou similar.  
#### 2.8.2. _Back-end_: FastAPI ou Django com Python 3.x, para APIs otimizadas de baixa latência e processamento assíncrono.  
#### 2.8.3. _Banco de Dados_: MariaDB (com Docker ou serviço gerenciado) e Django ORM para queries e segurança.  
#### 2.8.4. _Armazenamento de Arquivos_: AWS S3 ou MinIO + CDN (Cloudflare/ImageKit).  
#### 2.8.5. _Fila / Jobs_: Celery com Redis ou RQ para processamento de imagens e geração de thumbnails.  
#### 2.8.6. _Gráficos_: Plotly ou Matplotlib para geração de gráficos dinâmicos, integrados ao front-end.  
#### 2.8.7. _CI/CD_: GitHub + GitHub Actions para deploy contínuo e migrações de banco de dados via Alembic ou Django migrations.

### 2.9. Interfaces e Usabilidade  
#### 2.9.1. _Painel de Controle do Nutricionista_:

- Visualização do _histórico de fotos, \*\*gráficos_ e _medidas_.
- Acesso fácil para criar, editar e visualizar _dietas_ e _relatórios_.
- _Notificação de pendências_ para pacientes com avaliações não entregues.

#### 2.9.2. _Interface do Paciente_:

- Acesso ao _formulário de anamnese, \*\*avaliações quinzenais_ e _histórico de evolução_.
- Envio de _fotos e medidas_ para o nutricionista.

---

### 2.10. Administração do Sistema (Superusuário)

#### 2.10.1. Papel do Superusuário
- O sistema contará com um papel de **Superusuário** (Super Admin), que terá acesso irrestrito a todos os dados e funcionalidades da plataforma através do painel de administração do Django (`/admin/`).
- Este usuário é destinado ao administrador principal do sistema.

#### 2.10.2. Funcionalidades do Superusuário
- **Gestão de Acesso:** O superusuário terá a capacidade de aprovar manualmente o acesso de novos nutricionistas à plataforma (por exemplo, após a confirmação de um pagamento), alterando o status de suas contas.
- **Gestão de Cupons de Desconto:** O superusuário poderá criar, gerenciar e distribuir cupons de desconto para os planos de assinatura dos nutricionistas.

---

## 3. Roadmap

### 3.1. Fase 1 - MVP  
#### 3.1.1. _Cadastro e login_.  
#### 3.1.2. _Ficha de anamnese_ (presencial e online).  
#### 3.1.3. _Avaliação quinzenal (virtual)_.  
#### 3.1.4. _Banco de alimentos e dietas_.  
#### 3.1.5. _Relatórios PDF_.  
#### 3.1.6. _Notificações_.  
#### 3.1.7. _Histórico de avaliações_.

### 3.2. Fase 2 - Pós-MVP  
#### 3.2.1. _Avaliação presencial com reagendamento_.  
#### 3.2.2. _Gráficos dinâmicos_.  
#### 3.2.3. _Integração com API de suplementos (opcional)_.  
#### 3.2.4. _Funcionalidade de exportação de PDF personalizada_.
#### 3.2.5. _Sugestão de Dietas por IA_:

- Análise de perfil do paciente (anamnese, exames, objetivos) para sugerir modelos de dieta.
- Indicação de suplementos e manipulados com base na análise da IA.
- Nutricionista poderá avaliar, editar ou ignorar as sugestões da IA.

---

Este PRD agora inclui a _avaliação presencial com reagendamento, a \*\*Tabela TACo_ corretamente inserida, o _histórico de fotos e gráficos_ para cada paciente e as _notificações automáticas_ de pendências. As adaptações para Python foram realizadas principalmente na seção de tecnologias, substituindo o stack JavaScript por equivalentes em Python, mantendo a funcionalidade e escalabilidade originais.