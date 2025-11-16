/* ==========================================
   DESIGN SYSTEM JS - NutriXpert Pro
   JavaScript para funcionalidades do sistema
   ========================================== */

// ===== THEME SYSTEM =====
class ThemeManager {
    constructor() {
        this.currentTheme = localStorage.getItem('theme') || 'dark';
        this.init();
    }

    init() {
        this.applyTheme(this.currentTheme);
        this.updateToggleIcon();
    }

    toggle() {
        this.currentTheme = this.currentTheme === 'dark' ? 'light' : 'dark';
        this.applyTheme(this.currentTheme);
        this.updateToggleIcon();
        localStorage.setItem('theme', this.currentTheme);
    }

    applyTheme(theme) {
        if (theme === 'light') {
            document.body.classList.add('light-mode');
        } else {
            document.body.classList.remove('light-mode');
        }
    }

    updateToggleIcon() {
        const toggleBtn = document.getElementById('themeToggleBtn');
        if (toggleBtn) {
            const icon = toggleBtn.querySelector('i');
            if (this.currentTheme === 'light') {
                icon.className = 'fas fa-moon';
            } else {
                icon.className = 'fas fa-sun';
            }
        }
    }
}

// ===== VOICE SYSTEM =====
class VoiceManager {
    constructor() {
        this.isActive = false;
        this.recognition = null;
        this.synthesis = window.speechSynthesis;
        this.init();
    }

    init() {
        if ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window) {
            const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
            this.recognition = new SpeechRecognition();
            this.recognition.continuous = false;
            this.recognition.interimResults = false;
            this.recognition.lang = 'pt-BR';

            this.recognition.onresult = (event) => {
                const transcript = event.results[0][0].transcript;
                this.processVoiceCommand(transcript);
            };

            this.recognition.onerror = (event) => {
                console.error('Erro no reconhecimento de voz:', event.error);
                this.stop();
            };
        }
    }

    toggle() {
        if (this.isActive) {
            this.stop();
        } else {
            this.start();
        }
    }

    start() {
        if (!this.recognition) {
            showError('Voz não suportada', 'Seu navegador não suporta reconhecimento de voz.');
            return;
        }

        this.isActive = true;
        this.recognition.start();
        this.updateToggleButton();
        
        showInfo('Voz ativada', 'Diga um comando...');
    }

    stop() {
        if (this.recognition) {
            this.recognition.stop();
        }
        this.isActive = false;
        this.updateToggleButton();
    }

    updateToggleButton() {
        const voiceBtn = document.getElementById('voiceBtn');
        if (voiceBtn) {
            if (this.isActive) {
                voiceBtn.classList.add('active');
            } else {
                voiceBtn.classList.remove('active');
            }
        }
    }

    processVoiceCommand(command) {
        const lowerCommand = command.toLowerCase();
        
        // Comandos de navegação
        if (lowerCommand.includes('dashboard') || lowerCommand.includes('painel')) {
            window.location.href = '/users/dashboard/';
            this.speak('Navegando para o dashboard');
        } else if (lowerCommand.includes('pacientes')) {
            window.location.href = '/patients/';
            this.speak('Navegando para pacientes');
        } else if (lowerCommand.includes('consultas')) {
            window.location.href = '/appointments/';
            this.speak('Navegando para consultas');
        } else if (lowerCommand.includes('dietas')) {
            window.location.href = '/diets/';
            this.speak('Navegando para dietas');
        } else if (lowerCommand.includes('tema')) {
            themeManager.toggle();
            this.speak('Tema alterado');
        } else {
            this.speak('Comando não reconhecido');
        }

        this.stop();
    }

    speak(text) {
        if (this.synthesis) {
            const utterance = new SpeechSynthesisUtterance(text);
            utterance.lang = 'pt-BR';
            utterance.rate = 0.9;
            this.synthesis.speak(utterance);
        }
    }
}

// ===== SEARCH SYSTEM =====
class SearchManager {
    constructor() {
        this.searchInput = document.getElementById('searchInput');
        this.debounceTimer = null;
        this.init();
    }

    init() {
        if (this.searchInput) {
            this.searchInput.addEventListener('input', (e) => {
                clearTimeout(this.debounceTimer);
                this.debounceTimer = setTimeout(() => {
                    this.performSearch(e.target.value);
                }, 300);
            });
        }
    }

    performSearch(query) {
        if (query.length < 2) return;

        // Aqui você implementaria a busca real
        console.log('Buscando:', query);
        
        // Exemplo de busca inteligente
        const suggestions = this.getSearchSuggestions(query);
        this.showSearchSuggestions(suggestions);
    }

