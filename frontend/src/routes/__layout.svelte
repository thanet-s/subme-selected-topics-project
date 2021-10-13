<script>
	import '../styles/tailwind-output.css';
	import Header from '$lib/components/Header.svelte';
	import Sidebar from '$lib/components/Sidebar.svelte';
	import Footer from '$lib/components/Footer.svelte';
</script>

<Header />
<div class="flex-grow bg-gray-100">
	<div class="flex flex-col h-full md:flex-row">
		<Sidebar />
		<main class="w-full">
			<section class="text-gray-600 body-font">
				<div class="container p-5 mx-auto">
					<slot />
				</div>
			</section>
		</main>
	</div>
</div>
<Footer />
