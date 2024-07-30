module.exports = {
    content: [
        './templates/**/*.html',  // Current templates directory
        
        // Paths to Django template files
        '../templates/**/*.html',
        '../../templates/**/*.html',
        '../../**/templates/**/*.html',

        // Uncomment if you use Tailwind CSS in JavaScript files
        // '!../../**/node_modules',
        // '../../**/*.js',

        // Uncomment if you use Tailwind CSS classes in Python files
        // '../../**/*.py'
    ],
    theme: {
        extend: {
            colors: {
                transparent: 'transparent',
                current: 'currentColor',
                black: '#0f172a',
                white: '#ffffff',
                purple: '#3f3cbb',
                midnight: '#121063',
                metal: '#565584',
                tahiti: '#3ab7bf',
                silver: '#ecebff',
                'bubble-gum': '#ff77e9',
                bermuda: '#78dcca',
            },
        },
    },
    plugins: [
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/line-clamp'),
        require('@tailwindcss/aspect-ratio'),
        require("daisyui"),
    ],
    daisyui: {
        themes: ["light", "dark", "cupcake"],
    },
};
