# 🎯 OBJETIVO
Criar a página completa de Montagem de Plano Alimentar para nutricionistas no sistema Django, com interface moderna, cálculos automáticos, busca inteligente de alimentos (Tabela TACO), geração de substituições e cardápios.

# 📐 ESPECIFICAÇÕES FUNCIONAIS

## 1. DADOS DE ENTRADA (vindos do paciente)
O sistema já possui:

- ✅ Cadastro de Pacientes
- ✅ Anamnese completa (objetivo, restrições, alergias, preferências)

Dados necessários para cálculos:

- Nome, Sexo, Idade
- Peso (kg), Altura (m)
- % Gordura corporal (se disponível)
- Nível de atividade física (Sedentário, Leve, Moderado, Intenso, Muito Intenso)
- Objetivo (Emagrecimento, Ganho de Massa, Manutenção, Saúde)
- Restrições alimentares (da anamnese)

## 2. FÓRMULAS PARA CÁLCULO CALÓRICO
Implementar 4 fórmulas principais:

**A) Harris-Benedict (1984 - revisada)**
- **Homens:** TMB = 88.362 + (13.397 × peso_kg) + (4.799 × altura_cm) - (5.677 × idade)
- **Mulheres:** TMB = 447.593 + (9.247 × peso_kg) + (3.098 × altura_cm) - (4.330 × idade)

**B) Mifflin-St Jeor (1990)**
- **Homens:** TMB = (10 × peso_kg) + (6.25 × altura_cm) - (5 × idade) + 5
- **Mulheres:** TMB = (10 × peso_kg) + (6.25 × altura_cm) - (5 × idade) - 161

**C) Cunningham (requer % gordura)**
- TMB = 500 + (22 × massa_magra_kg)
- `massa_magra_kg = peso_kg × (1 - %gordura/100)`

**D) Katch-McArdle (requer % gordura)**
- TMB = 370 + (21.6 × massa_magra_kg)

**Gasto Calórico Diário Total (GCDT):**
GCDT = TMB × Fator_Atividade

**Fatores de Atividade:**
- Sedentário: 1.2
- Levemente ativo: 1.375
- Moderadamente ativo: 1.55
- Muito ativo: 1.725
- Extremamente ativo: 1.9

**Ajuste por Objetivo:**
- Emagrecimento: GCDT - 15% a 20%
- Ganho de massa: GCDT + 10% a 15%
- Manutenção: GCDT

## 3. DISTRIBUIÇÃO DE MACRONUTRIENTES
Padrão sugerido (ajustável):

**Emagrecimento:**
- Proteínas: 30-35% (2.0-2.5g/kg)
- Carboidratos: 40-45%
- Gorduras: 20-25%

**Ganho de Massa:**
- Proteínas: 25-30% (1.8-2.2g/kg)
- Carboidratos: 50-55%
- Gorduras: 20-25%

**Manutenção/Saúde:**
- Proteínas: 20-25%
- Carboidratos: 50-55%
- Gorduras: 25-30%

**Cálculos:**
```python
# Exemplo com 2000 kcal e 30% proteína:
calorias_proteina = 2000 * 0.30 = 600 kcal
gramas_proteina = 600 / 4 = 150g  # 1g proteína = 4 kcal

gramas_carboidrato = (calorias_carbo) / 4  # 1g carbo = 4 kcal
gramas_gordura = (calorias_gordura) / 9    # 1g gordura = 9 kcal
```

## 4. TABELA TACO DE ALIMENTOS
Fonte oficial: TACO (Tabela Brasileira de Composição de Alimentos) - UNICAMP

**Estrutura do banco de dados:**
```python
# Model: Alimento
class Alimento(models.Model):
    id = models.AutoField(primary_key=True)
    codigo_taco = models.CharField(max_length=255, unique=True)
    nome = models.CharField(max_length=255)
    categoria = models.CharField(max_length=255)
    porcao_padrao = models.DecimalField(max_digits=10, decimal_places=2)
    unidade_padrao = models.CharField(max_length=50)
    calorias = models.DecimalField(max_digits=10, decimal_places=2)
    proteinas = models.DecimalField(max_digits=10, decimal_places=2)
    carboidratos = models.DecimalField(max_digits=10, decimal_places=2)
    gorduras_totais = models.DecimalField(max_digits=10, decimal_places=2)
    gorduras_saturadas = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    fibras = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sodio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    calcio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ferro = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

**Categorias principais:**
- Cereais e derivados
- Verduras e legumes
- Frutas e sucos
- Carnes e ovos
- Leite e derivados
- Leguminosas
- Óleos e gorduras
- Açúcares e doces
- Oleaginosas
- Bebidas

**Total:** ~1.700 alimentos na TACO 4ª edição

**Link para download:**
[https://www.cfn.org.br/wp-content/uploads/2017/03/taco_4_edicao_ampliada_e_revisada.pdf](https://www.cfn.org.br/wp-content/uploads/2017/03/taco_4_edicao_ampliada_e_revisada.pdf)

## 5. ALIMENTOS CUSTOMIZADOS DO NUTRICIONISTA
```python
# Model: AlimentoCustomizado
class AlimentoCustomizado(models.Model):
    id = models.AutoField(primary_key=True)
    nutricionista = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    categoria = models.CharField(max_length=255)
    porcao_padrao = models.DecimalField(max_digits=10, decimal_places=2)
    unidade_padrao = models.CharField(max_length=50)
    calorias = models.DecimalField(max_digits=10, decimal_places=2)
    proteinas = models.DecimalField(max_digits=10, decimal_places=2)
    carboidratos = models.DecimalField(max_digits=10, decimal_places=2)
    gorduras_totais = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```
**Regra:** Alimentos customizados aparecem só para o nutricionista que criou.

## 6. SISTEMA DE FAVORITOS
```python
# Model: AlimentoFavorito
class AlimentoFavorito(models.Model):
    id = models.AutoField(primary_key=True)
    nutricionista = models.ForeignKey(User, on_delete=models.CASCADE)
    alimento = models.ForeignKey(Alimento, on_delete=models.CASCADE) # Pode ser TACO ou Customizado
    created_at = models.DateTimeField(auto_now_add=True)
