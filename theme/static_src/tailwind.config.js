module.exports = {
    content: [
        './inventory/**/*.html',
        '../../**/templates/**/*.html',
        // Add other paths where Tailwind CSS classes are used
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
        require('daisyui'),
    ],
    daisyui: {
        themes: ["light", "dark", "cupcake"],
    },
}
