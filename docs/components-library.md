# Biblioteca de Componentes - NutriXpert Pro

## 📚 Visão Geral

Esta biblioteca contém todos os componentes reutilizáveis extraídos do Design System do NutriXpert Pro Dashboard.

## 🧩 Componentes Disponíveis

### 1. Botões

#### Uso Básico
```html
{% include 'components/button.html' with variant='primary' text='Salvar' %}
```

#### Variações
- **Primary**: Ação principal (azul)
- **Secondary**: Ação secundária (cinza)
- **AI**: Funcionalidades de IA (roxo/azul)
- **Success**: Ações positivas (verde)
- **Warning**: Avisos (amarelo)
- **Danger**: Ações destrutivas (vermelho)
- **Ghost**: Transparente

#### Tamanhos
- **sm**: Pequeno
- **base**: Padrão
- **lg**: Grande

#### Exemplos
```html
<!-- Botão primário com ícone -->
{% include 'components/button.html' with variant='primary' text='Nova Consulta' icon='fas fa-plus' size='base' %}

<!-- Botão link -->
{% include 'components/button.html' with variant='secondary' text='Ver Mais' href='/patients/' %}

<!-- Botão AI -->
{% include 'components/button.html' with variant='ai' text='Gerar Insight' icon='fas fa-brain' onclick='generateInsight()' %}

<!-- Botão de largura completa -->
{% include 'components/button.html' with variant='success' text='Confirmar' full_width=True %}
```

---

### 2. Cards

#### Uso Básico
```html
{% include 'components/card.html' with title='Título do Card' %}
    <p>Conteúdo aqui</p>
{% endinclude %}
```

#### Parâmetros
- **title**: Título do card
- **icon**: Ícone FontAwesome para o título
- **action_text**: Texto do link de ação
- **action_href**: URL do link
- **padding**: sm|base|lg

#### Exemplos
```html
<!-- Card com título e ação -->
{% include 'components/card.html' with title='Pacientes Recentes' icon='fas fa-users' action_text='Ver todos' action_href='/patients/' %}
    <div class="space-y-3">
        <!-- Lista de pacientes -->
    </div>
{% endinclude %}

<!-- Card sem hover -->
{% include 'components/card.html' with title='Informações' hover=False padding='sm' %}
    <p class="text-sm">Dados estáticos</p>
{% endinclude %}
```

---

### 3. Stat Cards (Cards de Estatística)

#### Uso Básico
```html
{% include 'components/stat_card.html' with label='Pacientes Ativos' value='125' icon='fas fa-users' %}
```

#### Parâmetros
- **label**: Rótulo da métrica
- **value**: Valor principal
- **icon**: Ícone FontAwesome
- **icon_variant**: default|success|warning|danger|ai
- **trend**: up|down|neutral
- **trend_value**: Valor da tendência (ex: "12%")
- **footer_text**: Texto adicional
- **ai_insight**: Insight de IA

#### Exemplos
```html
<!-- Stat card com tendência positiva -->
{% include 'components/stat_card.html' with 
    label='Consultas Hoje' 
    value='8' 
    icon='fas fa-calendar-check' 
    icon_variant='success'
    trend='up' 
    trend_value='+15%'
    footer_text='3 novos agendamentos' %}

<!-- Stat card com insight de IA -->
{% include 'components/stat_card.html' with 
    label='Taxa de Adesão' 
    value='87%' 
    icon='fas fa-chart-line' 
    icon_variant='ai'
    ai_insight='Pacientes com dieta low-carb apresentam 92% de adesão' %}
```

---

### 4. Timeline Items

#### Uso Básico
```html
{% include 'components/timeline_item.html' with time='14:30' patient_name='João Silva' note='Consulta de retorno' %}
```

#### Parâmetros
- **time**: Horário (obrigatório)
- **date**: Data (opcional)
- **patient_name**: Nome do paciente
- **note**: Observação/descrição
- **avatar_url**: URL da foto
- **patient_id**: ID para avatar automático
- **tags**: Lista de tags
- **actions**: Lista de ações

#### Exemplo Completo
```html
{% include 'components/timeline_item.html' with 
    time='09:30' 
    date='15/11'
    patient_name='Maria Silva'
    note='Primeira consulta - Avaliação completa'
    patient_id='123'
    tags=timeline_tags
    actions=timeline_actions %}
```