```
**Lógica de busca:**
- Se filtro = "Favoritos": mostra só favoritos do nutricionista
- Se filtro = "Todos": mostra TACO + Customizados do nutricionista
- Se filtro = "Meus alimentos": mostra só customizados

## 7. ESTRUTURA DO PLANO ALIMENTAR
```python
# Model: PlanoAlimentar
class PlanoAlimentar(models.Model):
    id = models.AutoField(primary_key=True)
    paciente = models.ForeignKey('patients.PatientProfile', on_delete=models.CASCADE)
    nutricionista = models.ForeignKey(User, on_delete=models.CASCADE)
    data_criacao = models.DateField(auto_now_add=True)
    data_entrega = models.DateField()
    data_retorno = models.DateField()
    formula_usada = models.CharField(max_length=100)
    tmb = models.DecimalField(max_digits=10, decimal_places=2)
    gcdt = models.DecimalField(max_digits=10, decimal_places=2)
    calorias_meta = models.DecimalField(max_digits=10, decimal_places=2)
    proteinas_meta = models.DecimalField(max_digits=10, decimal_places=2)
    carboidratos_meta = models.DecimalField(max_digits=10, decimal_places=2)
    gorduras_meta = models.DecimalField(max_digits=10, decimal_places=2)
    observacoes = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50, default='Rascunho') # Rascunho, Finalizado, Arquivado
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Model: Refeicao
class Refeicao(models.Model):
    id = models.AutoField(primary_key=True)
    plano = models.ForeignKey(PlanoAlimentar, related_name='refeicoes', on_delete=models.CASCADE)
    ordem = models.IntegerField()
    nome = models.CharField(max_length=100) # Café da Manhã, Lanche, etc
    horario = models.TimeField()
    observacoes = models.TextField(blank=True, null=True)

# Model: ItemRefeicao
class ItemRefeicao(models.Model):
    id = models.AutoField(primary_key=True)
    refeicao = models.ForeignKey(Refeicao, related_name='itens', on_delete=models.CASCADE)
    alimento = models.ForeignKey(Alimento, on_delete=models.CASCADE)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    unidade = models.CharField(max_length=50)
    calorias_calculadas = models.DecimalField(max_digits=10, decimal_places=2)
    proteinas_calculadas = models.DecimalField(max_digits=10, decimal_places=2)
    carboidratos_calculados = models.DecimalField(max_digits=10, decimal_places=2)
    gorduras_calculadas = models.DecimalField(max_digits=10, decimal_places=2)
    ordem = models.IntegerField()
