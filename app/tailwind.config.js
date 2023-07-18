console.log(process.env.NODE_ENV)

/** @type {import('tailwindcss').Config} */
module.exports = {
	// safelist: process.env.NODE_ENV === 'development' ? [{ pattern: /./, }] : [],
	safelist: [{ pattern: /./, }],
	// content: ["./static/css/*.css", "./templates/*.jinja", "./templates/*.html"],
	theme: {
		extend: {},
	},
	plugins: [],
}