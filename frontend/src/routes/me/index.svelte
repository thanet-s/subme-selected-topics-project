<script context="module">
	/**
	 * @type {import('@sveltejs/kit').Load}
	 */
	export async function load({ page, fetch, session, stuff }) {
		const url = `http://localhost:3000/backend/user/videos`;
		const res = await fetch(url);

		if (res.ok) {
			return {
				props: {
					videos: await res.json()
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
	import { session } from '$app/stores';
	import VideoCard from '$lib/components/VideoCard.svelte';
	export let videos;
</script>

<svelte:head>
	<title>{$session.user.username} - profile</title>
</svelte:head>

<div class="flex flex-col text-left w-full mb-6">
	<h1 class="sm:text-3xl text-2xl font-medium title-font mb-4 text-gray-900">
		{$session.user.username}
	</h1>
</div>

<div class="flex flex-wrap -m-4">
	{#each videos as v}
		<VideoCard {...v} />
	{/each}
</div>