```

---

## 8. INTERFACE DA PÁGINA (Layout Visual)

#### SEÇÃO 1: Header da Página
```
┌─────────────────────────────────────────────────┐
│ ← Voltar | Plano Alimentar - Maria Silva        │
│                                    [Salvar] [PDF]│
└─────────────────────────────────────────────────┘
```

#### SEÇÃO 2: Dados do Paciente + Fórmulas
```
┌─────────────────────────────────────────────────┐
│ 👤 DADOS DO PACIENTE                            │
├─────────────────────────────────────────────────┤
│ [Card 1]        [Card 2]        [Card 3]        │
│ Peso: 65kg      Altura: 1.65m   Idade: 27      │
│ Sexo: Feminino  Ativ: Moderada  Obj: Emagrecer │
│                                                  │
│ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━│
│                                                  │
│ 📊 ESCOLHA A FÓRMULA:                           │
│ ( ) Harris-Benedict (clássica)                  │
│ ( ) Mifflin-St Jeor (moderna, mais precisa)    │
│ ( ) Cunningham (requer % gordura)              │
│ ( ) Katch-McArdle (requer % gordura)           │
│                                                  │
│ 💡 Sugestão Inteligente:                        │
│ "Mifflin-St Jeor recomendada para seu perfil"  │
│                                                  │
│ [Calcular TMB e GCDT]                           │
│                                                  │
│ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━│
│                                                  │
│ 📈 RESULTADO:                                   │
│ TMB: 1366 kcal | GCDT: 2116 kcal               │
│ Meta (emagrecimento -15%): 1800 kcal           │
│                                                  │
│ Distribuição sugerida:                          │
│ Proteínas: 135g (30%) | Carbos: 203g (45%)     │
│ Gorduras: 50g (25%)                             │
│                                                  │
│ [Ajustar Manualmente] ou [Aceitar]             │
└─────────────────────────────────────────────────┘
```

#### SEÇÃO 3: Painel de Metas (Fixo no Topo ao Scrollar)
```
┌─────────────────────────────────────────────────┐
│ 🎯 META DIÁRIA                                  │
├─────────────────────────────────────────────────┤
│ CALORIAS: 1800 kcal          Consumido: 1250   │
│ ████████████░░░░░░░░ 69% | Faltam: 550 kcal   │
│                                                  │
│ [Proteínas]     [Carboidratos]     [Gorduras]  │
│  135g (30%)       203g (45%)        50g (25%)  │
│  Atual: 95g       Atual: 140g       Atual: 35g │
│  ███████░░░       ██████░░░░        ███████░░░ │
│  Falta: 40g       Falta: 63g        Falta: 15g │
└─────────────────────────────────────────────────┘
```

#### SEÇÃO 4: Refeições (Repetível)
```
┌─────────────────────────────────────────────────┐
│ 🍳 REFEIÇÃO 1                                   │
├─────────────────────────────────────────────────┤
│ Nome: [Café da Manhã____] Horário: [07:00__]   │
│                                                  │
│ 🔍 Buscar alimento...  [🌟 Favoritos ▾]        │
│                                                  │
│ ┌─Tabela de Alimentos─────────────────────────┐│
│ │Alimento        Qtd Un  Ptn Carb Gor  Kcal  [X]│
│ │──────────────────────────────────────────────││
│ │Pão integral    50  g   4g  25g  2g   140    │││
│ │Ovo cozido      2   un  12g  0g  8g   120    │││
│ │Banana prata    1   un  1g  26g  0g   105    │││
│ │Café c/ leite   200 ml  6g  10g  3g    95    │││
│ │                                               ││
│ │[+ Adicionar linha]                            ││
│ └───────────────────────────────────────────────┘│
│                                                  │
│ TOTAL DA REFEIÇÃO: 23g  61g  13g   460 kcal    │
│                                                  │
│ Observações: [_______________________________]  │
└─────────────────────────────────────────────────┘

[+ ADICIONAR NOVA REFEIÇÃO]
```

#### SEÇÃO 5: Autocomplete de Busca (Popup)
```
┌──────────────────────────────────┐
│ 🔍 arr_              [🌟] [📋]  │
├──────────────────────────────────┤
│ ⭐ Arroz integral (Favorito)     │ ← Hover verde
│ ⭐ Arroz branco (Favorito)       │
│ ──────────────────────────────── │
│    Arroz parboilizado            │
│    Arroz selvagem                │
│    Arroz arbóreo                 │
│    Arroz basmati                 │
│    Arroz negro                   │
│ ... mais 8 resultados            │
│                                   │
│ [+ Adicionar novo alimento]      │
└──────────────────────────────────┘

