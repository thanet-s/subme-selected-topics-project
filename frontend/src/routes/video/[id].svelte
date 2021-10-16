<script context="module">
	/**
	 * @type {import('@sveltejs/kit').Load}
	 */
	export async function load({ page, fetch, session, stuff }) {
		const url = `http://localhost:3000/backend/video/get-${page.params.id}`;
		const res = await fetch(url);

		if (res.ok) {
			return {
				props: {
					video: await res.json()
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
	export let video;
</script>

<div class="aspect-w-16 aspect-h-9">
	<video width="100%" height="100%" controls autoplay>
		<source src={`/bucket/video/${video.id}`} />
		<track kind="captions">
		Your browser does not support the video tag.
	</video>
</div>

<div class="flex flex-col text-left w-full mb-1">
	<h1 class="sm:text-3xl text-2xl font-medium title-font mb-4 text-gray-900">
		{video.title}
	</h1>
</div>
<div class="flex flex-col text-left w-full mb-1">
	<p class="sm:text-1xl text-xl mb-4 text-gray-900">
		By: {video.user.username}
    </p>
</div>
<div class="flex flex-col text-left w-full mb-1">
	<p class=" mb-4 text-gray-900">
		{video.description}
    </p>
</div>