/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
      '../templates/**/*.html',
      '../*/templates/**/*.html',
      '../*/*.py',
      '../*/*/*.py'
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
