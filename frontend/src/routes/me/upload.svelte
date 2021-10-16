<script>
	import Alert from '$lib/components/Alert.svelte';
	import { goto } from '$app/navigation';
    

	let is_private = false;
	let title = '';
	let description = '';
	let errors = null;
	let videofile;
    let coverfile;
	let uploading = false;

	const getUploadUrl = async (event) => {
        uploading = true;
        const dataArray = new FormData();
        dataArray.append("is_private", is_private);
        dataArray.append("title", title);
        dataArray.append("description", description);
        dataArray.append("videofile", videofile);
        dataArray.append("coverfile", coverfile);
		const res_data = await fetch(`http://localhost:3000/backend/user/upload`, {
			method: 'POST',
			body: dataArray
		}).then((r) => r.json());
		errors = JSON.stringify(res_data.detail);
		if (res_data.success) {
			goto(`/video/${res_data.video.id}`);
		}
	};

	const onVideoSelected = (e) => {
		let video = e.target.files[0];
		videofile = video;
	};

    const onCoverSelected = (e) => {
		let cover = e.target.files[0];
		coverfile = cover;
	};
</script>

<svelte:head>
	<title>Upload</title>
</svelte:head>

<div class="flex flex-col text-left w-full mb-6">
	<h1 class="sm:text-3xl text-2xl font-medium title-font mb-4 text-gray-900">Upload</h1>
</div>

<div
	class="lg:w-1/2 md:w-2/3 bg-white rounded-lg p-8 flex flex-col w-full mt-10 md:mt-0 relative z-10 shadow-md"
>
	<Alert {errors} />
	<form on:submit|preventDefault={getUploadUrl}>
		<div class="flex flex-wrap -m-2">
			<div class="p-2 w-full">
				<div class="relative">
					<label for="title" class="leading-7 text-sm text-gray-600">Title</label>
					<input
						type="text"
						id="title"
						name="title"
						required
						bind:value={title}
						class="w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-red-500 focus:bg-white focus:ring-2 focus:ring-red-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out"
					/>
				</div>
			</div>
			<div class="p-2 w-full">
				<div class="relative">
					<div
						class="relative inline-block w-10 mr-2 align-middle select-none transition duration-200 ease-in"
					>
						<input
							type="checkbox"
							name="toggle"
							id="toggle"
							bind:checked={is_private}
							class="toggle-checkbox absolute block w-6 h-6 rounded-full bg-white border-4 appearance-none cursor-pointer"
						/>
						<label
							for="toggle"
							class="toggle-label block overflow-hidden h-6 rounded-full bg-gray-300 cursor-pointer"
						/>
					</div>
					<label for="toggle" class="text-xs text-gray-700"
						>{#if is_private}Private video{:else}Public video{/if}</label
					>
					<div class="p-2 w-full">
						<div class="relative">
							<label for="description" class="leading-7 text-sm text-gray-600">Description</label>
							<textarea
								id="description"
								name="description"
								bind:value={description}
								class="w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-red-500 focus:bg-white focus:ring-2 focus:ring-red-200 h-32 text-base outline-none text-gray-700 py-1 px-3 resize-none leading-6 transition-colors duration-200 ease-in-out"
							/>
						</div>
					</div>
				</div>
			</div>

			<div class="pl-2 pt-4 w-full">
				<label
					class="w-64 flex flex-col items-center px-4 py-6 bg-white rounded-md shadow-md tracking-wide uppercase border border-blue cursor-pointer hover:bg-red-600 hover:text-white text-red-600 ease-linear transition-all duration-150"
				>
					<svg
						xmlns="http://www.w3.org/2000/svg"
						class="h-6 w-6"
						fill="none"
						viewBox="0 0 24 24"
						stroke="currentColor"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2"
							d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"
						/>
					</svg>
					<span class="mt-2 text-base leading-normal">Select video</span>
					<input type="file" class="hidden" accept="video/*" on:change={onVideoSelected} required />
				</label>
				<div class="pt-4 w-full">
					{#if videofile}
						<p>{videofile.name}</p>
					{/if}
				</div>
			</div>

            <div class="pl-2 pt-4 w-full">
				<label
					class="w-64 flex flex-col items-center px-4 py-6 bg-white rounded-md shadow-md tracking-wide uppercase border border-blue cursor-pointer hover:bg-red-600 hover:text-white text-red-600 ease-linear transition-all duration-150"
				>
					<svg
						xmlns="http://www.w3.org/2000/svg"
						class="h-6 w-6"
						fill="none"
						viewBox="0 0 24 24"
						stroke="currentColor"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2"
							d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"
						/>
					</svg>
					<span class="mt-2 text-base leading-normal">Select Cover</span>
					<input type="file" class="hidden" accept="image/*" on:change={onCoverSelected} required />
				</label>
				<div class="pt-4 w-full">
					{#if coverfile}
						<p>{coverfile.name}</p>
					{/if}
				</div>
			</div>

			<div class="p-2 w-full">
				{#if !uploading}
					<button
						type="submit"
						class="flex mx-auto text-white bg-red-500 border-0 py-2 px-8 focus:outline-none hover:bg-red-600 rounded text-lg"
					>
						Upload
					</button>
				{:else}
					<button
						type="button"
						class="inline-flex items-center px-4 py-2 border border-transparent text-base leading-6 font-medium rounded-md text-white bg-red-600 hover:bg-red-500 focus:border-red-700 active:bg-red-700 transition ease-in-out duration-150 cursor-not-allowed"
						disabled=""
					>
						<svg
							class="animate-spin -ml-1 mr-3 h-5 w-5 text-white"
							xmlns="http://www.w3.org/2000/svg"
							fill="none"
							viewBox="0 0 24 24"
						>
							<circle
								class="opacity-25"
								cx="12"
								cy="12"
								r="10"
								stroke="currentColor"
								stroke-width="4"
							/>
							<path
								class="opacity-75"
								fill="currentColor"
								d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
							/>
						</svg>
						Processing
					</button>
				{/if}
			</div>
		</div>
	</form>
</div>

<style>
	/* CHECKBOX TOGGLE SWITCH */
	.toggle-checkbox:checked {
		right: 0;
		--tw-bg-opacity: 1;
		border-color: rgba(248, 113, 113, var(--tw-bg-opacity));
	}
	.toggle-checkbox {
		--tw-bg-opacity: 1;
		border-color: rgba(52, 211, 153, var(--tw-bg-opacity));
	}
	.toggle-checkbox:checked + .toggle-label {
		--tw-bg-opacity: 1;
		background-color: rgba(248, 113, 113, var(--tw-bg-opacity));
	}
</style>
