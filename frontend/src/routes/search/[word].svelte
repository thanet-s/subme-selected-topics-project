<script context="module">
	/**
	 * @type {import('@sveltejs/kit').Load}
	 */
	export async function load({ page, fetch, session, stuff }) {
		const url = `http://localhost:3000/backend/video/search-${page.params.word}`;
		const res = await fetch(url);

		if (res.ok) {
			return {
				props: {
					videos: await res.json(),
                    word: page.params.word
				}
			};
		}

		return {
			status: res.status,
			error: new Error(`Could not load ${url}`)
		};
	}
</script>

<script>
	import VideoCard from '$lib/components/VideoCard.svelte';
	export let videos;
    export let word;
</script>

<svelte:head>
	<title>Search {word}</title>
</svelte:head>

<div class="flex flex-wrap -m-4">
	{#each videos as v}
		<VideoCard {...v} />
	{/each}
</div>