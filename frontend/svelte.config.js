/** @type {import('@sveltejs/kit').Config} */
import adapter from '@sveltejs/adapter-node';
const config = {
	kit: {
		// hydrate the <div id="svelte"> element in src/app.html
		target: '#svelte',
		adapter: adapter({
			out: 'build',
			precompress: true,
			env: {
				host: 'HOST',
				port: 'PORT'
			}
		})
	}
};

export default config;