[🌟] = Mostrar favoritos
[📋] = Mostrar todos
```

#### SEÇÃO 6: Substituições Automáticas
```
┌─────────────────────────────────────────────────┐
│ 🔄 TABELA DE SUBSTITUIÇÕES                      │
├─────────────────────────────────────────────────┤
│ [Gerar Substituições Automaticamente]           │
│                                                  │
│ ┌──────────────────┬──────────────────────────┐│
│ │ CARBOIDRATOS     │ PROTEÍNAS                ││
│ ├──────────────────┼──────────────────────────┤│
│ │ Arroz integral   │ Frango grelhado          ││
│ │ 50g (180kcal)    │ 150g (165kcal)           ││
│ │ 3g ptn, 40g carb │ 31g ptn, 4g gor          ││
│ │                  │                          ││
│ │ Pode trocar por: │ Pode trocar por:         ││
│ │ • Batata doce 65g│ • Tilápia 160g           ││
│ │ • Macarrão 45g   │ • Carne moída 140g       ││
│ │ • Mandioca 60g   │ • Atum lata 130g         ││
│ │ • Inhame 70g     │ • Ovo (3 unidades)       ││
│ │ • Quinoa 55g     │ • Peito peru 145g        ││
│ └──────────────────┴──────────────────────────┘│
│                                                  │
│ [Baixar PDF das Substituições]                  │
└─────────────────────────────────────────────────┘
```
**Lógica de Substituições:**
```python
# Algoritmo:
# 1. Para cada refeição, identificar:
#    - Carboidrato principal (maior qtd de carbo)
#    - Proteína principal (maior qtd de proteína)
# 2. Buscar substitutos onde:
#    - Macronutriente principal ± 10%
#    - Calorias ± 15%
#    - Mesma categoria (ex: cereal por cereal)
# 3. Ordenar por:
#    - Favoritos primeiro
#    - Similaridade nutricional
#    - Nome alfabético
```

#### SEÇÃO 7: Cardápio Automático (IA)
```
┌─────────────────────────────────────────────────┐
│ 🤖 GERADOR DE CARDÁPIO INTELIGENTE              │
├─────────────────────────────────────────────────┤
│ Gerar cardápio para quantos dias? [7____]      │
│                                                  │
│ Variação de alimentos:                          │
│ ( ) Baixa (repete mais)                         │
│ (•) Média (recomendado)                         │
│ ( ) Alta (máxima variedade)                     │
│                                                  │
│ O sistema vai considerar:                       │
│ ✅ Meta calórica: 1800 kcal                     │
│ ✅ Objetivo: Emagrecimento                      │
│ ✅ Restrições: Sem lactose (da anamnese)        │
│ ✅ Preferências: Alimentos favoritos            │
│                                                  │
│ [Gerar Cardápio com IA]                         │
│                                                  │
│ ⚠️ Custo estimado: R$ 0,01 (usa API Claude)    │
└─────────────────────────────────────────────────┘
```

#### SEÇÃO 8: Gráficos
```
┌─────────────────────────────────────────────────┐
│ 📊 VISUALIZAÇÕES                                │
├─────────────────────────────────────────────────┤
│ [Gráfico 1: Pizza]      [Gráfico 2: Barras]    │
│                                                  │
│ Distribuição Macros     Calorias por Refeição  │
│      ╱──────╲               ┃                   │
│    ╱  Ptn   ╲             ┃▓▓▓▓▓ Café 460     │
│   │   30%    │            ┃▓▓▓   Lanc 300     │
│    ╲  Carb ╱             ┃▓▓▓▓▓▓ Almo 650     │
│      ╲ 45% ╱              ┃▓▓▓▓   Lanc 390     │
│    Gor 25%                                      │
└─────────────────────────────────────────────────┘
```

#### SEÇÃO 9: Footer/Ações
```
┌─────────────────────────────────────────────────┐
│ [💾 Salvar Rascunho]  [👁️ Pré-visualizar]       │
│ [📄 Gerar PDF]        [✅ Finalizar e Enviar]   │
└─────────────────────────────────────────────────┘
```

## 9. FUNCIONALIDADES INTERATIVAS (JavaScript)
- **Busca de Alimentos (Autocomplete):**
  ```javascript
  // Debounce de 300ms
  // Ao digitar: busca no backend
  // Retorna JSON: [{id, nome, categoria, macros, isFavorito}]
  // Renderiza dropdown
  // Teclas: ↓↑ navega, Enter seleciona, Esc fecha
  // Clique fora fecha
  ```
- **Adicionar Alimento à Refeição:**
  ```javascript
  // Ao selecionar alimento:
  // 1. Cria nova linha na tabela
  // 2. Campos editáveis: quantidade, unidade
  // 3. Calcula macros proporcionalmente
  // 4. Atualiza totalizador da refeição
  // 5. Atualiza painel de metas (topo)
  // 6. Animação: fade-in + slide
  ```
- **Remover Alimento:**
  ```javascript
  // Botão [X] vermelho
  // 1. Animação: fade-out + slide-up
  // 2. Recalcula totalizador da refeição
  // 3. Atualiza painel de metas
  ```
- **Favoritar Alimento:**
  ```javascript
  // Botão ⭐
  // 1. Toggle favorito (AJAX)
  // 2. Muda cor: cinza → amarelo
  // 3. Atualiza lista de favoritos
  ```
- **Gerar Substituições:**
  ```javascript
  // Botão "Gerar Substituições"
  // 1. Loading spinner
  // 2. POST para backend com todas as refeições
  // 3. Backend executa algoritmo
  // 4. Retorna JSON com substituições
  // 5. Renderiza tabela
  // 6. Animação de sucesso
  ```
- **Gerar Cardápio IA:**
  ```javascript
  // Botão "Gerar Cardápio com IA"
  // 1. Modal de confirmação (custo)
  // 2. Loading overlay (pode demorar 5-10s)
  // 3. POST para backend
  // 4. Backend chama API Claude
  // 5. Retorna 7 dias de cardápio
  // 6. Renderiza em cards/accordions
  // 7. Opção: "Aplicar este dia ao plano"
  ```
- **Painel de Metas (Sticky):**
  ```javascript
  // Fixa no topo ao scrollar
  // Atualiza em tempo real ao adicionar/remover
  // Barras de progresso animadas (CSS transitions)
  // Cores: verde (>80%), laranja (50-80%), vermelho (<50%)
  ```
- **Validações:**
  ```javascript
  // Antes de salvar:
  // - Mínimo 3 refeições
  // - Cada refeição tem pelo menos 1 alimento
  // - Meta calórica atingida (±10%)
  // - Nome e horário preenchidos em todas refeições
  ```

## 10. BACKEND (Views Django)
```python
# views.py

def criar_plano_alimentar(request, paciente_id):
    """Página principal de criação"""
    paciente = get_object_or_404(Paciente, pk=paciente_id)
    # Renderiza template com dados do paciente
    pass

def calcular_tmb(request):
    """AJAX: Calcula TMB baseado na fórmula escolhida"""
    # POST: {peso, altura, idade, sexo, formula, %gordura?}
    # Retorna JSON: {tmb, gcdt, meta_calorias, macros_sugeridos}
    pass

def buscar_alimentos(request):
    """AJAX: Autocomplete de alimentos"""
    # GET: ?q=arr&filtro=favoritos
    # Retorna JSON: [{id, nome, categoria, macros, isFavorito}]
    pass

