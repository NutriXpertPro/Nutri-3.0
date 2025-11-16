# Guia de Migração - Design System NutriXpert Pro

## 📋 Visão Geral

Este guia explica como migrar páginas existentes do NutriXpert Pro para usar o novo Design System padronizado.

## 🚀 Passos para Migração

### 1. Atualizar o Template Base

**ANTES:**
```html
{% extends 'base.html' %}
```

**DEPOIS:**
```html
{% extends 'base_design_system.html' %}
```

### 2. Incluir CSS do Design System

Se você não estiver usando o template base, inclua os arquivos CSS:

```html
<!-- Tokens e Base -->
<link rel="stylesheet" href="{% static 'css/tokens.css' %}">
<link rel="stylesheet" href="{% static 'css/base.css' %}">
<link rel="stylesheet" href="{% static 'css/components.css' %}">
<link rel="stylesheet" href="{% static 'css/utilities.css' %}">

<!-- JavaScript -->
<script src="{% static 'js/design-system.js' %}"></script>
```

### 3. Substituir Botões

**ANTES:**
```html
<button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
    Salvar
</button>
```

**DEPOIS:**
```html
{% include 'components/button.html' with variant='primary' text='Salvar' icon='fas fa-save' %}
```

Ou usando classes diretamente:
```html
<button class="btn btn-primary">
    <i class="fas fa-save"></i>
    Salvar
</button>
```

### 4. Substituir Cards

**ANTES:**
```html
<div class="bg-white shadow rounded-lg p-6">
    <h3 class="text-lg font-semibold mb-4">Título</h3>
    <p>Conteúdo do card</p>
</div>
```

**DEPOIS:**
```html
{% include 'components/card.html' with title='Título' icon='fas fa-info' %}
    <p>Conteúdo do card</p>
{% endinclude %}
```

### 5. Substituir Formulários

**ANTES:**
```html
<div class="mb-4">
    <label class="block text-gray-700 text-sm font-bold mb-2">
        Email
    </label>
    <input class="shadow appearance-none border rounded w-full py-2 px-3" type="email" name="email">
</div>
```

**DEPOIS:**
```html
{% include 'components/form_input.html' with name='email' label='Email' type='email' icon='fas fa-envelope' required=True %}
```

### 6. Atualizar Stats Cards

**ANTES:**
```html
<div class="bg-white rounded-lg shadow p-6">
    <div class="flex items-center">
        <div class="p-3 rounded-full bg-blue-500">
            <i class="fas fa-users text-white"></i>
        </div>
        <div class="ml-4">
            <p class="text-sm text-gray-600">Pacientes</p>
            <p class="text-2xl font-semibold">{{ total_patients }}</p>
        </div>
    </div>
</div>
```

**DEPOIS:**
```html
{% include 'components/stat_card.html' with label='Pacientes Ativos' value=total_patients icon='fas fa-users' trend='up' trend_value='12%' %}
```

### 7. Substituir Modais

**ANTES:**
```html
<div class="fixed inset-0 bg-gray-600 bg-opacity-50 hidden" id="myModal">
    <div class="flex items-center justify-center min-h-screen">
        <div class="bg-white rounded-lg p-6 max-w-md w-full">
            <h3>Título</h3>
            <p>Conteúdo</p>
        </div>
    </div>
</div>
```

**DEPOIS:**
```html
{% include 'components/modal.html' with id='myModal' title='Título' %}
    <p>Conteúdo do modal</p>
{% endinclude %}
```

## 📝 Mapeamento de Classes

### Cores

| ANTES | DEPOIS |
|-------|--------|
| `text-gray-800` | `text-primary` |
| `text-gray-600` | `text-secondary` |
| `text-gray-400` | `text-muted` |
| `bg-blue-500` | `bg-accent` |
| `bg-green-500` | `bg-success` |
| `bg-red-500` | `bg-danger` |
| `bg-yellow-500` | `bg-warning` |

### Espaçamentos

| ANTES | DEPOIS |
|-------|--------|
| `p-2` | `p-2` (mantido) |
| `p-4` | `p-4` (mantido) |
| `p-6` | `p-6` (mantido) |
| `mb-4` | `mb-4` (mantido) |
| `mt-8` | `mt-8` (mantido) |

### Border Radius

| ANTES | DEPOIS |
|-------|--------|
| `rounded` | `rounded` (mantido) |
| `rounded-lg` | `rounded-lg` (mantido) |
| `rounded-xl` | `rounded-xl` (mantido) |
| `rounded-full` | `rounded-full` (mantido) |

### Sombras

| ANTES | DEPOIS |
|-------|--------|
| `shadow` | `shadow-base` |
| `shadow-lg` | `shadow-lg` |
| `shadow-xl` | `shadow-xl` |

## 🎨 Usando Variáveis CSS

