<script>
	let isOpen = false;
	const toggle = () => (isOpen = !isOpen);
</script>

<svelte:head>
	<title>Subme</title>
</svelte:head>

<div class="flex flex-wrap -m-4">
	<div class="lg:w-1/4 md:w-1/2 p-4 w-full">
		<a href="#!" class="block relative rounded shadow-md overflow-hidden">
			<div class="aspect-w-16 aspect-h-9">
				<img
					alt="he Catalyzer"
					class="object-cover object-center w-full h-full block"
					src="https://dummyimage.com/420x260"
				/>
			</div>
		</a>
		<div class="mt-1 ml-1">
			<h2 class="text-gray-900 title-font text-lg font-medium">Me at Zoo</h2>
			<p>Jojo</p>
			<p class="text-gray-500 text-xs tracking-widest title-font mb-1">3 years ago</p>
		</div>
	</div>
</div>
