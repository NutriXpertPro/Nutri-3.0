import React, { useState } from 'react';
import ReactDOM from 'react-dom/client';
import { LineChart, Line, RadarChart, Radar, PolarGrid, PolarAngleAxis, PolarRadiusAxis, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, AreaChart, Area } from 'recharts';
import { TrendingDown, TrendingUp, Minus, Calendar, Camera, FileText, Utensils, Activity, Zap, Target, ChevronDown, ChevronUp, GitCompare, Sparkles, BarChart3, FileBarChart, Scale } from 'lucide-react';

const NutritionCommandCenter = (props) => {
  const {
    patient: patientData,
    metrics: currentMetrics,
    radar: radarData,
    evolution: evolutionData,
    labExams: labExamsHistory = [], // ✅ CORREÇÃO: Valor padrão como array vazio
    dietHistory = [], // ✅ CORREÇÃO: Valor padrão
    macrosEvolution = [], // ✅ CORREÇÃO: Valor padrão
    consultations = [] // ✅ CORREÇÃO: Valor padrão
  } = props;

  const [expandedConsultation, setExpandedConsultation] = useState(null);
  const [compareMode, setCompareMode] = useState(false);
  const [selectedCompare, setSelectedCompare] = useState([]);
  const [activeView, setActiveView] = useState('dashboard');

  const MetricCard = ({ label, data, icon: Icon }) => {
    const getColor = () => {
      if (data.trend === 'down' && (label === 'Peso' || label === 'Gordura' || label === 'IMC' || label === 'Abdômen')) return 'text-green-600';
      if (data.trend === 'up' && label === 'Músculo') return 'text-green-600';
      if (data.trend === 'up') return 'text-red-600';
      return 'text-gray-600';
    };
    
    const TrendIcon = data.trend === 'down' ? TrendingDown : data.trend === 'up' ? TrendingUp : Minus;
    
    return (
      <div className="bg-white rounded-xl shadow-lg p-6 border-2 border-gray-100 hover:shadow-2xl transition-all duration-300 hover:scale-105">
        <div className="flex items-center justify-between mb-4">
          <div className="flex items-center gap-2">
            <Icon className="w-5 h-5 text-blue-600" />
            <span className="text-sm font-medium text-gray-600">{label}</span>
          </div>
          <TrendIcon className={`w-6 h-6 ${getColor()}`} />
        </div>
        <div className="flex items-end justify-between mb-3">
          <div>
            <div className="text-3xl font-bold text-gray-800">{data.atual}</div>
            <div className="text-xs text-gray-500">atual</div>
          </div>
          <div className={`text-2xl font-bold ${getColor()}`}>
            {data.mudanca > 0 ? '+' : ''}{data.mudanca}
          </div>
          <div className="text-right">
            <div className="text-lg text-gray-600">{data.inicial}</div>
            <div className="text-xs text-gray-500">inicial</div>
          </div>
        </div>
        <div className="w-full bg-gray-200 rounded-full h-2">
          <div
            className={`h-2 rounded-full ${data.trend === 'down' ? 'bg-green-500' : 'bg-blue-500'}`}
            style={{ width: `${Math.abs((data.mudanca / data.inicial) * 100)}%` }}
          />
        </div>
        {data.objetivo && (
          <div className="text-xs text-gray-500 mt-2 text-center">
            Meta: {data.objetivo}kg
          </div>
        )}
      </div>
    );
  };

  const ConsultationCard = ({ consultation }) => {
    const isExpanded = expandedConsultation === consultation.id;
    const isSelected = selectedCompare.includes(consultation.id);

    return (
      <div className={`bg-white rounded-xl shadow-md border-2 ${consultation.isFirst ? 'border-purple-400' : isSelected ? 'border-blue-500' : 'border-gray-200'} mb-4 overflow-hidden transition-all duration-300`}>
        <div
          className="p-5 cursor-pointer hover:bg-gray-50"
          onClick={() => setExpandedConsultation(isExpanded ? null : consultation.id)}
        >
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-4">
              {compareMode && (
                <input
                  type="checkbox"
                  checked={isSelected}
                  onChange={(e) => {
                    e.stopPropagation();
                    if (isSelected) {
                      setSelectedCompare(selectedCompare.filter(id => id !== consultation.id));
                    } else if (selectedCompare.length < 2) {
                      setSelectedCompare([...selectedCompare, consultation.id]);
                    }
                  }}
                  className="w-5 h-5"
                />
              )}
              <div className={`w-3 h-3 rounded-full ${consultation.isFirst ? 'bg-purple-500' : 'bg-blue-500'}`} />
              <div>
                <div className="flex items-center gap-2">
                  <Calendar className="w-4 h-4 text-gray-500" />
                  <span className="font-bold text-gray-800">{consultation.data}</span>
                  {consultation.isFirst && (
                    <span className="text-xs bg-purple-100 text-purple-700 px-2 py-1 rounded-full font-semibold">
                      🎬 INÍCIO DA JORNADA
                    </span>
                  )}
                </div>
                <div className="text-sm text-gray-500">
                  {consultation.diasAtras === 0 ? 'Hoje' : `${consultation.diasAtras} dias atrás`} • Consulta #{consultation.id}
                </div>
              </div>
            </div>
            <div className="flex items-center gap-4">
              <div className="text-right">
                <div className="text-lg font-bold text-gray-800">{consultation.peso}kg</div>
                <div className="text-sm text-gray-500">{consultation.gordura}% gordura</div>
              </div>
              {isExpanded ? <ChevronUp className="w-5 h-5" /> : <ChevronDown className="w-5 h-5" />}
            </div>
          </div>
        </div>

        {isExpanded && (
          <div className="border-t border-gray-200 p-5 bg-gray-50">
            <div className="grid grid-cols-2 sm:grid-cols-4 gap-4 mb-4">
              <div className="text-center p-3 bg-white rounded-lg">
                <div className="text-xs text-gray-500 mb-1">Músculo</div>
                <div className="text-lg font-bold text-green-600">{consultation.musculo}kg</div>
              </div>
              <div className="text-center p-3 bg-white rounded-lg">
                <div className="text-xs text-gray-500 mb-1">IMC</div>
                <div className="text-lg font-bold text-blue-600">{consultation.imc}</div>
              </div>
              <div className="text-center p-3 bg-white rounded-lg">
                <div className="text-xs text-gray-500 mb-1">Cintura</div>
                <div className="text-lg font-bold text-purple-600">{consultation.medidas.cintura}cm</div>
              </div>
              <div className="text-center p-3 bg-white rounded-lg">
                <div className="text-xs text-gray-500 mb-1">Abdômen</div>
                <div className="text-lg font-bold text-orange-600">{consultation.medidas.abdomen}cm</div>
              </div>
            </div>

            <div className="bg-blue-50 p-4 rounded-lg mb-4">
              <div className="text-sm font-semibold text-blue-900 mb-2">Observações Clínicas:</div>
              <div className="text-sm text-blue-800">{consultation.observacoes}</div>
            </div>

            <div className="flex gap-2 flex-wrap">
              {consultation.fotos && (
                <button className="flex items-center gap-2 px-4 py-2 bg-purple-600 text-white rounded-lg hover:bg-purple-700 transition-colors">
                  <Camera className="w-4 h-4" />
                  Ver Fotos Evolutivas
                </button>
              )}
              {consultation.exames && (
                <button className="flex items-center gap-2 px-4 py-2 bg-red-600 text-white rounded-lg hover:bg-red-700 transition-colors">
                  <FileText className="w-4 h-4" />
                  Exames Laboratoriais
                </button>
              )}
              <button className="flex items-center gap-2 px-4 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700 transition-colors">
                <Utensils className="w-4 h-4" />
                {consultation.dieta}
              </button>
            </div>
          </div>
        )}
      </div>
    );
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-purple-50 to-pink-50 dark:bg-gray-900">
      <div className="sticky top-0 z-50 bg-white dark:bg-gray-800 shadow-lg border-b-4 border-blue-600">
        <div className="max-w-7xl mx-auto px-6 py-4">
          <div className="flex items-center justify-between mb-3">
            <div>
              <h1 className="text-3xl font-bold text-gray-800">{patientData.nome}</h1>
              <div className="flex items-center gap-4 text-sm text-gray-600 mt-1">
                <span>{patientData.idade} anos</span>
                <span>•</span>
                <span>{patientData.objetivo}</span>
                <span>•</span>
                <span className="font-semibold text-blue-600">{patientData.consultasTotal} consultas</span>
              </div>
            </div>
            <div className="flex gap-2">
              <button
                onClick={() => setCompareMode(!compareMode)}
                className={`flex items-center gap-2 px-4 py-2 rounded-lg font-semibold transition-colors ${
                  compareMode ? 'bg-blue-600 text-white' : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
                }`}
              >
                <GitCompare className="w-5 h-5" />
                Modo Comparação
              </button>
              <button className="flex items-center gap-2 px-4 py-2 bg-gradient-to-r from-purple-600 to-pink-600 text-white rounded-lg hover:from-purple-700 hover:to-pink-700 font-semibold">
                <Sparkles className="w-5 h-5" />
                IA Insights
              </button>
            </div>
          </div>

          <div className="flex gap-2">
            <button
              onClick={() => setActiveView('dashboard')}
              className={`px-4 py-2 rounded-lg font-medium transition-colors ${
                activeView === 'dashboard' ? 'bg-blue-600 text-white' : 'bg-gray-100 text-gray-600 hover:bg-gray-200'
              }`}
            >
              Dashboard Analítico
            </button>
            <button
              onClick={() => setActiveView('timeline')}
              className={`px-4 py-2 rounded-lg font-medium transition-colors ${
                activeView === 'timeline' ? 'bg-blue-600 text-white' : 'bg-gray-100 text-gray-600 hover:bg-gray-200'
              }`}
            >
              Timeline Evolutiva
            </button>
          </div>
        </div>
      </div>

      <div className="max-w-7xl mx-auto px-6 py-8">
        {activeView === 'dashboard' && (
          <>
            <div className="bg-white rounded-2xl shadow-2xl p-8 mb-8 border-4 border-blue-100">
              <h2 className="text-2xl font-bold text-gray-800 mb-6 flex items-center gap-3">
                <Zap className="w-7 h-7 text-yellow-500" />
                Dashboard Analítico - Visão Geral da Jornada
              </h2>

              <div className="mb-8">
                <h3 className="text-lg font-semibold text-gray-700 mb-4 flex items-center gap-2">
                  <Camera className="w-5 h-5" /> Transformação Visual
                </h3>
                <div className="grid grid-cols-3 gap-6">
                  <div className="text-center">
                    <div className="bg-gradient-to-br from-gray-300 to-gray-400 rounded-xl aspect-[3/4] mb-3 flex items-center justify-center">
                      <div className="text-center">
                        <Camera className="w-12 h-12 text-white mx-auto mb-2" />
                        <div className="text-white font-bold">FRONTAL</div>
                        <div className="text-sm text-gray-200">Antes → Depois</div>
                      </div>
                    </div>
                    <div className="text-sm font-semibold text-gray-600">Visão Frontal</div>
                  </div>
                  <div className="text-center">
                    <div className="bg-gradient-to-br from-blue-300 to-blue-400 rounded-xl aspect-[3/4] mb-3 flex items-center justify-center">
                      <div className="text-center">
                        <Camera className="w-12 h-12 text-white mx-auto mb-2" />
                        <div className="text-white font-bold">LATERAL</div>
                        <div className="text-sm text-gray-200">Antes → Depois</div>
                      </div>
                    </div>
                    <div className="text-sm font-semibold text-gray-600">Visão Lateral</div>
                  </div>
                  <div className="text-center">
                    <div className="bg-gradient-to-br from-purple-300 to-purple-400 rounded-xl aspect-[3/4] mb-3 flex items-center justify-center">
                      <div className="text-center">
                        <Camera className="w-12 h-12 text-white mx-auto mb-2" />
                        <div className="text-white font-bold">COSTAS</div>
                        <div className="text-sm text-gray-200">Antes → Depois</div>
                      </div>
                    </div>
                    <div className="text-sm font-semibold text-gray-600">Visão Posterior</div>
                  </div>
                </div>
              </div>

              <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-4 mb-8">
                <MetricCard label="Peso" data={currentMetrics.peso} icon={Scale} />
                <MetricCard label="Gordura" data={currentMetrics.gordura} icon={TrendingDown} />
                <MetricCard label="Músculo" data={currentMetrics.musculo} icon={TrendingUp} />
                <MetricCard label="IMC" data={currentMetrics.imc} icon={Target} />
                <MetricCard label="Abdômen" data={currentMetrics.abdomen} icon={Activity} />
              </div>

              <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-8">
                <div className="bg-gray-50 rounded-xl p-6">
                  <h3 className="text-lg font-bold text-gray-800 mb-4 flex items-center gap-2">
                    <BarChart3 className="w-5 h-5" /> Radar Corporal - Evolução de Medidas
                  </h3>
                  <ResponsiveContainer width="100%" height={300}>
                    <RadarChart data={radarData}>
                      <PolarGrid stroke="#e5e7eb" />
                      <PolarAngleAxis dataKey="metrica" tick={{ fill: '#6b7280', fontSize: 12 }} />
                      <PolarRadiusAxis angle={90} domain={[0, 'dataMax']} />
                      <Radar name="Inicial" dataKey="inicial" stroke="#ef4444" fill="#ef4444" fillOpacity={0.3} />
                      <Radar name="Atual" dataKey="atual" stroke="#10b981" fill="#10b981" fillOpacity={0.5} />
                      <Legend />
                      <Tooltip />
                    </RadarChart>
                  </ResponsiveContainer>
                </div>

                <div className="bg-gray-50 rounded-xl p-6">
                  <h3 className="text-lg font-bold text-gray-800 mb-4 flex items-center gap-2">
                    <TrendingUp className="w-5 h-5" /> Evolução de Composição Corporal
                  </h3>
                  <ResponsiveContainer width="100%" height={300}>
                    <LineChart data={evolutionData}>
                      <CartesianGrid strokeDasharray="3 3" stroke="#e5e7eb" />
                      <XAxis dataKey="data" tick={{ fill: '#6b7280', fontSize: 11 }} />
                      <YAxis yAxisId="left" tick={{ fill: '#6b7280', fontSize: 11 }} />
                      <YAxis yAxisId="right" orientation="right" tick={{ fill: '#6b7280', fontSize: 11 }} />
                      <Tooltip />
                      <Legend />
                      <Line yAxisId="left" type="monotone" dataKey="peso" stroke="#3b82f6" strokeWidth={3} name="Peso (kg)" />
                      <Line yAxisId="right" type="monotone" dataKey="gordura" stroke="#f59e0b" strokeWidth={3} name="Gordura (%)" />
                      <Line yAxisId="left" type="monotone" dataKey="musculo" stroke="#10b981" strokeWidth={3} name="Músculo (kg)" />
                    </LineChart>
                  </ResponsiveContainer>
                </div>
              </div>

              <div className="mb-8">
                <h3 className="text-lg font-bold text-gray-800 mb-4 flex items-center gap-2">
                  <FileBarChart className="w-5 h-5" /> Histórico de Exames Laboratoriais
                </h3>
                {/* ✅ CORREÇÃO CRÍTICA: Verificação antes do .map() */}
                {Array.isArray(labExamsHistory) && labExamsHistory.length > 0 ? (
                  <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                    {labExamsHistory.map((exame, index) => (
                      <div key={index} className="bg-red-50 border border-red-200 rounded-xl p-4">
                        <div className="flex items-center gap-2 mb-2">
                          <FileText className="w-4 h-4 text-red-600" />
                          <span className="font-semibold text-red-800">{exame.exame}</span>
                        </div>
                        <div className="text-sm text-gray-700 mb-2">
                          <Calendar className="w-3 h-3 inline mr-1" /> {exame.data}
                        </div>
                        <div className="text-xs text-gray-600 space-y-1">
                          {Object.entries(exame.indicadores).map(([key, value]) => (
                            <div key={key}><strong>{key}:</strong> {value}</div>
                          ))}
                        </div>
                        <div className="text-xs text-blue-600 mt-2 italic">{exame.observacoes}</div>
                      </div>
                    ))}
                  </div>
                ) : (
                  <div className="bg-gray-50 border border-gray-200 rounded-xl p-8 text-center">
                    <FileText className="w-12 h-12 text-gray-400 mx-auto mb-3" />
                    <p className="text-gray-500 font-medium">Nenhum exame laboratorial cadastrado</p>
                    <p className="text-sm text-gray-400 mt-1">Os exames aparecerão aqui quando forem adicionados</p>
                  </div>
                )}
              </div>

              <div className="mb-8">
                <h3 className="text-lg font-bold text-gray-800 mb-4 flex items-center gap-2">
                  <Utensils className="w-5 h-5" /> Histórico de Dietas e Macros
                </h3>
                <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
                  <div className="bg-green-50 rounded-xl p-6">
                    <h4 className="font-semibold text-green-800 mb-3">Evolução de Planos Nutricionais</h4>
                    {/* ✅ CORREÇÃO: Verificação antes do .map() */}
                    {Array.isArray(dietHistory) && dietHistory.length > 0 ? (
                      <div className="space-y-3">
                        {dietHistory.map((dieta) => (
                          <div key={dieta.id} className="bg-white p-3 rounded-lg border-l-4 border-green-500">
                            <div className="flex justify-between items-start">
                              <div>
                                <div className="font-bold text-sm">{dieta.nome}</div>
                                <div className="text-xs text-gray-600">Início: {dieta.dataInicio} • {dieta.metodo}</div>
                                <div className="text-xs text-gray-500 mt-1">Duração: {dieta.duracao}</div>
                              </div>
                              <div className="text-right text-xs">
                                <div>Cal: {dieta.macros.calorias}kcal</div>
                                <div>Prot: {dieta.macros.proteinas}g</div>
                                <div>Carbs: {dieta.macros.carboidratos}g</div>
                                <div>Gord: {dieta.macros.gorduras}g</div>
                              </div>
                            </div>
                            <div className="text-xs text-blue-600 mt-1">{dieta.observacoes}</div>
                          </div>
                        ))}
                      </div>
                    ) : (
                      <div className="text-center text-gray-500 py-8">
                        <Utensils className="w-10 h-10 text-gray-400 mx-auto mb-2" />
                        <p className="text-sm">Nenhuma dieta cadastrada</p>
                      </div>
                    )}
                  </div>

                  <div className="bg-green-50 rounded-xl p-6">
                    <h4 className="font-semibold text-green-800 mb-3">Evolução de Macros ao Longo do Tempo</h4>
                    {/* ✅ CORREÇÃO: Verificação antes de usar no gráfico */}
                    {Array.isArray(macrosEvolution) && macrosEvolution.length > 0 ? (
                      <ResponsiveContainer width="100%" height={250}>
                        <AreaChart data={macrosEvolution}>
                          <CartesianGrid strokeDasharray="3 3" stroke="#e5e7eb" />
                          <XAxis dataKey="mes" tick={{ fill: '#6b7280', fontSize: 11 }} />
                          <YAxis tick={{ fill: '#6b7280', fontSize: 11 }} />
                          <Tooltip />
                          <Legend />
                          <Area type="monotone" dataKey="calorias" stackId="1" stroke="#10b981" fill="#10b981" name="Calorias" />
                          <Area type="monotone" dataKey="carbs" stackId="2" stroke="#3b82f6" fill="#3b82f6" name="Carboidratos" />
                          <Area type="monotone" dataKey="prot" stackId="3" stroke="#f59e0b" fill="#f59e0b" name="Proteínas" />
                        </AreaChart>
                      </ResponsiveContainer>
                    ) : (
                      <div className="h-[250px] flex items-center justify-center text-gray-500">
                        <div className="text-center">
                          <BarChart3 className="w-10 h-10 text-gray-400 mx-auto mb-2" />
                          <p className="text-sm">Dados insuficientes para gráfico</p>
                        </div>
                      </div>
                    )}
                  </div>
                </div>
              </div>
            </div>
          </>
        )}

        {activeView === 'timeline' && (
          <>
            {/* ✅ CORREÇÃO: Verificação antes do .map() */}
            {Array.isArray(consultations) && consultations.length > 0 ? (
              <div className="relative">
                <div className="absolute left-8 top-0 bottom-0 w-1 bg-gradient-to-b from-blue-600 via-purple-600 to-pink-600 rounded-full" />
                <div className="space-y-6 relative">
                  {consultations.map((consultation) => (
                    <div key={consultation.id} className="ml-16">
                      <ConsultationCard consultation={consultation} />
                    </div>
                  ))}
                </div>
              </div>
            ) : (
              <div className="bg-white rounded-xl shadow-lg p-12 text-center">
                <Calendar className="w-16 h-16 text-gray-400 mx-auto mb-4" />
                <h3 className="text-xl font-bold text-gray-700 mb-2">Nenhuma consulta cadastrada</h3>
                <p className="text-gray-500">As consultas aparecerão aqui conforme forem sendo realizadas</p>
              </div>
            )}
            {compareMode && selectedCompare.length === 2 && (
              <div className="fixed bottom-8 right-8 bg-blue-600 text-white px-6 py-3 rounded-full shadow-2xl font-bold cursor-pointer hover:bg-blue-700 transition-colors animate-bounce">
                Comparar Consultas Selecionadas →
              </div>
            )}
          </>
        )}
      </div>
    </div>
  );
};

window.addEventListener('DOMContentLoaded', () => {
  const container = document.getElementById('root');
  if (container) {
    // Read data from Django's json_script tags with fallbacks
    const pageData = {
      patient: JSON.parse(document.getElementById('patient_data')?.textContent || '{}'),
      metrics: JSON.parse(document.getElementById('metrics_data')?.textContent || '{}'),
      radar: JSON.parse(document.getElementById('radar_data')?.textContent || '[]'),
      evolution: JSON.parse(document.getElementById('evolution_data')?.textContent || '[]'),
      labExams: JSON.parse(document.getElementById('lab_exams_data')?.textContent || '[]'),
      dietHistory: JSON.parse(document.getElementById('diet_history_data')?.textContent || '[]'),
      macrosEvolution: JSON.parse(document.getElementById('macros_evolution_data')?.textContent || '[]'),
      consultations: JSON.parse(document.getElementById('consultations_data')?.textContent || '[]'),
    };

    const root = ReactDOM.createRoot(container);
    root.render(<NutritionCommandCenter {...pageData} />);
  }
});