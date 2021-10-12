<script>
	import '../styles/tailwind-output.css';
	import Header from '$lib/components/Header.svelte';
	import Footer from '$lib/components/Footer.svelte';
</script>

<Header />
<main class="p-4 flex-grow">
	<slot />
</main>
<Footer />