def toggle_favorito(request):
    """AJAX: Adiciona/remove favorito"""
    # POST: {alimento_id}
    # Retorna JSON: {success, isFavorito}
    pass

def salvar_plano(request):
    """Salva plano (rascunho ou finalizado)"""
    # POST: JSON completo do plano
    # Cria PlanoAlimentar + Refeicoes + ItensRefeicao
    # Retorna JSON: {success, plano_id}
    pass

def gerar_substituicoes(request):
    """AJAX: Gera tabela de substituições"""
    # POST: {refeicoes: [...]}
    # Executa algoritmo de substituição
    # Retorna JSON: {carboidratos: [...], proteinas: [...]}
    pass

def gerar_cardapio_ia(request):
    """AJAX: Chama API Claude para gerar cardápio"""
    # POST: {dias, variacao, meta_calorias, restricoes}
    # Chama API Claude com prompt estruturado
    # Retorna JSON: {dias: [{dia, refeicoes: [...]}]}
    pass

def gerar_pdf(request, plano_id):
    """Gera PDF do plano alimentar"""
    # Usa weasyprint ou reportlab
    # Template HTML → PDF
    # Retorna arquivo PDF
    pass
```

## 11. URLS
```python
# urls.py
urlpatterns = [
    path('plano/criar/<int:paciente_id>/', views.criar_plano_alimentar, name='criar_plano'),
    path('plano/calcular-tmb/', views.calcular_tmb, name='calcular_tmb'),
    path('alimentos/buscar/', views.buscar_alimentos, name='buscar_alimentos'),
    path('alimentos/favoritar/', views.toggle_favorito, name='toggle_favorito'),
    path('plano/salvar/', views.salvar_plano, name='salvar_plano'),
    path('plano/substituicoes/', views.gerar_substituicoes, name='gerar_substituicoes'),
    path('plano/cardapio-ia/', views.gerar_cardapio_ia, name='gerar_cardapio_ia'),
    path('plano/pdf/<int:plano_id>/', views.gerar_pdf, name='gerar_pdf'),
]
```

## 12. INTEGRAÇÃO COM API CLAUDE (IA)
Opção escolhida: API Claude

**Setup:**
```python
# settings.py
ANTHROPIC_API_KEY = 'sk-ant-...'  # Variável de ambiente

# requirements.txt
anthropic==0.25.0
```

**Exemplo de chamada:**
```python
import anthropic

def gerar_cardapio_com_ia(meta_calorias, restricoes, dias=7):
    client = anthropic.Anthropic(api_key=settings.ANTHROPIC_API_KEY)

    prompt = f"""
    Crie um cardápio de {dias} dias para um paciente com:
    - Meta: {meta_calorias} kcal/dia
    - Restrições: {restricoes}
    - Distribuição: 30% ptn, 45% carb, 25% gor

    Retorne APENAS JSON no formato:
    {{
      "dias": [
        {{
          "dia": 1,
          "refeicoes": [
            {{
              "nome": "Café da Manhã",
              "horario": "07:00",
              "alimentos": [
                {{"nome": "Pão integral", "qtd": 50, "un": "g"}},
                ...
              ]
            }},
            ...
          ]
        }},
        ...
      ]
    }}
    """

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=4000,
        messages=[{"role": "user", "content": prompt}]
    )

    return json.loads(response.content[0].text)
```

**Custo estimado:**
- Input: ~500 tokens × $0.003/1K = $0.0015
- Output: ~3000 tokens × $0.015/1K = $0.045
- **Total por cardápio: ~$0.05 (R$ 0,25)**

---

## 13. REGRAS DE NEGÓCIO

**Validações obrigatórias:**
- ✅ Plano deve ter entre 3-8 refeições
- ✅ Cada refeição deve ter pelo menos 1 alimento
- ✅ Horários não podem conflitar (mínimo 2h entre refeições)
- ✅ Meta calórica deve ser atingida com tolerância de ±10%
- ✅ Alimentos com restrições do paciente não podem ser adicionados

**Permissões:**
- ✅ Nutricionista só edita seus próprios planos
- ✅ Alimentos customizados são privados por nutricionista
- ✅ Favoritos são privados por nutricionista

**Status do plano:**
- 📝 Rascunho: pode editar livremente
- ✅ Finalizado: enviado ao paciente, não pode editar (só duplicar)
- 📦 Arquivado: histórico, não aparece em listagens

---

## 14. ARQUIVOS NECESSÁRIOS

**Templates:**
```
templates/
├── planos/
│   ├── criar_plano.html           # Página principal
│   ├── components/
│   │   ├── painel_metas.html      # Painel de metas fixo
│   │   ├── card_refeicao.html     # Card de refeição
│   │   ├── modal_busca.html       # Modal de busca
│   │   └── tabela_substituicoes.html
│   └── pdf_plano.html             # Template para PDF
```

**CSS:**
```
static/css/
├── plano-alimentar.css  # Estilos específicos da página
└── (usa tokens.css, base.css, components.css do Design System)
```

**JavaScript:**
```
static/js/
├── plano-alimentar.js   # Lógica principal
├── autocomplete.js      # Busca de alimentos
└── calculos.js          # Cálculos de macros em tempo real
```

## 15. DADOS DA TABELA TACO
**Como importar:**

Download da TACO:
- Link oficial: [https://www.cfn.org.br/index.php/composicao-dos-alimentos/](https://www.cfn.org.br/index.php/composicao-dos-alimentos/)
- Formato: Excel (.xlsx) ou CSV
- Versão recomendada: TACO 4ª edição (revisada e ampliada)

**Script de Importação Django:**
```python
# management/commands/importar_taco.py

