<script context="module">
	export function load({ error, status }) {
		return {
			props: {
				title: `${status}: ${error.message}`
			}
		};
	}
</script>

<script>
	export let title;
</script>

<svelte:head>
	<title>{title} - Subme</title>
</svelte:head>


<div class="flex flex-col text-center w-full mb-20">
	<h1 class="sm:text-3xl text-2xl font-medium title-font mb-4 text-gray-900">
		{title}
	</h1>
</div>
