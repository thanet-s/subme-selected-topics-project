<script>
    import { session } from "$app/stores";
	import VideoCard from "$lib/components/VideoCard.svelte";
	const fake_video = {
		id: 1,
		title: 'Hi CS',
		user: "jojo",
		create_at: '2021-10-15T07:51:56.822901+00:00'
	};
</script>

<svelte:head>
    <title>{$session.user.username} - profile</title>
</svelte:head>

<div class="flex flex-col text-left w-full mb-6">
    <h1 class="sm:text-3xl text-2xl font-medium title-font mb-4 text-gray-900">{$session.user.username}</h1>
    
</div>

<div class="flex flex-wrap -m-4">
        <VideoCard {...fake_video}/>
</div>