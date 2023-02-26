/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['../templates/**/*.{html, js}'],
  theme: {
    extend: {},
    fontFamily: {
      'poppins': ['Poppins', 'sans-serif'],
      'pacifico': ['Pacifico', 'cursive'],
      'lalezar': ['Lalezar', 'cursive'],
      'marhey': ['Marhey', 'cursive'],
      'tajawal': ['Tajawal', 'sans-serif'],
      'elmessiri': ['El Messiri', 'sans-serif'],      
    },
    screens: {
      'sm': '640px',
      'md': '768px',
      'lg': '1024px',
      'xl': '1280px',
      '2xl': '1536px',
    },
  },
  plugins: [],
}