from django.core.management.base import BaseCommand
import pandas as pd
from alimentos.models import Alimento

class Command(BaseCommand):
    help = 'Importa alimentos da Tabela TACO'

    def handle(self, *args, **kwargs):
        # Lê arquivo Excel/CSV da TACO
        df = pd.read_excel('data/taco_4_edicao.xlsx')

        for index, row in df.iterrows():
            Alimento.objects.update_or_create(
                codigo_taco=row['codigo'],
                defaults={
                    'nome': row['descricao'],
                    'categoria': row['categoria'],
                    'porcao_padrao': 100,  # TACO é baseada em 100g
                    'unidade_padrao': 'g',
                    'calorias': row['energia_kcal'],
                    'proteinas': row['proteina_g'],
                    'carboidratos': row['carboidrato_g'],
                    'gorduras_totais': row['lipideos_g'],
                    'gorduras_saturadas': row['saturados_g'] or 0,
                    'fibras': row['fibra_g'] or 0,
                    'sodio': row['sodio_mg'] or 0,
                    'calcio': row['calcio_mg'] or 0,
                    'ferro': row['ferro_mg'] or 0,
                }
            )

        self.stdout.write(self.style.SUCCESS(f'Importados {df.shape[0]} alimentos'))
```
**Executar importação:**
```bash
python manage.py importar_taco
```

**Estrutura CSV alternativa (se não tiver Excel):**
```csv
codigo,nome,categoria,calorias,proteinas,carboidratos,gorduras,fibras,sodio
C001,Arroz branco cozido,Cereais,128,2.5,28.1,0.2,0.2,1
C002,Arroz integral cozido,Cereais,123,2.6,25.8,1.0,2.7,1
C003,Macarrão cozido,Cereais,135,4.5,28.0,0.5,1.2,1
...
```

---

## 16. EXEMPLO COMPLETO DE FLUXO DE USO

**Passo a passo do nutricionista:**

1.  **Acessa o plano:**
    `Dashboard → Pacientes → Maria Silva → [Criar Plano Alimentar]`
2.  **Calcula TMB/GCDT:**
    - Dados já vêm preenchidos (peso, altura, idade)
    - Escolhe fórmula: Mifflin-St Jeor
    - Clica [Calcular]
    - Sistema mostra: TMB 1366 kcal, GCDT 2116 kcal
    - Objetivo: Emagrecimento (-15%) = 1800 kcal
    - Sistema sugere macros: 135g ptn, 203g carb, 50g gor
3.  **Monta Café da Manhã (07:00):**
    - Clica [+ Adicionar Refeição]
    - Nome: "Café da Manhã" | Horário: "07:00"
    - Busca "pao" → seleciona "Pão integral"
    - Quantidade: 50g
    - Sistema calcula: 4g ptn, 25g carb, 2g gor, 140 kcal ✅
    - Adiciona "Ovo cozido": 2 unidades
    - Sistema calcula: 12g ptn, 0g carb, 8g gor, 120 kcal ✅
    - Adiciona "Banana prata": 1 unidade
    - Total da refeição: 23g ptn, 61g carb, 13g gor, 460 kcal
    - **Painel de metas atualiza automaticamente**
4.  **Repete para todas refeições:**
    - Lanche da Manhã (10:00)
    - Almoço (12:30)
    - Lanche da Tarde (16:00)
    - Jantar (19:30)
    - Ceia (22:00)
5.  **Gera substituições:**
    - Clica [Gerar Substituições]
    - Sistema identifica carboidratos/proteínas principais
    - Mostra tabela de substituições equivalentes
6.  **Gera cardápio IA (opcional):**
    - Clica [Gerar Cardápio 7 dias]
    - IA cria variações do plano
    - Nutricionista escolhe quais dias usar
7.  **Finaliza:**
    - Clica [Gerar PDF]
    - Revisa PDF
    - Clica [Finalizar e Enviar]
    - Status muda para "Finalizado"
    - Paciente recebe notificação (email/WhatsApp)

---

## 17. ESTRUTURA DO PDF GERADO

**Layout do PDF:**
```
┌─────────────────────────────────────────────────┐
│             [LOGO NUTRICIONISTA]                │
│                                                  │
│          PLANO ALIMENTAR PERSONALIZADO          │
│                                                  │
│ Paciente: Maria Silva                           │
│ Data de Entrega: 14/11/2024                     │
│ Data de Retorno: 14/12/2024                     │
│ Nutricionista: Dr. João Santos | CRN 12345      │
├─────────────────────────────────────────────────┤
│                                                  │
│ DADOS ANTROPOMÉTRICOS                           │
│ Peso: 65kg | Altura: 1.65m | IMC: 23.9         │
│ Idade: 27 anos | Sexo: Feminino                 │
│                                                  │
│ OBJETIVO: Emagrecimento saudável                │
│ ATIVIDADE FÍSICA: Moderada (3-5x/semana)        │
├─────────────────────────────────────────────────┤
│                                                  │
│ PRESCRIÇÃO DIETÉTICA                            │
│ Valor Energético Total (VET): 1800 kcal        │
│ Proteínas: 135g (30%) | 2.1g/kg                 │
│ Carboidratos: 203g (45%)                        │
│ Gorduras: 50g (25%)                             │
├─────────────────────────────────────────────────┤
│                                                  │
│ 🍳 CAFÉ DA MANHÃ - 07:00                        │
│ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━│
│ • Pão integral .......................... 50g  │
│ • Ovo cozido ..................... 2 unidades  │
│ • Banana prata ..................... 1 unidade │
│ • Café com leite desnatado ............. 200ml │
│                                                  │
│ TOTAL: 23g ptn | 61g carb | 13g gor | 460 kcal │
│                                                  │
│ 🥤 LANCHE DA MANHÃ - 10:00                      │
│ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━│
│ • Iogurte grego natural ............... 150g   │
│ • Granola sem açúcar ................... 30g   │
│                                                  │
│ TOTAL: 18g ptn | 32g carb | 9g gor | 300 kcal  │
│                                                  │
│ [... demais refeições ...]                      │
│                                                  │
├─────────────────────────────────────────────────┤
│                                                  │
│ 🔄 TABELA DE SUBSTITUIÇÕES                      │
│                                                  │
│ CARBOIDRATOS:                                   │
│ Arroz integral 50g pode trocar por:             │
│ ✓ Batata doce 65g                               │
│ ✓ Macarrão integral 45g                         │
│ ✓ Mandioca cozida 60g                           │
│ ✓ Quinoa cozida 55g                             │
│                                                  │
│ PROTEÍNAS:                                      │
│ Frango grelhado 150g pode trocar por:           │
│ ✓ Tilápia grelhada 160g                         │
│ ✓ Carne moída magra 140g                        │
│ ✓ Atum em água 130g                             │
│ ✓ Ovo (3 unidades)                              │
│                                                  │
├─────────────────────────────────────────────────┤
│                                                  │
│ ORIENTAÇÕES GERAIS:                             │
│ • Beber no mínimo 2L de água por dia           │
│ • Evitar frituras e alimentos ultraprocessados  │
│ • Respeitar os horários das refeições           │
│ • Não pular refeições                           │
│ • Registrar evolução de peso semanalmente       │
│                                                  │
│ OBSERVAÇÕES IMPORTANTES:                        │
│ [Texto personalizado do nutricionista]          │
│                                                  │
├─────────────────────────────────────────────────┤
│                                                  │
│ CONTROLE DE PESO SEMANAL:                       │
│                                                  │
│ Semana 1: _____kg | Data: ___/___/____         │
│ Semana 2: _____kg | Data: ___/___/____         │
│ Semana 3: _____kg | Data: ___/___/____         │
│ Semana 4: _____kg | Data: ___/___/____         │
│                                                  │
├─────────────────────────────────────────────────┤
│                                                  │
│ Este plano foi elaborado especialmente para     │
│ você, considerando suas necessidades e objetivo.│
│ Em caso de dúvidas, entre em contato.           │
│                                                  │
│ ________________________                        │
│ Assinatura e Carimbo                            │
│                                                  │
└─────────────────────────────────────────────────┘
```
**Biblioteca para gerar PDF:**
- **Opção 1: WeasyPrint (recomendado - HTML to PDF)** `pip install weasyprint`
- **Opção 2: ReportLab (mais controle, mais complexo)** `pip install reportlab`
- **Opção 3: xhtml2pdf (mais simples)** `pip install xhtml2pdf`

## 18. APIS/ENDPOINTS NECESSÁRIAS
Resumo de todas as rotas:
```python
# URLs da aplicação de planos

