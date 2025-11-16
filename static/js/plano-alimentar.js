// Plano Alimentar - JavaScript functionality
document.addEventListener('DOMContentLoaded', function() {
    // Controle de abas
    const abas = document.querySelectorAll('[id^="aba-"]');
    const conteudos = document.querySelectorAll('[id^="conteudo-"]');
    
    abas.forEach(aba => {
        aba.addEventListener('click', function() {
            const abaId = this.id.replace('aba-', '');
            
            // Remove classes ativas
            abas.forEach(a => {
                a.classList.remove('border-accent', 'text-accent');
                a.classList.add('border-transparent', 'text-muted-foreground');
            });
            
            // Remove conteúdos
            conteudos.forEach(c => c.classList.add('hidden'));
            
            // Ativa aba atual
            this.classList.add('border-accent', 'text-accent');
            this.classList.remove('border-transparent', 'text-muted-foreground');
            
            // Mostra conteúdo correspondente
            const conteudo = document.getElementById(`conteudo-${abaId}`);
            if (conteudo) {
                conteudo.classList.remove('hidden');
            }
        });
    });

    // Navegação entre dias da semana
    const diasSemana = document.querySelectorAll('[data-dia]');
    diasSemana.forEach(dia => {
        dia.addEventListener('click', function() {
            diasSemana.forEach(d => {
                d.classList.remove('bg-accent', 'text-accent-foreground');
                d.classList.add('bg-muted', 'text-muted-foreground');
            });
            
            this.classList.add('bg-accent', 'text-accent-foreground');
            this.classList.remove('bg-muted', 'text-muted-foreground');
        });
    });

    // Busca de alimentos
    const inputsBusca = document.querySelectorAll('input[placeholder*="Buscar alimento"]');
    inputsBusca.forEach(input => {
        let timeoutId;
        
        input.addEventListener('input', function() {
            clearTimeout(timeoutId);
            const query = this.value.trim();
            
            if (query.length >= 2) {
                timeoutId = setTimeout(() => {
                    buscarAlimentos(query, this);
                }, 300);
            } else {
                ocultarResultadosBusca(this);
            }
        });

        // Fechar resultados quando clicar fora
        document.addEventListener('click', function(event) {
            if (!input.contains(event.target)) {
                ocultarResultadosBusca(input);
            }
        });
    });

    // Adicionar/remover favoritos
    document.addEventListener('click', function(event) {
        if (event.target.classList.contains('btn-favorito')) {
            toggleFavorito(event.target);
        }
    });

    // Adicionar nova refeição
    const btnNovaRefeicao = document.querySelector('#btn-nova-refeicao');
    if (btnNovaRefeicao) {
        btnNovaRefeicao.addEventListener('click', adicionarRefeicao);
    }

    // Recalcular macros
    const btnRecalcular = document.querySelector('#btn-recalcular');
    if (btnRecalcular) {
        btnRecalcular.addEventListener('click', recalcularMacros);
    }

    // Integração com tema do dashboard
    integrarComTemaDashboard();
});

function buscarAlimentos(query, inputElement) {
    // Simulação de busca - em produção faria requisição AJAX
    const alimentos = [
        { id: 1, nome: 'Frango, peito, grelhado', categoria: 'Carnes', calorias: 165, proteinas: 31, carboidratos: 0, gorduras: 3.6 },
        { id: 2, nome: 'Arroz integral, cozido', categoria: 'Cereais', calorias: 123, proteinas: 2.6, carboidratos: 25.8, gorduras: 1 },
        { id: 3, nome: 'Banana, prata', categoria: 'Frutas', calorias: 98, proteinas: 1.3, carboidratos: 26, gorduras: 0.1 },
        { id: 4, nome: 'Ovo, galinha, cozido', categoria: 'Ovos', calorias: 155, proteinas: 13, carboidratos: 1.1, gorduras: 10.6 }
    ];

    const resultados = alimentos.filter(alimento => 
        alimento.nome.toLowerCase().includes(query.toLowerCase())
    );

    mostrarResultadosBusca(resultados, inputElement);
}

