console.log(process.env.NODE_ENV)

module.exports = {
	content: [
		"./static/css/tailwind.css",
		"./templates/*.jinja",
		// "./templates/*.html",
		"./templates/components/*.jinja",
	],
	theme: {
		extend: {},
	},
	plugins: [],
}