import App from './App.svelte';

const app = new App({
	target: document.body,
	props: {
		base_url: 'localhost:8000'
	}
});

export default app;