function mostrarResultadosBusca(resultados, inputElement) {
    // Remove dropdown existente
    ocultarResultadosBusca(inputElement);

    if (resultados.length === 0) {
        return;
    }

    const dropdown = document.createElement('div');
    dropdown.className = 'resultados-busca absolute top-full mt-1 w-full bg-card border border-border rounded-lg shadow-xl z-20 max-h-64 overflow-auto';
    
    resultados.forEach(alimento => {
        const item = document.createElement('div');
        item.className = 'p-2 hover:bg-muted cursor-pointer border-b border-border last:border-0 flex items-center justify-between';
        item.innerHTML = `
            <div class="flex-1" onclick="adicionarAlimento(${alimento.id}, '${alimento.nome}', ${alimento.calorias}, ${alimento.proteinas}, ${alimento.carboidratos}, ${alimento.gorduras})">
                <div class="font-semibold text-xs text-foreground">${alimento.nome}</div>
                <div class="text-xs text-muted-foreground">${alimento.categoria} • ${alimento.calorias}kcal • P:${alimento.proteinas}g C:${alimento.carboidratos}g G:${alimento.gorduras}g</div>
            </div>
            <button class="btn-favorito p-1 hover:bg-muted rounded transition" onclick="toggleFavorito(this)">
                <i class="fas fa-star w-4 h-4 text-muted-foreground"></i>
            </button>
        `;
        dropdown.appendChild(item);
    });

    // Posicionar dropdown
    const container = inputElement.closest('td') || inputElement.parentElement;
    container.style.position = 'relative';
    container.appendChild(dropdown);
}

function ocultarResultadosBusca(inputElement) {
    const container = inputElement.closest('td') || inputElement.parentElement;
    const dropdown = container.querySelector('.resultados-busca');
    if (dropdown) {
        dropdown.remove();
    }
}

function adicionarAlimento(id, nome, calorias, proteinas, carboidratos, gorduras) {
    console.log('Adicionando alimento:', nome);
    // Aqui você adicionaria o alimento à refeição
    // Em produção, faria uma requisição AJAX ou atualizaria o estado
    
    // Limpar input de busca
    const inputs = document.querySelectorAll('input[placeholder*="Buscar alimento"]');
    inputs.forEach(input => {
        input.value = '';
        ocultarResultadosBusca(input);
    });
}

function toggleFavorito(botao) {
    const icon = botao.querySelector('i');
    const isFavorito = icon.classList.contains('text-yellow-500');
    
    if (isFavorito) {
        icon.classList.remove('text-yellow-500', 'fas');
        icon.classList.add('text-muted-foreground', 'far');
    } else {
        icon.classList.add('text-yellow-500', 'fas');
        icon.classList.remove('text-muted-foreground', 'far');
    }
}

function adicionarRefeicao() {
    console.log('Adicionando nova refeição...');
    // Em produção, criaria dinamicamente uma nova seção de refeição
}

function recalcularMacros() {
    console.log('Recalculando macros...');
    // Em produção, faria cálculos baseados nos alimentos selecionados
}

function integrarComTemaDashboard() {
    // Verifica se já existe um tema salvo no localStorage
    const temaAtual = localStorage.getItem('theme');
    
    if (temaAtual === 'light') {
        document.body.classList.add('light-mode');
    }

    // Observer para mudanças no tema do dashboard
    const observer = new MutationObserver(function(mutations) {
        mutations.forEach(function(mutation) {
            if (mutation.type === 'attributes' && mutation.attributeName === 'class') {
                const hasLightMode = document.body.classList.contains('light-mode');
                console.log('Dieta Plano - Tema alterado:', hasLightMode ? 'claro' : 'escuro');
            }
        });
    });

    // Observar mudanças na classe do body
    observer.observe(document.body, {
        attributes: true,
        attributeFilter: ['class']
    });

    console.log('Dieta Plano: Integração com tema do dashboard ativada');
}

// Funções utilitárias para manipulação de dados
function calcularTotaisRefeicao(alimentos) {
    return alimentos.reduce((total, alimento) => {
        total.calorias += alimento.calorias * (alimento.quantidade / alimento.porcao);
        total.proteinas += alimento.proteinas * (alimento.quantidade / alimento.porcao);
        total.carboidratos += alimento.carboidratos * (alimento.quantidade / alimento.porcao);
        total.gorduras += alimento.gorduras * (alimento.quantidade / alimento.porcao);
        return total;
    }, { calorias: 0, proteinas: 0, carboidratos: 0, gorduras: 0 });
}

function formatarNumero(numero, casasDecimais = 1) {
    return Math.round(numero * Math.pow(10, casasDecimais)) / Math.pow(10, casasDecimais);
}