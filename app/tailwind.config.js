console.log(process.env.NODE_ENV)

module.exports = {
	// safelist: [{ pattern: /.*/, }],
	content: [
		"./static/css/tailwind.css",
		"./templates/*.jinja",
		"./templates/*.html",
	],
	theme: {
		extend: {},
	},
	plugins: [],
}