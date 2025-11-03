const defaultTheme = require('tailwindcss/defaultTheme')

/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './templates/appointments/**/*.html',
    './templates/anamnesis/**/*.html',
    './templates/diets/**/*.html',
    './templates/evaluations/**/*.html',
    './templates/messages/**/*.html',
    './templates/notifications/**/*.html',
    './templates/patients/**/*.html',
    './templates/payments/**/*.html',
    './templates/users/**/*.html',
    './theme/templates/**/*.html',
    './**/*.py',
    './**/*.js',
    './theme/static/src/input.css',  // Self-scan para forçar geração de @apply classes
  ],
  theme: {
  },
  plugins: [],
}
