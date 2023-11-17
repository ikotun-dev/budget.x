/** @type {import('tailwindcss').Config} */

module.exports = {
  content: [
    './templates/**/*.html'
  ],
  theme: {
    extend: {
      spacing: {
        '17' : '4.43rem',
        '25' : '8.22rem',
        '98' : '23.3rem',
        '99' : '26rem',
        '100' : '56rem',
        '47' : '11rem',
        '54' : '13.5rem'

      }
    },
  },
  plugins: [],
}

