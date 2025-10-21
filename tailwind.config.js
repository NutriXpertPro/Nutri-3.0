/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
      './**/*.html',
      './**/templates/**/*.html',
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        'brand-background': '#0A0E28',
        'card-primary': '#0E1832',
        'card-secondary': '#0D262B',
        'card-tertiary': '#321C14',
        'accent-blue': '#3B82F6',
        'accent-green': '#10B981',
        'accent-orange': '#F97316',
        'accent-purple': '#A855F7',
      }
    },
  },
  plugins: [],
}
