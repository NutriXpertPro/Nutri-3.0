# Design System - NutriXpert Pro Dashboard

## 📋 Visão Geral

Este documento apresenta o **Design System completo** extraído do Dashboard de Nutricionista do NutriXpert Pro, padronizando todos os elementos visuais para garantir consistência total em UX/UI.

## 🎨 Tokens de Design

### Cores

#### Modo Escuro (Padrão)
```css
--primary: #0f172a;        /* Background principal */
--secondary: #1e293b;      /* Background secundário */
--accent: #3b82f6;         /* Cor de destaque (azul) */
--accent-dark: #2563eb;    /* Variação mais escura do accent */
--success: #10b981;        /* Verde - sucesso */
--warning: #f59e0b;        /* Amarelo - aviso */
--danger: #ef4444;         /* Vermelho - erro/perigo */
--text-primary: #f8fafc;   /* Texto principal */
--text-secondary: #cbd5e1; /* Texto secundário */
--text-muted: #64748b;     /* Texto esmaecido */
--border: #334155;         /* Bordas */
--bg-card: #1e293b;        /* Background dos cards */
--bg-hover: #334155;       /* Background ao fazer hover */
--ai-accent: #8b5cf6;      /* Roxo para IA */
```

#### Modo Claro
```css
--primary: #F5F5DC;        /* Beige */
--secondary: #E0E0C0;      /* Light Khaki */
--accent: #3b82f6;         /* Azul (mantido) */
--text-primary: #333333;   /* Texto escuro */
--text-secondary: #666666; /* Texto secundário */
--text-muted: #999999;     /* Texto esmaecido */
--border: #D3D3D3;         /* Bordas claras */
--bg-card: #FFFFFF;        /* Background branco para cards */
--bg-hover: #F0F0E0;       /* Background hover claro */
```

### Tipografia

#### Família da Fonte
- **Principal**: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif
- **Importação**: Google Fonts - Inter (300, 400, 500, 600, 700, 800)

#### Tamanhos de Texto
```css
.text-xs { font-size: 0.75rem; }     /* 12px */
.text-sm { font-size: 0.875rem; }    /* 14px */
.text-base { font-size: 1rem; }      /* 16px */
.text-lg { font-size: 1.125rem; }    /* 18px */
.text-xl { font-size: 1.25rem; }     /* 20px */
.text-2xl { font-size: 1.5rem; }     /* 24px */
.text-3xl { font-size: 1.875rem; }   /* 30px */
.text-4xl { font-size: 2.25rem; }    /* 36px */
.text-5xl { font-size: 3rem; }       /* 48px */
```

#### Pesos da Fonte
```css
.font-light { font-weight: 300; }
.font-normal { font-weight: 400; }
.font-medium { font-weight: 500; }
.font-semibold { font-weight: 600; }
.font-bold { font-weight: 700; }
.font-extrabold { font-weight: 800; }
```

### Espaçamentos

#### Sistema de Espaçamento (baseado em rem)
```css
.spacing-1 { margin/padding: 0.25rem; }  /* 4px */
.spacing-2 { margin/padding: 0.5rem; }   /* 8px */
.spacing-3 { margin/padding: 0.75rem; }  /* 12px */
.spacing-4 { margin/padding: 1rem; }     /* 16px */
.spacing-5 { margin/padding: 1.25rem; }  /* 20px */
.spacing-6 { margin/padding: 1.5rem; }   /* 24px */
.spacing-8 { margin/padding: 2rem; }     /* 32px */
.spacing-10 { margin/padding: 2.5rem; }  /* 40px */
.spacing-12 { margin/padding: 3rem; }    /* 48px */
```

### Border Radius

```css
.rounded-sm { border-radius: 0.25rem; }   /* 4px */
.rounded { border-radius: 0.5rem; }       /* 8px */
.rounded-md { border-radius: 0.75rem; }   /* 12px */
.rounded-lg { border-radius: 1rem; }      /* 16px */
.rounded-xl { border-radius: 1.5rem; }    /* 24px */
.rounded-2xl { border-radius: 2rem; }     /* 32px */
.rounded-3xl { border-radius: 3rem; }     /* 48px */
.rounded-full { border-radius: 50%; }
```

### Sombras

```css
.shadow-sm { box-shadow: 0 1px 3px rgba(0,0,0,0.1); }
.shadow { box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
.shadow-md { box-shadow: 0 4px 12px rgba(0,0,0,0.15); }
.shadow-lg { box-shadow: 0 8px 20px rgba(0,0,0,0.15); }
.shadow-xl { box-shadow: 0 12px 24px rgba(0,0,0,0.2); }
.shadow-2xl { box-shadow: 0 20px 40px rgba(0,0,0,0.3); }
```

### Z-Index

```css
.z-0 { z-index: 0; }
.z-10 { z-index: 10; }
.z-20 { z-index: 20; }
.z-30 { z-index: 30; }
.z-40 { z-index: 40; }
.z-50 { z-index: 50; }
```

## 🏗️ Layout

### Grid System

#### Dashboard Principal
```css
.dashboard {
    padding: 24px;
    max-width: 1600px;
    margin: 0 auto;
}

.stats-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 20px;
    margin-bottom: 32px;
}

.main-grid {
    display: grid;
    grid-template-columns: 2fr 1fr;
    gap: 20px;
    margin-bottom: 32px;
}

.analytics-grid {
    display: grid;
    grid-template-columns: 2fr 1fr;
    gap: 20px;
}
```

#### Breakpoints Responsivos
```css
/* Mobile: <768px */
@media (max-width: 768px) {
    .main-grid,
    .analytics-grid {
        grid-template-columns: 1fr;
    }
    
    .stats-grid {
        grid-template-columns: 1fr;
    }
}
```

