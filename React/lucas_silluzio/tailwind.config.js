/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        transparent: 'transparent',
        current: 'currentColor',
        'white': '#ffffff',
        'purple': '#3f3cbb',
        'midnight': '#121063',
        'metal': '#565584',
        'tahiti': '#3ab7bf',
        'silver': '#ecebff',
        'bubble-gum': '#ff77e9',
        'black': '#000000',
      },
      backgroundImage: {
        'gif': "url('/src/images/2.gif')",
      },
      screens: {
        'sm': '500px',
        'md': [
          {'min': '668px', 'max': '767px'},
          {'min': '868px'}
        ],
        'lg': '1100px',
        'xl': '1400px',
      },
    },
  },
  plugins: [],
}
