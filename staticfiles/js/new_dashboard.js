// Inicialização da Data Atual e Saudação (agora vêm do Django)

// Theme Toggle Logic
function toggleTheme() {
    document.body.classList.toggle('light-mode');
    const isLightMode = document.body.classList.contains('light-mode');
    localStorage.setItem('theme', isLightMode ? 'light' : 'dark');

    // Force chart to update with new theme colors
    if (window.evolutionChart) {
        const newTextColor = isLightMode ? '#999999' : '#64748b'; // --text-muted values
        const newGridColor = isLightMode ? '#D3D3D3' : '#334155'; // --border values
        
        evolutionChart.options.scales.x.ticks.color = newTextColor;
        evolutionChart.options.scales.y.ticks.color = newTextColor;
        evolutionChart.options.scales.y.grid.color = newGridColor;
        evolutionChart.update();
    }
}

let evolutionChart;

// Apply saved theme on load
document.addEventListener('DOMContentLoaded', () => {
    const savedTheme = localStorage.getItem('theme');
    const isLightMode = savedTheme === 'light';
    if (isLightMode) {
        document.body.classList.add('light-mode');
    }

    // Gráfico de Evolução com Chart.js
    const evolutionChartElement = document.getElementById('evolutionChart');
    if (evolutionChartElement) {
        const evolutionChartCtx = evolutionChartElement.getContext('2d');

        const chartData = {
            labels: ['Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro'],
            peso: {
                label: 'Peso (kg)',
                data: [78, 79, 81, 80, 78, 77],
                borderColor: '#3b82f6', // Blue
                backgroundColor: 'rgba(59, 130, 246, 0.1)',
            },
            imc: {
                label: 'IMC',
                data: [24.1, 24.4, 25.0, 24.7, 24.1, 23.8],
                borderColor: '#10b981', // Green
                backgroundColor: 'rgba(16, 185, 129, 0.1)',
            },
            massa: {
                label: 'Massa Muscular (kg)',
                data: [55, 55.2, 55.8, 56, 55.5, 55.3],
                borderColor: '#A52A2A', // Dark red
                backgroundColor: 'rgba(165, 42, 42, 0.3)',
            },
            gordura: {
                label: '% Gordura Corporal',
                data: [22, 22.5, 23, 22.8, 22.2, 21.8],
                borderColor: '#FFD700', // Yellow
                backgroundColor: 'rgba(255, 215, 0, 0.2)',
            }
        };

        evolutionChart = new Chart(evolutionChartCtx, {
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
                        grid: {
                            display: false
                        },
                        ticks: {
                            color: '#64748b' // Initial dark mode color
                        }
                    },
                    y: {
                        grid: {
                            color: '#334155' // Initial dark mode color
                        },
                        ticks: {
                            color: '#64748b' // Initial dark mode color
                        }
                    }
                }
            }
        });

        // Set initial text color based on theme
        if (isLightMode) {
            const initialTextColor = '#999999';
            const initialGridColor = '#D3D3D3';
            evolutionChart.options.scales.x.ticks.color = initialTextColor;
            evolutionChart.options.scales.y.ticks.color = initialTextColor;
            evolutionChart.options.scales.y.grid.color = initialGridColor;
            evolutionChart.update();
        }
    }

    window.updateEvolutionChart = function(metric) {
        const metricData = chartData[metric];
        
        evolutionChart.data.datasets[0].label = metricData.label;
        evolutionChart.data.datasets[0].data = metricData.data;
        evolutionChart.data.datasets[0].borderColor = metricData.borderColor;
        evolutionChart.data.datasets[0].backgroundColor = metricData.backgroundColor;
        evolutionChart.data.datasets[0].pointBorderColor = metricData.borderColor;
        evolutionChart.update();

        document.querySelectorAll('.metric-btn').forEach(btn => {
            btn.classList.remove('active');
        });
        document.querySelector(`.metric-btn[onclick="updateEvolutionChart('${metric}')"]`).classList.add('active');
    }

    window.updateChart = function() {
        const period = document.getElementById('periodSelect').value;
        if (period === 'Últimos 3 meses') {
            evolutionChart.data.labels = ['Ago', 'Set', 'Out', 'Nov'];
        } else {
            evolutionChart.data.labels = chartData.labels;
        }
        evolutionChart.update();
    }

    // O resto do seu código DOMContentLoaded...
});