#### Tags e Ações (no context do Django)
```python
# No seu view
timeline_tags = [
    {'text': 'Online', 'type': 'online', 'icon': 'fas fa-video'},
    {'text': '60 min', 'type': 'duration', 'icon': 'fas fa-clock'},
    {'text': 'IA: Verificar glicose', 'type': 'ai', 'icon': 'fas fa-brain'}
]

timeline_actions = [
    {'icon': 'fas fa-phone', 'onclick': 'startCall("123")', 'title': 'Iniciar chamada'},
    {'icon': 'fas fa-comment', 'onclick': 'openChat("123")', 'title': 'Abrir chat', 'variant': 'ai'}
]
```

---

### 5. Form Inputs

#### Uso Básico
```html
{% include 'components/form_input.html' with name='email' label='Email' type='email' %}
```

#### Tipos Suportados
- text, email, password, number, tel, url, search

#### Parâmetros
- **name**: Nome do campo
- **label**: Rótulo
- **type**: Tipo do input
- **placeholder**: Texto de exemplo
- **value**: Valor inicial
- **required**: Campo obrigatório
- **icon**: Ícone FontAwesome
- **help_text**: Texto de ajuda
- **error**: Mensagem de erro

#### Exemplos
```html
<!-- Input com ícone e validação -->
{% include 'components/form_input.html' with 
    name='email' 
    label='Email' 
    type='email' 
    icon='fas fa-envelope'
    placeholder='seu@email.com'
    required=True
    help_text='Usaremos este email para contato' %}

<!-- Input com erro -->
{% include 'components/form_input.html' with 
    name='peso' 
    label='Peso (kg)' 
    type='number' 
    icon='fas fa-weight'
    value='75'
    error='Peso deve ser entre 30 e 300 kg' %}
```

---

### 6. Modais

#### Uso Básico
```html
{% include 'components/modal.html' with id='meuModal' title='Título do Modal' %}
    <p>Conteúdo do modal aqui</p>
{% endinclude %}
```

#### Parâmetros
- **id**: ID único do modal
- **title**: Título
- **size**: sm|base|lg|xl
- **close_button**: Mostrar botão fechar
- **backdrop_close**: Fechar ao clicar fora

#### Controle via JavaScript
```javascript
// Abrir modal
openModal('meuModal');

// Fechar modal
closeModal('meuModal');
```

#### Exemplo Completo
```html
{% include 'components/modal.html' with id='patientModal' title='Detalhes do Paciente' size='lg' %}
    <div class="grid grid-cols-2 gap-4">
        <div>
            <h4>Informações Básicas</h4>
            <p><strong>Nome:</strong> João Silva</p>
            <p><strong>Idade:</strong> 32 anos</p>
        </div>
        <div>
            <h4>Métricas</h4>
            <p><strong>IMC:</strong> 24.5</p>
            <p><strong>Peso:</strong> 75kg</p>
        </div>
    </div>
    
    <div class="mt-6 flex gap-3">
        {% include 'components/button.html' with variant='primary' text='Editar' %}
        {% include 'components/button.html' with variant='secondary' text='Fechar' onclick='closeModal("patientModal")' %}
    </div>
{% endinclude %}
```

---

## 🎨 Sistema de Classes CSS

### Layout
```css
.dashboard          /* Container principal do dashboard */
.main-content       /* Área principal (com margem da sidebar) */
.stats-grid         /* Grid responsivo para stat cards */
.main-grid          /* Grid 2fr 1fr responsivo */
.analytics-grid     /* Grid para gráficos e analytics */
.grid-responsive    /* Grid auto-fit responsivo */
```

### Componentes
```css
.btn                /* Botão base */
.btn-primary        /* Botão primário */
.btn-secondary      /* Botão secundário */
.btn-ai             /* Botão IA */
.card               /* Card base */
.stat-card          /* Card de estatística */
.form-input         /* Input de formulário */
.icon-btn           /* Botão apenas com ícone */
```

### Utilitários
```css
.clickable          /* Adiciona cursor pointer e hover */
.hover-lift         /* Efeito de elevação no hover */
.animate-pulse      /* Animação de pulse */
.loading-spinner    /* Spinner de carregamento */
.status-dot         /* Ponto de status */
.notification-badge /* Badge de notificação */
```

---

## 🚀 Exemplos de Uso em Páginas