# GET - Renderiza página
/plano/criar/<paciente_id>/

# POST - AJAX endpoints
/api/plano/calcular-tmb/           # Calcula TMB/GCDT
/api/alimentos/buscar/             # Autocomplete busca
/api/alimentos/favoritar/          # Toggle favorito
/api/alimentos/criar-customizado/  # Cria alimento novo
/api/plano/salvar/                 # Salva plano (rascunho/final)
/api/plano/substituicoes/          # Gera substituições
/api/plano/cardapio-ia/            # Gera cardápio com IA

# GET - Download
/plano/pdf/<plano_id>/             # Baixa PDF
/plano/visualizar/<plano_id>/      # Pré-visualiza HTML
```
**Formato JSON das respostas:**
1.  **Buscar Alimentos:**
    ```json
    // GET /api/alimentos/buscar/?q=arr&filtro=favoritos
    {
      "results": [
        {
          "id": 123,
          "nome": "Arroz integral cozido",
          "categoria": "Cereais",
          "isFavorito": true,
          "isCustomizado": false,
          "macros": {
            "calorias": 123,
            "proteinas": 2.6,
            "carboidratos": 25.8,
            "gorduras": 1.0
          },
          "porcao_padrao": 100,
          "unidade_padrao": "g"
        }
      ],
      "count": 15
    }
    ```
2.  **Calcular TMB:**
    ```json
    // POST /api/plano/calcular-tmb/
    // Body: {peso, altura, idade, sexo, formula, atividade, objetivo, %gordura?}
    {
      "success": true,
      "tmb": 1366.5,
      "gcdt": 2116.7,
      "meta_calorias": 1799,
      "macros_sugeridos": {
        "proteinas": {"gramas": 135, "percentual": 30, "calorias": 540, "gramas_por_kg": 2.08},
        "carboidratos": {"gramas": 202, "percentual": 45, "calorias": 809},
        "gorduras": {"gramas": 50, "percentual": 25, "calorias": 450}
      },
      "sugestao_ia": "Mifflin-St Jeor é a mais indicada para seu perfil"
    }
    ```
3.  **Salvar Plano:**
    ```json
    // POST /api/plano/salvar/
    {
      "paciente_id": 45,
      "data_entrega": "2024-11-14",
      "data_retorno": "2024-12-14",
      "formula_usada": "Mifflin-St Jeor",
      "tmb": 1366.5,
      "gcdt": 2116.7,
      "calorias_meta": 1800,
      "proteinas_meta": 135,
      "carboidratos_meta": 203,
      "gorduras_meta": 50,
      "observacoes": "Evitar frituras...",
      "status": "finalizado",
      "refeicoes": [
        {
          "ordem": 1,
          "nome": "Café da Manhã",
          "horario": "07:00",
          "observacoes": "Tomar com água",
          "itens": [
            {"alimento_id": 123, "quantidade": 50, "unidade": "g"},
            {"alimento_id": 456, "quantidade": 2, "unidade": "unidade"}
          ]
        }
      ]
    }

    // Resposta:
    {
      "success": true,
      "plano_id": 789,
      "message": "Plano salvo com sucesso!"
    }
    ```
4.  **Gerar Substituições:**
    ```json
    // POST /api/plano/substituicoes/
    // Body: {refeicoes: [...]}
    {
      "success": true,
      "substituicoes": {
        "carboidratos": [
          {
            "original": {"nome": "Arroz integral", "quantidade": 50, "macros": {"ptn": 3, "carb": 40, "gor": 1, "kcal": 180}},
            "substitutos": [
              {"nome": "Batata doce", "quantidade": 65, "macros": {"ptn": 2, "carb": 38, "gor": 0, "kcal": 175}, "similaridade": 95}
            ]
          }
        ],
        "proteinas": [
          {
            "original": {"nome": "Frango grelhado", "quantidade": 150, "macros": {"ptn": 31, "carb": 0, "gor": 4, "kcal": 165}},
            "substitutos": []
          }
        ]
      }
    }
    ```
5.  **Gerar Cardápio IA:**
    ```json
    // POST /api/plano/cardapio-ia/
    // Body: {dias: 7, variacao: "media", meta_calorias: 1800, restricoes: [...]}
    {
      "success": true,
      "custo_estimado": 0.05,
      "cardapio": {
        "dias": [
          {
            "dia": 1,
            "data": "2024-11-14",
            "calorias_total": 1795,
            "refeicoes": [
              {
                "nome": "Café da Manhã",
                "horario": "07:00",
                "alimentos": [
                  {"nome": "Tapioca", "qtd": 60, "un": "g"},
                  {"nome": "Queijo cottage", "qtd": 50, "un": "g"}
                ],
                "macros": {"ptn": 25, "carb": 58, "gor": 12, "kcal": 445}
              }
            ]
          }
        ]
      }
    }
    ```

## 19. RESPONSIVIDADE (Mobile)
**Breakpoints:**
```css
/* Mobile first */
.container {
  padding: 1rem;
}

