<script>
	import VideoCard from "$lib/components/VideoCard.svelte";
	const fake_video = {
		id: 1,
		title: 'Hi CS',
		user: "jojo",
		create_at: '2021-10-15T07:51:56.822901+00:00'
	};
</script>

<svelte:head>
	<title>Subme</title>
</svelte:head>

<div class="flex flex-wrap -m-4">
	<VideoCard {...fake_video}/>
</div>
