<script>
	import '../styles/tailwind-output.css';
	import Header from '$lib/components/Header.svelte';
	import Sidebar from '$lib/components/Sidebar.svelte';
	import Footer from '$lib/components/Footer.svelte';
</script>

<Header />
<div class="flex-grow bg-gray-50">
	<div class="flex flex-row h-full">
		<Sidebar />
		<main class="w-full">
			<slot />
		</main>
	</div>
</div>
<Footer />