    getSearchSuggestions(query) {
        // Mock de sugestões - implementar com dados reais
        const mockData = [
            { type: 'patient', name: 'João Silva', id: 1 },
            { type: 'patient', name: 'Maria Santos', id: 2 },
            { type: 'diet', name: 'Dieta Low Carb', id: 1 },
            { type: 'appointment', name: 'Consulta 15/11', id: 1 }
        ];

        return mockData.filter(item => 
            item.name.toLowerCase().includes(query.toLowerCase())
        );
    }

    showSearchSuggestions(suggestions) {
        // Implementar dropdown de sugestões
        console.log('Sugestões:', suggestions);
    }
}

// ===== DRAG & DROP SYSTEM =====
class DragDropManager {
    constructor() {
        this.init();
    }

    init() {
        // Implementar funcionalidades de drag & drop para agendamentos
        document.addEventListener('dragstart', this.handleDragStart.bind(this));
        document.addEventListener('dragover', this.handleDragOver.bind(this));
        document.addEventListener('drop', this.handleDrop.bind(this));
    }

    handleDragStart(e) {
        if (e.target.classList.contains('timeline-item')) {
            e.dataTransfer.setData('text/plain', e.target.id);
            e.target.style.opacity = '0.5';
        }
    }

    handleDragOver(e) {
        e.preventDefault();
        e.dataTransfer.dropEffect = 'move';
    }

    handleDrop(e) {
        e.preventDefault();
        const draggedId = e.dataTransfer.getData('text/plain');
        const draggedElement = document.getElementById(draggedId);
        
        if (draggedElement) {
            draggedElement.style.opacity = '';
            // Implementar lógica de reordenação
            showSuccess('Agendamento movido', 'Horário atualizado com sucesso!');
        }
    }
}

// ===== CHART MANAGER =====
class ChartManager {
    constructor() {
        this.charts = {};
        this.init();
    }

    init() {
        this.initEvolutionChart();
    }

    initEvolutionChart() {
        const evolutionChartElement = document.getElementById('evolutionChart');
        if (!evolutionChartElement) return;

        const ctx = evolutionChartElement.getContext('2d');
        
        const chartData = {
            labels: ['Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro'],
            peso: {
                label: 'Peso (kg)',
                data: [78, 79, 81, 80, 78, 77],
                borderColor: '#3b82f6',
                backgroundColor: 'rgba(59, 130, 246, 0.1)',
            },
            imc: {
                label: 'IMC',
                data: [24.1, 24.4, 25.0, 24.7, 24.1, 23.8],
                borderColor: '#10b981',
                backgroundColor: 'rgba(16, 185, 129, 0.1)',
            },
            massa: {
                label: 'Massa Muscular (kg)',
                data: [55, 55.2, 55.8, 56, 55.5, 55.3],
                borderColor: '#A52A2A',
                backgroundColor: 'rgba(165, 42, 42, 0.3)',
            },
            gordura: {
                label: '% Gordura Corporal',
                data: [22, 22.5, 23, 22.8, 22.2, 21.8],
                borderColor: '#FFD700',
                backgroundColor: 'rgba(255, 215, 0, 0.2)',
            }
        };

        this.charts.evolution = new Chart(ctx, {
            type: 'line',
            data: {
                labels: chartData.labels,
                datasets: [{
                    label: chartData.peso.label,
                    data: chartData.peso.data,
                    borderColor: chartData.peso.borderColor,
                    backgroundColor: chartData.peso.backgroundColor,
                    borderWidth: 3,
                    pointBackgroundColor: 'white',
                    pointBorderColor: chartData.peso.borderColor,
                    pointBorderWidth: 2,
                    pointRadius: 5,
                    tension: 0.4,
                    fill: true,
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        display: false
                    }
                },
                scales: {
                    x: {
                        grid: { display: false },
                        ticks: { color: '#64748b' }
                    },
                    y: {
                        grid: { color: '#334155' },
                        ticks: { color: '#64748b' }
                    }
                }
            }
        });

        // Função global para atualizar o gráfico
        window.updateEvolutionChart = (metric) => {
            const metricData = chartData[metric];
            
            this.charts.evolution.data.datasets[0].label = metricData.label;
            this.charts.evolution.data.datasets[0].data = metricData.data;
            this.charts.evolution.data.datasets[0].borderColor = metricData.borderColor;
            this.charts.evolution.data.datasets[0].backgroundColor = metricData.backgroundColor;
            this.charts.evolution.data.datasets[0].pointBorderColor = metricData.borderColor;
            this.charts.evolution.update();

            // Atualizar botões ativos
            document.querySelectorAll('.metric-btn').forEach(btn => {
                btn.classList.remove('active');
            });
            document.querySelector(`.metric-btn[onclick="updateEvolutionChart('${metric}')"]`)?.classList.add('active');
        };
    }

