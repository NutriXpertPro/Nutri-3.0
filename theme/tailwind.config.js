const defaultTheme = require('tailwindcss/defaultTheme')

/** @type {import('tailwindcss').Config} */
module.exports = {
  important: '#react-root',
  content: [
    './templates/*.html',           // **FIX:** Adicionado para garantir a leitura de arquivos na raiz de /templates
    './templates/**/*.html',        // Para arquivos em subdiretórios de /templates
    './**/templates/**/*.html',     // Para templates dentro de cada app do Django
    './**/*.py',
    './**/*.js',
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Inter var', ...defaultTheme.fontFamily.sans],
      },
    },
  },
  safelist: [
    // Cores dinâmicas usadas no componente React
    { pattern: /text-(blue|purple|yellow|green)-400/ },
    { pattern: /(bg|text|border)-slate-(50|100|200|300|400|500|600|700|800|900)/ },
    { pattern: /(bg|text|border)-(red|green|blue|purple|yellow)-(100|200|300|400|500|600)/ },

    // Utilitários comuns presentes na página
    'min-h-screen', 'mx-auto', 'p-6', 'mb-6', 'px-3', 'px-4', 'py-1', 'py-2', 'py-4',
    'grid', 'grid-cols-3', 'gap-2', 'gap-3', 'gap-4', 'flex', 'items-center', 'justify-center',
    'bg-slate-950', 'bg-slate-900', 'bg-slate-800/50', 'text-slate-100', 'text-slate-300', 'text-slate-400',
    'border', 'border-l-4', 'border-t', 'border-r', 'border-b', 'border-slate-700', 'border-slate-800', 'border-dashed',
    'rounded', 'rounded-lg', 'rounded-2xl', 'rounded-full', 'shadow-2xl',
    'sticky', 'top-0', 'z-10', 'z-20', 'z-40', 'z-50',
    'overflow-x-auto', 'transition', 'capitalize', 'group', 'group-hover:opacity-100', 'opacity-0',
    'w-3', 'w-4', 'w-5', 'w-8', 'w-full', 'h-3', 'h-4', 'h-5', 'h-8',
    'text-xs', 'text-sm', 'text-lg', 'text-xl', 'text-2xl', 'font-bold', 'font-semibold',
    'hover:bg-slate-800', 'hover:bg-slate-700', 'hover:bg-red-500/20', 'hover:text-blue-500',
    'focus:border-blue-500', 'outline-none'
  ],
  plugins: [],
}
