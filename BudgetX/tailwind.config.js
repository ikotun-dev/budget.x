/** @type {import('tailwindcss').Config} */

module.exports = {
  content: [
    './templates/**/*.html'
  ],
  theme: {
    extend: {
      fontFamily :{
        'pop' : ['Poppins', 'sans-serif'],
        'philosopher' : ['Philosopher', 'sans-serif'],
        montserrat: ['Montserrat', 'sans-serif'],
      },

      spacing: {
        '17' : '4.43rem',
        '25' : '8.22rem',
        '98' : '23.3rem',
        '99' : '26rem',
        '100' : '30rem',
        '47' : '11rem',
        '54' : '13.5rem'

      }
    },
  },
  plugins: [],
}

