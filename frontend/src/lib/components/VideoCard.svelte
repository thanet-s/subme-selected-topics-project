<script>
	import { onMount } from 'svelte';
	import dayjs from 'dayjs';
	import relativeTime from 'dayjs/plugin/relativeTime';
	dayjs.extend(relativeTime);

    export let id;
	export let title;
	export let user;
	export let created_at;
	let time = null;

	onMount(async () => {
		setTimeout(() => {
			time = dayjs(created_at).fromNow().toString();
		}, 100);
	});
</script>

{#if time}
	<div class="lg:w-1/4 md:w-1/2 p-4 w-full">
		<a href={`/video/${id}`} class="block relative rounded shadow-md overflow-hidden">
			<div class="aspect-w-16 aspect-h-9">
				<img
					alt="he Catalyzer"
					class="object-cover object-center w-full h-full block"
					src="https://dummyimage.com/420x260"
				/>
			</div>
		</a>
		<div class="mt-1 ml-1">
			<h2 class="text-gray-900 title-font text-lg font-medium">{title}</h2>
			<p><a href={`/user/${user.username}`}>{user.username}</a></p>
			<p class="text-gray-500 text-xs tracking-widest title-font mb-1">{time}</p>
		</div>
	</div>
{:else}
	<div class="animate-pulse lg:w-1/4 md:w-1/2 p-4 w-full">
		<a href="#!" class="block relative rounded shadow-md overflow-hidden">
			<div class="aspect-w-16 aspect-h-9 bg-red-400" />
		</a>
		<div class="mt-2 ml-1">
			<div class="space-y-2">
				<div class="h-4 bg-red-400 rounded w-3/4" />
				<div class="pt-4 h-4 bg-red-400 rounded w-1/4" />
				<div class="h-4 bg-red-400 rounded w-1/2" />
			</div>
		</div>
	</div>
{/if}