### Dashboard Principal
```html
{% extends 'base_design_system.html' %}

{% block content %}
<div class="dashboard">
    <!-- Stats Grid -->
    <div class="stats-grid">
        {% include 'components/stat_card.html' with label='Pacientes Ativos' value=total_patients icon='fas fa-users' trend='up' trend_value='8%' %}
        {% include 'components/stat_card.html' with label='Consultas Hoje' value=consultas_hoje icon='fas fa-calendar' icon_variant='success' %}
    </div>
    
    <!-- Main Grid -->
    <div class="main-grid">
        <!-- Agenda -->
        {% include 'components/card.html' with title='Agenda do Dia' icon='fas fa-calendar-alt' %}
            <div class="timeline">
                {% for appointment in appointments_today %}
                    {% include 'components/timeline_item.html' with time=appointment.time patient_name=appointment.patient.name %}
                {% endfor %}
            </div>
        {% endinclude %}
        
        <!-- Paciente em Foco -->
        {% include 'components/card.html' with title='Paciente em Foco' icon='fas fa-star' %}
            <!-- Conteúdo do paciente -->
        {% endinclude %}
    </div>
</div>
{% endblock %}
```

### Formulário de Paciente
```html
{% extends 'base_design_system.html' %}

{% block content %}
<div class="dashboard">
    {% include 'components/card.html' with title='Novo Paciente' icon='fas fa-user-plus' %}
        <form method="post">
            {% csrf_token %}
            
            <div class="grid grid-cols-2 gap-4">
                {% include 'components/form_input.html' with name='name' label='Nome Completo' icon='fas fa-user' required=True %}
                {% include 'components/form_input.html' with name='email' label='Email' type='email' icon='fas fa-envelope' %}
            </div>
            
            <div class="grid grid-cols-3 gap-4">
                {% include 'components/form_input.html' with name='weight' label='Peso (kg)' type='number' icon='fas fa-weight' %}
                {% include 'components/form_input.html' with name='height' label='Altura (cm)' type='number' icon='fas fa-ruler' %}
                {% include 'components/form_input.html' with name='age' label='Idade' type='number' icon='fas fa-birthday-cake' %}
            </div>
            
            <div class="flex gap-3 mt-6">
                {% include 'components/button.html' with variant='primary' text='Salvar Paciente' icon='fas fa-save' type='submit' %}
                {% include 'components/button.html' with variant='secondary' text='Cancelar' href='/patients/' %}
            </div>
        </form>
    {% endinclude %}
</div>
{% endblock %}
```

---

## 📱 Responsividade

Todos os componentes são responsivos por padrão:

- **Mobile**: Layout em coluna única
- **Tablet**: Layout adaptado com 2 colunas
- **Desktop**: Layout completo

### Classes Utilitárias Responsivas
```html
<div class="hidden-mobile">Oculto no mobile</div>
<div class="mobile-only">Apenas mobile</div>
<div class="desktop-only">Apenas desktop</div>
```

---

## 🎯 Boas Práticas

### 1. Sempre Use Componentes
```html
<!-- ❌ Não faça isso -->
<button class="bg-blue-500 text-white px-4 py-2">Botão</button>

<!-- ✅ Faça isso -->
{% include 'components/button.html' with variant='primary' text='Botão' %}
```

### 2. Consistência de Ícones
```html
<!-- Use sempre FontAwesome 6.4.0 -->
<i class="fas fa-users"></i>     <!-- ✅ Correto -->
<i class="fa fa-users"></i>      <!-- ❌ Versão antiga -->
```

### 3. Acessibilidade
```html
<!-- Sempre inclua labels em formulários -->
{% include 'components/form_input.html' with name='email' label='Email' %}

<!-- Use títulos descritivos em modais -->
{% include 'components/modal.html' with title='Editar Informações do Paciente' %}
```

### 4. Performance
```html
<!-- Carregue apenas componentes necessários -->
<!-- Use lazy loading para modais pesados -->
```

---

## 🔄 Versionamento

### Versão Atual: 1.0.0

#### Alterações Futuras
- Novos componentes serão adicionados sem quebrar os existentes
- Mudanças breaking terão nova versão major
- Documentação sempre atualizada

---

## 📞 Suporte

Para dúvidas sobre componentes:
1. Consulte esta documentação
2. Veja os exemplos práticos
3. Teste no ambiente de desenvolvimento
4. Mantenha sempre atualizado

**💡 Dica:** Use o DevTools do navegador para inspecionar componentes em produção e entender sua estrutura.