module.exports = {
  mode: 'jit',
  purge: ['./src/app.html', './src/**/*.{svelte,js,ts}'],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {},
  },
  variants: {
    extend: {},
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/aspect-ratio')
  ],
}