/* Tablet: 768px+ */
 @media (min-width: 768px) {
  .grid-refeicoes {
    grid-template-columns: repeat(2, 1fr);
  }
}

/* Desktop: 1024px+ */
 @media (min-width: 1024px) {
  .painel-metas {
    position: sticky;
    top: 70px; /* Altura do header */
  }
}
```
- **Mobile (< 768px):** Menu hambúrguer, Refeições empilhadas (1 coluna), Tabela de alimentos com scroll horizontal, Botões full-width, Painel de metas colapsável (accordion), Busca em modal fullscreen.
- **Tablet (768-1024px):** Refeições em 2 colunas, Sidebar colapsável, Botões tamanho médio.
- **Desktop (> 1024px):** Layout completo, Sidebar fixa, Painel de metas sticky, Hover effects.

## 20. PERFORMANCE & OTIMIZAÇÕES
**Backend:**
- Usar `select_related` e `prefetch_related`.
- Cache de busca de alimentos (Redis).
- Indexação no banco de dados.

**Frontend:**
- Debounce na busca.
- Lazy loading de imagens.
- Paginação na listagem de alimentos.

**CSS:**
- Animações com `will-change`.
- Critical CSS inline.

## 21. SEGURANÇA
- Verificar permissões.
- Sanitizar inputs.
- CSRF token em AJAX.
- Rate limiting.

## 22. TESTES
Testes unitários essenciais:
- `test_calculo_tmb_harris_benedict`
- `test_busca_alimentos_favoritos`
- `test_gerar_substituicoes`
- `test_salvar_plano`
