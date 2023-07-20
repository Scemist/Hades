import { defineConfig } from "vite"

export default defineConfig({
	build: {
		root: 'static/javascript',	
		outDir: 'static/build/assets',
		rollupOptions: {
			input: 'static/javascript/app.js',
			output: {
				entryFileNames: `[name].js`,
				chunkFileNames: `[name].js`,
				assetFileNames: `[name].[ext]`
			}
		},
	},
	server: {
		hmr: true
	}
})