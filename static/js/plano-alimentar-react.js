// Plano Alimentar React (UMD) - Versão 2 completa com abas, TACO e análises
// Carrega via React/ReactDOM UMD e ícones SVG inline (sem ESM)
(function(){
  const React = window.React;
  const { createRoot } = window.ReactDOM;
  const h = React.createElement;

  // Marcador de montagem incremental
  // Icons helper
function makeIcon(paths,{w=20,h=20}={}){return (p={})=>h('svg',{width:p.w||w,height:p.h||h,viewBox:'0 0 24 24',fill:'none',stroke:'currentColor',strokeWidth:2,strokeLinecap:'round',strokeLinejoin:'round',...p},paths.map((q,i)=>h(q.tag||'path',{key:i,...q})));}
const Plus=makeIcon([{d:'M12 5v14M5 12h14'}]);
const Search=(p={})=>h('svg',{width:p.w||16,height:p.h||16,viewBox:'0 0 24 24',fill:'none',stroke:'currentColor',strokeWidth:2,strokeLinecap:'round',strokeLinejoin:'round',...p},[h('circle',{cx:11,cy:11,r:8}),h('line',{x1:21,y1:21,x2:16.65,y2:16.65})]);
const Trash2=(p={})=>h('svg',{width:p.w||16,height:p.h||16,viewBox:'0 0 24 24',fill:'none',stroke:'currentColor',strokeWidth:2,strokeLinecap:'round',strokeLinejoin:'round',...p},[h('polyline',{points:'3 6 5 6 21 6'}),h('path',{d:'M19 6l-1 14a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2L5 6'}),h('path',{d:'M10 11v6'}),h('path',{d:'M14 11v6'}),h('path',{d:'M9 6V4a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v2'})]);
const Save=makeIcon([{d:'M19 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11l5 5v11a2 2 0 0 1-2 2z'}]);
const FileText=(p={})=>h('svg',{width:p.w||20,height:p.h||20,viewBox:'0 0 24 24',fill:'none',stroke:'currentColor',strokeWidth:2,strokeLinecap:'round',strokeLinejoin:'round',...p},[h('path',{d:'M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z'}),h('polyline',{points:'14 2 14 8 20 8'}),h('line',{x1:16,y1:13,x2:8,y2:13}),h('line',{x1:16,y1:17,x2:8,y2:17})]);
const Smartphone=makeIcon([{d:'M13 2H7a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V4a2 2 0 0 0-2-2z'}]);
const Calculator=makeIcon([{d:'M7 3h10a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2z'},{d:'M16 7H8'},{d:'M16 11H8'},{d:'M10 15h.01'},{d:'M13 15h.01'},{d:'M16 15h.01'}]);
const BarChart3=(p={})=>h('svg',{width:p.w||20,height:p.h||20,viewBox:'0 0 24 24',fill:'none',stroke:'currentColor',strokeWidth:2,strokeLinecap:'round',strokeLinejoin:'round',...p},[h('line',{x1:3,y1:3,x2:3,y2:21}),h('line',{x1:3,y1:21,x2:21,y2:21}),h('rect',{x:7,y:12,width:3,height:5}),h('rect',{x:12,y:8,width:3,height:9}),h('rect',{x:17,y:5,width:3,height:12})]);
const PieChart=(p={})=>h('svg',{width:p.w||20,height:p.h||20,viewBox:'0 0 24 24',fill:'none',stroke:'currentColor',strokeWidth:2,strokeLinecap:'round',strokeLinejoin:'round',...p},[h('path',{d:'M21.21 15.89A10 10 0 1 1 8 2.83'}),h('path',{d:'M22 12A10 10 0 0 0 12 2v10z'})]);
const Edit2=(p={})=>h('svg',{width:p.w||16,height:p.h||16,viewBox:'0 0 24 24',fill:'none',stroke:'currentColor',strokeWidth:2,strokeLinecap:'round',strokeLinejoin:'round',...p},[h('path',{d:'M17 3a2.828 2.828 0 1 1 4 4L7 21H3v-4L17 3z'})]);
const Copy=(p={})=>h('svg',{width:p.w||16,height:p.h||16,viewBox:'0 0 24 24',fill:'none',stroke:'currentColor',strokeWidth:2,strokeLinecap:'round',strokeLinejoin:'round',...p},[h('rect',{x:9,y:9,width:13,height:13,rx:2,ry:2}),h('path',{d:'M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1'})]);
const Settings=(p={})=>h('svg',{width:p.w||16,height:p.h||16,viewBox:'0 0 24 24',fill:'none',stroke:'currentColor',strokeWidth:2,strokeLinecap:'round',strokeLinejoin:'round',...p},[h('circle',{cx:12,cy:12,r:3}),h('path',{d:'M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 1 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 1 1-4 0v-.09a1.65 1.65 0 0 0-1-1.51 1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 1 1-2.83-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 1 1 0-4h.09a1.65 1.65 0 0 0 1.51-1 1.65 1.65 0 0 0-.33-1.82l-.06-.06A2 2 0 1 1 7.1 3.7l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V2a2 2 0 1 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 1 1 2.83 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 1 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z'})]);
const AlertCircle=(p={})=>h('svg',{width:p.w||16,height:p.h||16,viewBox:'0 0 24 24',fill:'none',stroke:'currentColor',strokeWidth:2,strokeLinecap:'round',strokeLinejoin:'round',...p},[h('circle',{cx:12,cy:12,r:10}),h('line',{x1:12,y1:8,x2:12,y2:12}),h('line',{x1:12,y1:16,x2:12,y2:16})]);
const CheckCircle=(p={})=>h('svg',{width:p.w||16,height:p.h||16,viewBox:'0 0 24 24',fill:'none',stroke:'currentColor',strokeWidth:2,strokeLinecap:'round',strokeLinejoin:'round',...p},[h('path',{d:'M22 11.08V12a10 10 0 1 1-5.93-9.14'}),h('polyline',{points:'22 4 12 14.01 9 11.01'})]);
const XCircle=(p={})=>h('svg',{width:p.w||16,height:p.h||16,viewBox:'0 0 24 24',fill:'none',stroke:'currentColor',strokeWidth:2,strokeLinecap:'round',strokeLinejoin:'round',...p},[h('circle',{cx:12,cy:12,r:10}),h('line',{x1:15,y1:9,x2:9,y2:15}),h('line',{x1:9,y1:9,x2:15,y2:15})]);
const Star=makeIcon([{tag:'polygon',points:'12 2 15 8.5 22 9 17 13.5 18.5 20 12 16.5 5.5 20 7 13.5 2 9 9 8.5'}],{w:16,h:16});
const Calendar=makeIcon([{d:'M8 7V3M16 7V3M3 11h18M5 5h14a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2z'}]);
const ClipboardList=(p={})=>h('svg',{width:p.w||16,height:p.h||16,viewBox:'0 0 24 24',fill:'none',stroke:'currentColor',strokeWidth:2,strokeLinecap:'round',strokeLinejoin:'round',...p},[h('rect',{x:9,y:2,width:6,height:4,rx:1}),h('path',{d:'M9 14h.01M9 10h.01M13 14h4M13 10h4'}),h('path',{d:'M5 8h14v12a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2z'})]);
const TrendingUp=makeIcon([{d:'M3 17l6-6 4 4 8-8'},{d:'M14 7h7v7'}]);
const History=makeIcon([{d:'M3 12a9 9 0 1 0 3-7'},{d:'M3 3v6h6'},{d:'M12 7v5l4 2'}]);
const ChevronDown=makeIcon([{d:'M6 9l6 6 6-6'}],{w:16,h:16});
const ChevronRight=makeIcon([{d:'M9 18l6-6-6-6'}],{w:16,h:16});
const DollarSign=makeIcon([{d:'M12 1v22'},{d:'M17 5H9.5a3.5 3.5 0 0 0 0 7H14a3.5 3.5 0 0 1 0 7H6'}]);
const ShoppingCart=makeIcon([{d:'M6 6h15l-1.5 9h-12z'},{d:'M6 6l-2-3'},{d:'M9 22a1 1 0 1 0 0-2 1 1 0 0 0 0 2z'},{d:'M18 22a1 1 0 1 0 0-2 1 1 0 0 0 0 2z'}]);

// DonutChart
function DonutChart({proteinas, carboidratos, gorduras}){const total=Math.max(proteinas+carboidratos+gorduras,1);const r=60;const C=2*Math.PI*r;const p=(proteinas/total)*C,c=(carboidratos/total)*C,g=C-p-c;return h('div',{className:'flex items-center gap-2'},h('svg',{width:80,height:80,viewBox:'0 0 200 200',className:'transform -rotate-90'},h('circle',{cx:100,cy:100,r,fill:'none',stroke:'#1e293b',strokeWidth:25}),h('circle',{cx:100,cy:100,r,fill:'none',stroke:'#3b82f6',strokeWidth:25,strokeDasharray:`${p} ${C}`,strokeDashoffset:0}),h('circle',{cx:100,cy:100,r,fill:'none',stroke:'#a855f7',strokeWidth:25,strokeDasharray:`${c} ${C}`,strokeDashoffset:-p}),h('circle',{cx:100,cy:100,r,fill:'none',stroke:'#eab308',strokeWidth:25,strokeDasharray:`${g} ${C}`,strokeDashoffset:-(p+c)})),h('div',{className:'text-xs space-y-0.5'},h('div',{className:'flex items-center gap-1'},h('div',{className:'w-2 h-2 bg-blue-500 rounded'}),h('span',null,`P:${Math.round(proteinas)}g`)),h('div',{className:'flex items-center gap-1'},h('div',{className:'w-2 h-2 bg-purple-500 rounded'}),h('span',null,`C:${Math.round(carboidratos)}g`)),h('div',{className:'flex items-center gap-1'},h('div',{className:'w-2 h-2 bg-yellow-500 rounded'}),h('span',null,`G:${Math.round(gorduras)}g`))));}

// Dados TACO (resumo suficiente)
const alimentosTACO=[
 {id:1,nome:'Frango, peito, grelhado',categoria:'Carnes',calorias:165,proteinas:31,carboidratos:0,gorduras:3.6,fibras:0,porcao:100,unidade:'g',favorito:false},
 {id:3,nome:'Arroz integral, cozido',categoria:'Cereais',calorias:123,proteinas:2.6,carboidratos:25.8,gorduras:1,fibras:2.7,porcao:100,unidade:'g',favorito:false},
 {id:6,nome:'Aveia, flocos',categoria:'Cereais',calorias:394,proteinas:13.9,carboidratos:66.6,gorduras:8.5,fibras:9.1,porcao:30,unidade:'g',favorito:false},
 {id:7,nome:'Banana, prata',categoria:'Frutas',calorias:98,proteinas:1.3,carboidratos:26,gorduras:0.1,fibras:2,porcao:1,unidade:'und',favorito:false},
 {id:9,nome:'Ovo, galinha, cozido',categoria:'Ovos',calorias:155,proteinas:13,carboidratos:1.1,gorduras:10.6,fibras:0,porcao:50,unidade:'g',favorito:false},
 {id:12,nome:'Iogurte, grego, natural',categoria:'Laticínios',calorias:59,proteinas:10,carboidratos:3.6,gorduras:0.4,fibras:0,porcao:100,unidade:'g',favorito:false},
 {id:13,nome:'Brócolis, cozido',categoria:'Verduras',calorias:25,proteinas:2.4,carboidratos:4,gorduras:0.4,fibras:3.4,porcao:100,unidade:'g',favorito:false},
 {id:14,nome:'Batata-doce, cozida',categoria:'Tubérculos',calorias:77,proteinas:0.6,carboidratos:18.4,gorduras:0.1,fibras:2.2,porcao:100,unidade:'g',favorito:false},
 {id:18,nome:'Pão, trigo, integral',categoria:'Cereais',calorias:253,proteinas:8,carboidratos:49,gorduras:3,fibras:6.9,porcao:50,unidade:'g',favorito:false},
 {id:23,nome:'Salmão, grelhado',categoria:'Peixes',calorias:211,proteinas:23,carboidratos:0,gorduras:13,fibras:0,porcao:100,unidade:'g',favorito:false},
 {id:26,nome:'Amêndoas',categoria:'Oleaginosas',calorias:579,proteinas:21,carboidratos:20,gorduras:50,fibras:11,porcao:30,unidade:'g',favorito:false},
];

function App(){
  const {useState,useEffect,useCallback}=React;
  const metodos={balanced:{nome:'Balanced',proteinas:30,carboidratos:45,gorduras:25},lowcarb:{nome:'Low Carb',proteinas:35,carboidratos:25,gorduras:40},highprotein:{nome:'High Protein',proteinas:40,carboidratos:40,gorduras:20},ketogenic:{nome:'Ketogenic',proteinas:25,carboidratos:10,gorduras:65},custom:{nome:'Custom',proteinas:30,carboidratos:45,gorduras:25}};
  const formulas=[{id:'mifflin',nome:'Mifflin-St Jeor'},{id:'harris',nome:'Harris-Benedict'},{id:'cunningham',nome:'Cunningham'},{id:'who',nome:'OMS/FAO'}];
  const [paciente,setPaciente]=useState({nome:'Maria Silva',peso:65,altura:165,idade:27,sexo:'F',atividade:'moderado',objetivo:'emagrecimento',restricoes:['Lactose'],objetivoDetalhado:'Perder 5kg em 3 meses mantendo massa muscular',orientacoesGerais:['Beber 2L de água por dia','Evitar frituras']});
  const [aba,setAba]=useState('dieta');
  const [dia,setDia]=useState(0);
  const [metodo,setMetodo]=useState('balanced');
  const [formula,setFormula]=useState('mifflin');
  const [macrosCustom,setMacrosCustom]=useState({proteinas:30,carboidratos:45,gorduras:25});
  const [res,setRes]=useState(null);
  const [refs,setRefs]=useState([]);
  const [current,setCurrent]=useState(null);
  const [q,setQ]=useState('');
  const [alims,setAlims]=useState(alimentosTACO);
  const favs=alims.filter(a=>a.favorito);

  const calc=useCallback(()=>{const {peso,altura,idade,sexo,atividade,objetivo}=paciente;const pct=metodo==='custom'?macrosCustom:metodos[metodo];let tmb=0; if(formula==='harris') tmb=sexo==='M'?88.362+(13.397*peso)+(4.799*altura)-(5.677*idade):447.593+(9.247*peso)+(3.098*altura)-(4.330*idade); else if(formula==='cunningham'){const mm=peso*0.75;tmb=500+(22*mm);} else if(formula==='who') tmb=sexo==='M'?(11.6*peso)+879:(8.7*peso)+829; else tmb=sexo==='M'?(10*peso)+(6.25*altura)-(5*idade)+5:(10*peso)+(6.25*altura)-(5*idade)-161; const fatores={sedentario:1.2,leve:1.375,moderado:1.55,intenso:1.725,muito_intenso:1.9}; const gcdt=tmb*(fatores[atividade]||1.55); const ajustes={emagrecimento:0.85,manutencao:1,ganho_massa:1.15}; const meta=gcdt*(ajustes[objetivo]||1); const macros={proteinas:{g:Math.round((meta*pct.proteinas/100)/4),gkg:Math.round((((meta*pct.proteinas/100)/4)/peso)*10)/10},carboidratos:{g:Math.round((meta*pct.carboidratos/100)/4),gkg:Math.round((((meta*pct.carboidratos/100)/4)/peso)*10)/10},gorduras:{g:Math.round((meta*pct.gorduras/100)/9),gkg:Math.round((((meta*pct.gorduras/100)/9)/peso)*10)/10}}; setRes({tmb:Math.round(tmb),gcdt:Math.round(gcdt),meta:Math.round(meta),macros});},[paciente,metodo,formula,macrosCustom]);
  useEffect(()=>{calc()},[]); useEffect(()=>{if(res) calc()},[metodo,formula]);

  const totals=(()=>{if(!res) return null; const t={calorias:0,proteinas:0,carboidratos:0,gorduras:0,fibras:0}; refs.forEach(r=>r.itens?.forEach(i=>{t.calorias+=i.caloriasCalc;t.proteinas+=i.proteinasCalc;t.carboidratos+=i.carboidratosCalc;t.gorduras+=i.gordurasCalc;t.fibras+=i.fibrasCalc||0;})); return t;})();
  const diffMacro=(m)=>{if(!totals||!res) return {valor:0,cor:'cinza',icon:h(AlertCircle,{className:'w-3 h-3 text-slate-400'})}; const meta=res.macros[m].g; const real=totals[m]; const d=real-meta; if(Math.abs(d)<1) return {valor:0,cor:'verde',icon:h(CheckCircle,{className:'w-3 h-3 text-green-500'})}; if(d>0) return {valor:d,cor:'vermelho',icon:h(XCircle,{className:'w-3 h-3 text-red-500'})}; return {valor:d,cor:'cinza',icon:h(AlertCircle,{className:'w-3 h-3 text-slate-400'})};};

  const addRef=()=>{const base=refs.length?refs[refs.length-1].horario:'08:00'; const [h2,m2]=base.split(':').map(Number); const nh=`${String((h2+3)%24).padStart(2,'0')}:${String(m2).padStart(2,'0')}`; setRefs([...refs,{id:`ref-${Date.now()}`,nome:`Refeição ${refs.length+1}`,horario:nh,itens:[],tipo:'lanche',orientacoes:'',mostrarOrientacoes:false}]);};
  const addFood=(a,refId)=>{setRefs(prev=>prev.map(r=>{if(r.id!==refId) return r; const it={...a,quantidade:a.porcao,caloriasCalc:a.calorias,proteinasCalc:a.proteinas,carboidratosCalc:a.carboidratos,gordurasCalc:a.gorduras,fibrasCalc:a.fibras||0}; return {...r,itens:[...(r.itens||[]),it]};})); setQ('');};
  const rmFood=(refId,idx)=>setRefs(prev=>prev.map(r=> r.id===refId?{...r,itens:r.itens.filter((_,i)=>i!==idx)}:r));
  const updQty=(refId,idx,qtd)=>setRefs(prev=>prev.map(r=>{if(r.id!==refId) return r; const it=r.itens[idx]; const f=qtd/it.porcao; const novo={...it,quantidade:qtd,caloriasCalc:Math.round(it.calorias*f),proteinasCalc:Math.round(it.proteinas*f*10)/10,carboidratosCalc:Math.round(it.carboidratos*f*10)/10,gordurasCalc:Math.round(it.gorduras*f*10)/10,fibrasCalc:Math.round((it.fibras||0)*f*10)/10}; const itens=[...r.itens]; itens[idx]=novo; return {...r,itens};}));
  const toggleFav=(id)=>setAlims(prev=>prev.map(a=>a.id===id?{...a,favorito:!a.favorito}:a));
  const results=q.length>1? alims.filter(a=>a.nome.toLowerCase().includes(q.toLowerCase())).sort((a,b)=>(b.favorito?1:0)-(a.favorito?1:0)) : [];

  // Render helper (pedaço 1) - continua abaixo
  // Render (pedaço 2)
  const header = () => h('div',{className:'max-w-7xl mx-auto mb-4'},
    h('div',{className:'bg-slate-900 border border-slate-800 rounded-xl p-4'},
      h('div',{className:'flex items-center justify-between mb-3'},
        h('div',{className:'flex items-center gap-4'},
          h('div',{className:'flex items-center gap-2'},
            h('div',{className:'w-10 h-10 bg-gradient-to-br from-blue-500 to-purple-600 rounded-full flex items-center justify-center font-bold text-lg'}, paciente.nome.split(' ').map(n=>n[0]).join('')),
            h('div',null,
              h('h2',{className:'font-bold text-sm'},paciente.nome),
              h('p',{className:'text-xs text-slate-400'},`${paciente.idade}a, ${paciente.sexo==='M'?'M':'F'} | ${paciente.peso}kg, ${paciente.altura}cm | ${paciente.atividade}`)
            )
          ),
          res && h('div',{className:'flex items-center gap-2 text-xs px-3 py-1 bg-slate-800/50 rounded-lg'},
            h('span',{className:'text-slate-400'},'TMB:'), h('span',{className:'font-bold'},res.tmb),
            h('span',{className:'text-slate-600'},'|'), h('span',{className:'text-slate-400'},'GCDT:'), h('span',{className:'font-bold'},res.gcdt),
            h('span',{className:'text-slate-600'},'|'), h('span',{className:'text-slate-400'},'META:'), h('span',{className:'font-bold text-green-400'},`${res.meta} kcal`)
          )
        ),
        h('div',{className:'flex items-center gap-2'},
          h('select',{value:metodo,onChange:e=>setMetodo(e.target.value),className:'bg-slate-800 border border-slate-700 rounded-lg px-2 py-1 text-xs focus:border-blue-500 outline-none'}, Object.entries(metodos).map(([k,m])=>h('option',{key:k,value:k},m.nome))),
          h('select',{value:formula,onChange:e=>setFormula(e.target.value),className:'bg-slate-800 border border-slate-700 rounded-lg px-2 py-1 text-xs focus:border-blue-500 outline-none'}, [
            h('option',{key:'mifflin',value:'mifflin'},'Mifflin-St Jeor'),
            h('option',{key:'harris',value:'harris'},'Harris-Benedict'),
            h('option',{key:'cunningham',value:'cunningham'},'Cunningham'),
            h('option',{key:'who',value:'who'},'OMS/FAO'),
          ]),
          h('button',{onClick:calc,className:'px-3 py-1 bg-blue-600 hover:bg-blue-500 rounded-lg transition text-xs flex items-center gap-1'}, h(Calculator,{className:'w-3 h-3'}),' Recalcular')
        )
      ),
      res && h('div',{className:'flex items-center justify-between'},
        h('div',{className:'flex items-center gap-6'}, ['proteinas','carboidratos','gorduras'].map(m=>{const d=diffMacro(m);return h('div',{key:m,className:'flex items-center gap-2'},
          h('div',{className:`font-bold ${m==='proteinas'?'text-blue-400':m==='carboidratos'?'text-purple-400':'text-yellow-400'}`}, `${m==='proteinas'?'P':m==='carboidratos'?'C':'G'}: ${res.macros[m].g}g`),
          h('div',{className:'text-xs text-slate-400'},`(${res.macros[m].gkg}g/kg)`),
          h('div',{className:`text-xs font-bold flex items-center gap-0.5 ${d.cor==='verde'?'text-green-400':d.cor==='vermelho'?'text-red-400':'text-slate-400'}`}, d.icon, (d.valor>0?('+'+Math.round(d.valor)):Math.round(d.valor))+'g')
        );})),
        h('div',{className:'flex items-center gap-4'}, totals && h(DonutChart,{proteinas:totals.proteinas,carboidratos:totals.carboidratos,gorduras:totals.gorduras}), totals&&res&& h('div',{className:'text-sm font-bold'}, h('span',{className:totals.calorias>res.meta?'text-red-400':'text-green-400'}, Math.round(totals.calorias)), h('span',{className:'text-slate-400'},` / ${res.meta} kcal`))),
        h('div',{className:'flex gap-2'}, h('button',{className:'px-3 py-1 bg-slate-800 hover:bg-slate-700 rounded-lg transition text-xs flex items-center gap-1'}, h(Save,{className:'w-3 h-3'}),' Salvar'), h('button',{className:'px-3 py-1 bg-blue-600 hover:bg-blue-500 rounded-lg transition text-xs flex items-center gap-1'}, h(FileText,{className:'w-3 h-3'}),' PDF'), h('button',{className:'px-3 py-1 bg-green-600 hover:bg-green-500 rounded-lg transition text-xs flex items-center gap-1'}, h(Smartphone,{className:'w-3 h-3'}),' App'))
      )
    )
  );

  const tabs = () => h('div',{className:'max-w-7xl mx-auto mb-4'}, h('div',{className:'flex gap-2 border-b border-slate-800'}, ['dieta','contexto','analise','historico'].map(tab=> h('button',{key:tab,onClick:()=>setAba(tab),className:`px-4 py-2 text-sm font-medium flex items-center gap-2 border-b-2 transition ${aba===tab?'border-blue-500 text-blue-400':'border-transparent text-slate-400 hover:text-slate-200'}`}, tab==='dieta'&&h(Calendar,{className:'w-4 h-4'}), tab==='contexto'&&h(ClipboardList,{className:'w-4 h-4'}), tab==='analise'&&h(TrendingUp,{className:'w-4 h-4'}), tab==='historico'&&h(History,{className:'w-4 h-4'}), ` ${tab.charAt(0).toUpperCase()+tab.slice(1)}`))));

  // Conteúdo Dieta (resumo funcional)
  const dietContent = () => h('div',null,
    h('div',{className:'flex items-center justify-between mb-4 bg-slate-900 border border-slate-800 rounded-xl p-3'},
      h('div',{className:'flex items-center gap-2'}, h('span',{className:'text-xs text-slate-400 mr-2'},'Dia da semana:'), ['SEG','TER','QUA','QUI','SEX','SAB','DOM'].map((d,idx)=> h('button',{key:idx,onClick:()=>setDia(idx),className:`w-10 h-10 rounded-full font-bold text-xs transition ${dia===idx?'bg-blue-600 text-white':'bg-slate-800 text-slate-400 hover:bg-slate-700'}`}, d))),
      h('div',{className:'flex items-center gap-2'}, h('span',{className:'text-xs text-slate-400'},'Templates:'), h('select',{className:'bg-slate-800 border border-slate-700 rounded-lg px-3 py-1 text-xs focus:border-blue-500 outline-none'}, h('option',{value:'t1'},'Café Padrão')), h('button',{className:'px-3 py-1 bg-slate-800 hover:bg-slate-700 rounded-lg transition text-xs flex items-center gap-1'}, h(Copy,{className:'w-3 h-3'}),' Copiar dia'))
    ),
    h('div',{className:'space-y-4'},
      refs.map((refeicao,index)=> h('div',{key:refeicao.id,className:'bg-slate-900 border border-slate-800 rounded-xl p-4 group'},
        h('div',{className:'flex justify-between items-center mb-3'},
          h('div',{className:'flex items-center gap-3'},
            h('div',{className:`w-8 h-8 rounded-full flex items-center justify-center text-white font-bold text-sm ${refeicao.tipo==='cafe'?'bg-amber-500':refeicao.tipo==='almoco'?'bg-emerald-500':refeicao.tipo==='jantar'?'bg-purple-500':'bg-slate-500'}`}, index+1),
            h('input',{type:'text',value:refeicao.nome,onChange:e=>setRefs(prev=>prev.map(r=> r.id===refeicao.id?{...r,nome:e.target.value}:r)),className:'text-lg font-bold bg-transparent border-b-2 border-transparent hover:border-blue-500 focus:border-blue-500 outline-none px-2 transition'}),
            h('input',{type:'time',value:refeicao.horario,onChange:e=>setRefs(prev=>prev.map(r=> r.id===refeicao.id?{...r,horario:e.target.value}:r)),className:'bg-slate-800 px-2 py-1 rounded-lg border border-slate-700 text-xs focus:border-blue-500 outline-none'}),
            h('button',{onClick:()=>setRefs(prev=>prev.map(r=> r.id===refeicao.id?{...r,mostrarOrientacoes:!r.mostrarOrientacoes}:r)),className:'p-1 hover:bg-slate-800 rounded transition flex items-center gap-1 text-xs text-slate-400'}, h(ChevronRight,{className:'w-3 h-3'}),' Orientações')
          ),
          h('div',{className:'flex gap-2'}, h('button',{className:'p-1.5 hover:bg-slate-800 rounded-lg transition',title:'Salvar como template'}, h(Settings,{className:'w-4 h-4 text-slate-400'})), h('button',{onClick:()=>{const copia={...refeicao,id:`ref-${Date.now()}`,nome:`${refeicao.nome} (cópia)`,itens:[...refeicao.itens]}; setRefs([...refs,copia]);},className:'p-1.5 hover:bg-slate-800 rounded-lg transition',title:'Duplicar'}, h(Copy,{className:'w-4 h-4 text-slate-400'})), h('button',{onClick:()=>setRefs(prev=>prev.filter(r=> r.id!==refeicao.id)),className:'p-1.5 hover:bg-red-500/20 rounded-lg transition',title:'Remover'}, h(Trash2,{className:'w-4 h-4 text-red-500'})))
        ),
        refeicao.mostrarOrientacoes && h('div',{className:'mb-3 p-2 bg-slate-800/50 rounded-lg'}, h('textarea',{value:refeicao.orientacoes,onChange:e=>setRefs(prev=>prev.map(r=> r.id===refeicao.id?{...r,orientacoes:e.target.value}:r)),placeholder:'Orientações...',className:'w-full bg-slate-800 border border-slate-700 rounded-lg px-3 py-2 text-xs focus:border-blue-500 outline-none resize-none',rows:2})),
        h('div',{className:'mb-3'}, h('div',{className:'text-xs text-slate-400 mb-2 flex items-center gap-2'}, h(Star,{className:'w-3 h-3 text-yellow-500'}),'Alimentos favoritos:'), h('div',{className:'flex flex-wrap gap-2'}, favs.slice(0,8).map(a=> h('button',{key:a.id,onClick:()=>addFood(a,refeicao.id),className:'px-2 py-1 bg-slate-800 hover:bg-slate-700 rounded-full text-xs transition flex items-center gap-1'}, a.nome.length>20?a.nome.substring(0,20)+'...':a.nome)))),
        h('div',{className:'overflow-x-auto mb-3'}, h('table',{className:'w-full'}, h('thead',null, h('tr',{className:'border-b border-slate-700'}, ['Alimento','Qtd','Un','P','C','G','Kcal',''].map((t,i)=> h('th',{key:i,className:'text-left py-2 text-xs text-slate-400'+(i>0?' text-center':'')}, t)))), h('tbody',null,
          (refeicao.itens||[]).map((item,idx)=> h('tr',{key:idx,className:'border-b border-slate-800 hover:bg-slate-800/30 transition'},
            h('td',{className:'py-2 text-xs'}, item.nome),
            h('td',{className:'text-center'}, h('input',{type:'number',value:item.quantidade,onChange:e=>updQty(refeicao.id,idx,Number(e.target.value)),className:'w-14 bg-slate-800 border border-slate-700 rounded px-1 py-1 text-center text-xs focus:border-blue-500 outline-none'})),
            h('td',{className:'text-center text-slate-400 text-xs'}, item.unidade||'-'),
            h('td',{className:'text-center text-blue-400 font-semibold text-xs'}, item.proteinasCalc),
            h('td',{className:'text-center text-purple-400 font-semibold text-xs'}, item.carboidratosCalc),
            h('td',{className:'text-center text-yellow-400 font-semibold text-xs'}, item.gordurasCalc),
            h('td',{className:'text-center text-green-400 font-bold text-xs'}, item.caloriasCalc),
            h('td',{className:'text-center'}, h('button',{onClick:()=>rmFood(refeicao.id,idx),className:'p-1 hover:bg-red-500/20 rounded transition'}, h(Trash2,{className:'w-3 h-3 text-red-500'})))
          )),
          h('tr',{className:'border-t-2 border-dashed border-slate-700'}, h('td',{className:'py-2 relative',colSpan:8}, h('div',{className:'flex items-center gap-2'}, h(Search,{className:'w-4 h-4 text-slate-400 absolute left-2 top-3.5'}), h('input',{type:'text',placeholder:' Buscar alimento na base TACO...', value: current===refeicao.id ? q : '', onFocus:()=>setCurrent(refeicao.id), onChange:e=>setQ(e.target.value), className:'w-full pl-8 pr-2 py-2 bg-slate-800 border border-slate-700 rounded-lg text-xs focus:border-blue-500 outline-none'})), current===refeicao.id && q.length>1 && h('div',{className:'absolute top-full mt-1 w-full bg-slate-800 border border-slate-700 rounded-lg shadow-xl z-20 max-h-64 overflow-auto'}, results.slice(0,15).map(a=> h('div',{key:a.id,className:'p-2 hover:bg-slate-700 cursor-pointer border-b border-slate-700 last:border-0 flex items-center justify-between'}, h('div',{onClick:()=>addFood(a,refeicao.id),className:'flex-1'}, h('div',{className:'font-semibold text-xs flex items-center gap-2'}, a.favorito && h(Star,{className:'w-3 h-3 text-yellow-500 fill-yellow-500'}), a.nome), h('div',{className:'text-xs text-slate-400'}, `${a.categoria}  ${a.calorias}kcal  P:${a.proteinas}g C:${a.carboidratos}g G:${a.gorduras}g`)), h('button',{onClick:()=>toggleFav(a.id),className:'p-1 hover:bg-slate-600 rounded transition'}, h(Star,{className:a.favorito?'w-4 h-4 text-yellow-500 fill-yellow-500':'w-4 h-4 text-slate-500'})))))))
        )),
      h('button',{onClick:addRef,className:'w-full py-4 border-2 border-dashed border-slate-700 hover:border-blue-500 rounded-xl transition flex items-center justify-center gap-2 text-slate-400 hover:text-blue-500 font-semibold text-sm'}, h(Plus,{className:'w-5 h-5'}),' Adicionar Nova Refeição')
    )
  );

  // Conteúdos simples das outras abas (placeholders funcionais)
  const contexto = () => h('div',{className:'grid grid-cols-2 gap-6'},
    h('div',{className:'bg-slate-900 border border-slate-800 rounded-xl p-4'}, h('h3',{className:'text-sm font-bold mb-3 flex items-center gap-2'}, h(ClipboardList,{className:'w-4 h-4 text-amber-500'}),'Restrições Alimentares'), h('div',{className:'space-y-2 mb-3'}, paciente.restricoes.map((r,idx)=> h('div',{key:idx,className:'flex items-center justify-between bg-slate-800/50 px-3 py-2 rounded-lg'}, h('span',{className:'text-sm'}, r), h('button',{onClick:()=> setPaciente({...paciente, restricoes: paciente.restricoes.filter((_,i)=>i!==idx)}) ,className:'text-red-500 hover:bg-red-500/20 p-1 rounded transition'}, h(Trash2,{className:'w-3 h-3'}))))),
      h('div',{className:'flex gap-2'}, h('input',{type:'text',placeholder:'Ex: Glúten...', onChange:e=>window.__nr=e.target.value,className:'flex-1 bg-slate-800 border border-slate-700 rounded-lg px-3 py-2 text-sm focus:border-blue-500 outline-none'}), h('button',{onClick:()=>{if(window.__nr){ setPaciente({...paciente, restricoes:[...paciente.restricoes, window.__nr]}); window.__nr='';}}, className:'px-3 py-2 bg-blue-600 hover:bg-blue-500 rounded-lg transition'}, h(Plus,{className:'w-4 h-4'})))) ,
    h('div',{className:'bg-slate-900 border border-slate-800 rounded-xl p-4'}, h('h3',{className:'text-sm font-bold mb-3 flex items-center gap-2'}, h(FileText,{className:'w-4 h-4 text-blue-500'}),'Orientações Gerais'), h('textarea',{defaultValue: paciente.orientacoesGerais.join('\n'), onBlur:e=> setPaciente({...paciente, orientacoesGerais: e.target.value.split('\n').filter(Boolean)}) ,className:'w-full bg-slate-800 border border-slate-700 rounded-lg px-3 py-2 text-sm focus:border-blue-500 outline-none resize-none',rows:6}))
  );

  const analise = () => h('div',{className:'grid grid-cols-2 gap-6'},
    h('div',{className:'bg-slate-900 border border-slate-800 rounded-xl p-4'}, h('h3',{className:'text-sm font-bold mb-4 flex items-center gap-2'}, h(TrendingUp,{className:'w-4 h-4 text-blue-500'}),'Micronutrientes'), totals? h('div',{className:'space-y-3'}, ['Fibras'].map((nome)=>{const valor=Math.round(totals.fibras); const meta=25; const pct=Math.min((valor/meta)*100,100); return h('div',{key:nome}, h('div',{className:'flex justify-between text-xs mb-1'}, h('span',{className:'text-slate-300'}, nome), h('span',{className:`font-bold ${pct>=80?'text-green-400':pct>=50?'text-yellow-400':'text-red-400'}`}, `${valor} / ${meta} g`)), h('div',{className:'w-full bg-slate-800 rounded-full h-2'}, h('div',{className:`h-2 rounded-full ${pct>=80?'bg-green-500':pct>=50?'bg-yellow-500':'bg-red-500'}`, style:{width:`${pct}%`}})), h('div',{className:'text-xs text-slate-400 mt-0.5'}, `${Math.round(pct)}% da meta`)); })) : h('div',{className:'text-center text-slate-400 text-sm py-8'},'Adicione alimentos para ver análise') ),
    h('div',{className:'bg-slate-900 border border-slate-800 rounded-xl p-4'}, h('h3',{className:'text-sm font-bold mb-4 flex items-center gap-2'}, h(BarChart3,{className:'w-4 h-4 text-purple-500'}),'Análise Semanal'), h('div',{className:'space-y-4'}, ['Aderência à Dieta','Variação Calórica','Dias Cumpridos'].map((t,i)=> h('div',{key:i,className:'bg-slate-800/50 p-3 rounded-lg'}, h('div',{className:'text-xs text-slate-400 mb-1'}, t), h('div',{className:`text-2xl font-bold ${i===0?'text-green-400':i===1?'text-blue-400':'text-purple-400'}`}, i===0?'85%': i===1?'150 kcal':'6/7')))))
  );

  const historico = () => h('div',{className:'space-y-6'}, h('div',{className:'bg-slate-900 border border-slate-800 rounded-xl p-4'}, h('h3',{className:'text-sm font-bold mb-4 flex items-center gap-2'}, h(History,{className:'w-4 h-4 text-blue-500'}),'Dietas Anteriores'), h('div',{className:'space-y-2'}, [{data:'01/11/2025',tipo:'Cutting',calorias:1800,status:'Concluída'},{data:'15/10/2025',tipo:'Manutenção',calorias:2100,status:'Concluída'}].map((d,i)=> h('div',{key:i,className:'flex items-center justify-between bg-slate-800/50 p-3 rounded-lg hover:bg-slate-800 transition cursor-pointer'}, h('div',null, h('div',{className:'font-semibold text-sm'}, d.tipo), h('div',{className:'text-xs text-slate-400'}, `${d.data}  ${d.calorias} kcal/dia`)), h('span',{className:'text-xs px-2 py-1 bg-green-900/30 text-green-400 rounded'}, d.status))))));

  // App render
  return h('div',{className:'min-h-screen bg-slate-950 text-slate-100 p-6'}, header(), tabs(), h('div',{className:'max-w-7xl mx-auto'}, aba==='dieta'? dietContent() : aba==='contexto'? contexto() : aba==='analise'? analise() : historico()));
}

// Mount
const rootEl = document.getElementById('react-root');
if (rootEl) { const root = createRoot(rootEl); root.render(h(App)); }

})();