    updateThemeColors() {
        const isLightMode = document.body.classList.contains('light-mode');
        const textColor = isLightMode ? '#999999' : '#64748b';
        const gridColor = isLightMode ? '#D3D3D3' : '#334155';

        Object.values(this.charts).forEach(chart => {
            if (chart.options.scales) {
                if (chart.options.scales.x) {
                    chart.options.scales.x.ticks.color = textColor;
                }
                if (chart.options.scales.y) {
                    chart.options.scales.y.ticks.color = textColor;
                    chart.options.scales.y.grid.color = gridColor;
                }
                chart.update();
            }
        });
    }
}

// ===== AI INSIGHTS SYSTEM =====
class AIInsightsManager {
    constructor() {
        this.init();
    }

    init() {
        // Implementar sistema de insights de IA
    }

    generateInsight() {
        showInfo('IA Processando', 'Analisando dados do paciente...');
        
        // Simular processamento
        setTimeout(() => {
            const insights = [
                'Paciente apresenta padrão irregular de sono. Recomendar ajustes na dieta.',
                'Tendência de aumento de massa muscular. Manter protocolo atual.',
                'Deficiência de vitamina D detectada. Considerar suplementação.',
                'Progresso acima da meta. Parabenizar paciente na próxima consulta.'
            ];
            
            const randomInsight = insights[Math.floor(Math.random() * insights.length)];
            showSuccess('Insight IA', randomInsight, { duration: 8000 });
        }, 2000);
    }

    applyAIPlan() {
        showSuccess('Plano IA Aplicado', 'Recomendações foram adicionadas ao prontuário do paciente.');
    }
}

// ===== TASK MANAGER =====
class TaskManager {
    constructor() {
        this.tasks = [];
        this.init();
    }

    init() {
        // Implementar sistema de tarefas
    }

    completeTask(taskId) {
        const taskElement = document.querySelector(`[onclick="completeTask(${taskId})"]`);
        if (taskElement) {
            taskElement.style.opacity = '0.5';
            taskElement.style.textDecoration = 'line-through';
            
            setTimeout(() => {
                taskElement.style.display = 'none';
                showSuccess('Tarefa Concluída', 'Item removido da lista de pendências.');
            }, 1000);
        }
    }
}

// ===== INICIALIZAÇÃO =====
let themeManager, voiceManager, searchManager, dragDropManager, chartManager, aiInsightsManager, taskManager;

document.addEventListener('DOMContentLoaded', function() {
    // Inicializar sistemas
    themeManager = new ThemeManager();
    voiceManager = new VoiceManager();
    searchManager = new SearchManager();
    dragDropManager = new DragDropManager();
    chartManager = new ChartManager();
    aiInsightsManager = new AIInsightsManager();
    taskManager = new TaskManager();

    // Event listeners globais
    document.addEventListener('themeChanged', () => {
        chartManager.updateThemeColors();
    });

    // Funções globais
    window.toggleTheme = () => {
        themeManager.toggle();
        document.dispatchEvent(new CustomEvent('themeChanged'));
    };

    window.toggleVoice = () => {
        voiceManager.toggle();
    };

    window.generatePlan = () => {
        aiInsightsManager.generateInsight();
    };

    window.applyAIPlan = () => {
        aiInsightsManager.applyAIPlan();
    };

    window.completeTask = (taskId) => {
        taskManager.completeTask(taskId);
    };

    window.aiAction = (action) => {
        showInfo('IA Ativada', `Executando ação: ${action}`);
    };

    // Modal functions
    window.openModal = (patientName) => {
        const modal = document.getElementById('patientModal');
        if (modal) {
            const modalTitle = document.getElementById('modalTitle');
            if (modalTitle) {
                modalTitle.textContent = `Detalhes - ${patientName}`;
            }
            modal.classList.add('active');
            document.body.style.overflow = 'hidden';
        }
    };

    window.closeModal = () => {
        const modals = document.querySelectorAll('.overlay.active');
        modals.forEach(modal => {
            modal.classList.remove('active');
        });
        document.body.style.overflow = '';
    };

    // Drag & Drop functions
    window.allowDrop = (ev) => {
        ev.preventDefault();
    };

    window.drag = (ev) => {
        ev.dataTransfer.setData("text", ev.target.id);
    };

    window.drop = (ev) => {
        ev.preventDefault();
        const data = ev.dataTransfer.getData("text");
        showInfo('Agendamento', 'Horário reorganizado!');
    };

    console.log('✅ Design System inicializado com sucesso!');
});