### Sidebar

#### Estrutura
```css
.sidebar {
    position: fixed;
    top: 0;
    left: 0;
    width: 80px;
    height: 100vh;
    background: var(--bg-card);
    border-right: 1px solid var(--border);
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 24px 0;
    z-index: 50;
}
```

## 🧩 Componentes

### Botões

#### Primário
```css
.btn-primary {
    background: var(--accent);
    color: white;
    padding: 12px 24px;
    border-radius: 12px;
    font-weight: 600;
    transition: all 0.3s ease;
}

.btn-primary:hover {
    background: var(--accent-dark);
    transform: translateY(-2px);
    box-shadow: 0 8px 20px rgba(59, 130, 246, 0.3);
}
```

#### Secundário
```css
.btn-secondary {
    background: var(--bg-hover);
    color: var(--text-primary);
    border: 1px solid var(--border);
    padding: 12px 24px;
    border-radius: 12px;
    font-weight: 600;
    transition: all 0.3s ease;
}

.btn-secondary:hover {
    border-color: var(--accent);
    transform: translateY(-2px);
}
```

#### AI (Inteligência Artificial)
```css
.btn-ai {
    background: var(--gradient-ai);
    color: white;
    position: relative;
    overflow: hidden;
}

.btn-ai:hover {
    transform: translateY(-4px);
    box-shadow: 0 16px 32px rgba(139, 92, 246, 0.5);
}
```

### Cards

#### Card Base
```css
.card {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 24px;
    transition: all 0.3s ease;
}

.card:hover {
    border-color: var(--accent);
    transform: translateY(-2px);
    box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
```

#### Stat Card
```css
.stat-card {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 24px;
    position: relative;
    transition: all 0.3s ease;
}

.stat-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 24px rgba(0, 0, 0, 0.2);
    border-color: var(--accent);
}
```

### Icons

#### Icon Button
```css
.icon-btn {
    width: 40px;
    height: 40px;
    border-radius: 10px;
    background: var(--bg-hover);
    color: var(--text-secondary);
    border: none;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: all 0.3s ease;
}

.icon-btn:hover {
    background: var(--accent);
    color: white;
    transform: scale(1.1);
}
```

### Forms

#### Input Field
```css
.search-input {
    width: 100%;
    padding: 12px 16px 12px 48px;
    background: var(--bg-hover);
    border: 1px solid var(--border);
    border-radius: 12px;
    color: var(--text-primary);
    font-size: 14px;
    transition: all 0.3s ease;
}

.search-input:focus {
    outline: none;
    border-color: var(--accent);
    box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
}
```

## 🎭 Estados de Interação

### Hover Effects
```css
/* Botões */
.btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}

/* Cards */
.card:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 24px rgba(0, 0, 0, 0.3);
    border-color: var(--accent);
}

/* Icon Buttons */
.icon-btn:hover {
    transform: scale(1.1);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}
```

### Focus States
```css
/* Para acessibilidade */
.btn:focus,
.icon-btn:focus,
.search-input:focus {
    outline: 2px solid var(--accent);
    outline-offset: 2px;
}
```

### Active States
```css
.btn:active {
    transform: translateY(0);
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.nav-item.active {
    background: var(--accent);
    color: white;
}
```

## 🎨 Animações e Transições

### Transições Base
```css
.transition-all { transition: all 0.3s ease; }
.transition-transform { transition: transform 0.3s ease; }
.transition-colors { transition: background-color 0.3s ease, color 0.3s ease; }
```

### Animações Keyframes
```css
@keyframes floating {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-10px); }
    100% { transform: translateY(0px); }
}

@keyframes subtleShift {
    0% { background-position: 0 0, 0 0, 0 0; }
    100% { background-position: 50px 50px, 50px 50px, 100px 100px; }
}

@keyframes pulse {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.05); }
}
```

## 📱 Responsividade

### Mobile First Approach
```css
/* Base: Mobile */
.dashboard {
    padding: 16px;
}

/* Tablet: 768px+ */
@media (min-width: 768px) {
    .dashboard {
        padding: 20px;
    }
}

/* Desktop: 1024px+ */
@media (min-width: 1024px) {
    .dashboard {
        padding: 24px;
    }
}
```

## ♿ Acessibilidade

### Contraste de Cores
- **Texto normal**: Mínimo 4.5:1 (WCAG AA)
- **Texto grande**: Mínimo 3:1 (WCAG AA)
- **Elementos UI**: Mínimo 3:1

### Navegação por Teclado
```css
/* Indicador de foco visível */
*:focus-visible {
    outline: 2px solid var(--accent);
    outline-offset: 2px;
}

/* Pular para conteúdo principal */
.skip-link {
    position: absolute;
    top: -40px;
    left: 6px;
    background: var(--accent);
    color: white;
    padding: 8px;
    text-decoration: none;
    transition: top 0.3s;
}

.skip-link:focus {
    top: 6px;
}
```

## 🔧 Utilitários

### Classes Helper
```css
/* Display */
.hidden { display: none; }
.block { display: block; }
.inline { display: inline; }
.flex { display: flex; }
.grid { display: grid; }

/* Flexbox */
.items-center { align-items: center; }
.justify-center { justify-content: center; }
.justify-between { justify-content: space-between; }

/* Text Alignment */
.text-left { text-align: left; }
.text-center { text-align: center; }
.text-right { text-align: right; }

/* Overflow */
.overflow-hidden { overflow: hidden; }
.overflow-auto { overflow: auto; }
```

---

## 📝 Próximos Passos

1. Implementar tokens de design em arquivo CSS separado
2. Criar componentes reutilizáveis 
3. Documentar biblioteca de componentes
4. Criar guia de migração para páginas existentes