### Cores
```css
/* Ao invés de cores fixas */
color: #3b82f6;

/* Use as variáveis */
color: var(--accent);
background: var(--bg-card);
border-color: var(--border);
```

### Espaçamentos
```css
/* Ao invés de valores fixos */
padding: 16px;

/* Use as variáveis */
padding: var(--spacing-4);
margin-bottom: var(--spacing-6);
```

## 📱 Responsividade

### Grid Layouts

**ANTES:**
```html
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
```

**DEPOIS:**
```html
<div class="stats-grid">
<!-- ou -->
<div class="grid-responsive">
```

### Breakpoints
Use as classes utilitárias responsivas:
```html
<div class="hidden-mobile">Oculto no mobile</div>
<div class="mobile-only">Apenas no mobile</div>
<div class="desktop-only">Apenas no desktop</div>
```

## 🔧 JavaScript

### Notificações

**ANTES:**
```javascript
alert('Sucesso!');
```

**DEPOIS:**
```javascript
showSuccess('Sucesso!', 'Operação realizada com sucesso');
showError('Erro!', 'Algo deu errado');
showWarning('Atenção!', 'Verifique os dados');
showInfo('Informação', 'Dados atualizados');
```

### Modais

**ANTES:**
```javascript
$('#myModal').modal('show');
```

**DEPOIS:**
```javascript
openModal('myModal');
closeModal('myModal');
```

### Tema

```javascript
// Alternar tema
toggleTheme();

// Verificar tema atual
const isLightMode = document.body.classList.contains('light-mode');
```

## ✅ Checklist de Migração

### Para cada página:

- [ ] Atualizar extends do template base
- [ ] Substituir botões por componentes ou classes do DS
- [ ] Substituir cards por componentes
- [ ] Atualizar formulários com componentes
- [ ] Substituir modais por componentes
- [ ] Atualizar cores para variáveis CSS
- [ ] Verificar responsividade
- [ ] Testar funcionalidades JavaScript
- [ ] Validar acessibilidade
- [ ] Testar modo escuro/claro

### Validação:

- [ ] Página mantém funcionalidade original
- [ ] Visual está consistente com o Design System
- [ ] Responsivo funciona corretamente
- [ ] Acessibilidade mantida (navegação por teclado, contraste)
- [ ] Performance não foi degradada

## 🚨 Problemas Comuns

### 1. Classes Conflitantes
**Problema:** Classes antigas conflitando com novas
**Solução:** Remover classes antigas e usar apenas as do DS

### 2. JavaScript Quebrado
**Problema:** Funções antigas não funcionam
**Solução:** Atualizar para usar as funções globais do DS

### 3. Estilos Customizados
**Problema:** CSS customizado não funcionando
**Solução:** Usar variáveis CSS ou criar classes utilitárias

### 4. Modais Não Abrem
**Problema:** Modais antigos não funcionam
**Solução:** Usar os novos componentes e funções

## 📋 Exemplo Completo de Migração

### ANTES:
```html
{% extends 'base.html' %}

{% block content %}
<div class="container mx-auto p-4">
    <div class="bg-white shadow rounded-lg p-6 mb-4">
        <h2 class="text-xl font-bold mb-4">Pacientes</h2>
        <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
            Novo Paciente
        </button>
    </div>
    
    <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
        <div class="bg-white rounded-lg shadow p-6">
            <div class="text-2xl font-bold">125</div>
            <div class="text-gray-600">Total</div>
        </div>
    </div>
</div>
{% endblock %}
```

### DEPOIS:
```html
{% extends 'base_design_system.html' %}

{% block content %}
<div class="dashboard">
    {% include 'components/card.html' with title='Pacientes' icon='fas fa-users' %}
        {% include 'components/button.html' with variant='primary' text='Novo Paciente' icon='fas fa-plus' href='/patients/create/' %}
    {% endinclude %}
    
    <div class="stats-grid mt-6">
        {% include 'components/stat_card.html' with label='Total de Pacientes' value='125' icon='fas fa-users' icon_variant='success' trend='up' trend_value='8%' %}
    </div>
</div>
{% endblock %}
```

## 🔄 Processo de Migração Recomendado

1. **Página por página**: Migre uma página de cada vez
2. **Teste constantemente**: Valide cada mudança
3. **Mantenha backup**: Tenha sempre uma versão anterior
4. **Documente problemas**: Anote questões para resolver depois
5. **Solicite review**: Peça para alguém revisar as mudanças

## 📞 Suporte

Se encontrar problemas durante a migração:

1. Consulte a [Documentação do Design System](design-system.md)
2. Verifique os [Componentes Disponíveis](components-library.md)
3. Analise os exemplos neste guia
4. Teste no ambiente de desenvolvimento primeiro

---

**📌 Lembre-se:** A migração é um processo gradual. Não tente migrar tudo de uma vez. Foque na consistência e na experiência do usuário.