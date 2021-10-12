/** @type {import('@sveltejs/kit').Config} */
import node_adapter from '@sveltejs/adapter-node';
const config = {
	kit: {
		// hydrate the <div id="svelte"> element in src/app.html
		target: '#svelte',
		adapter: node_adapter({
			// default options are shown
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
