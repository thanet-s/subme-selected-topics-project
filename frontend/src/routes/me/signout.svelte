<script>
	import { session } from '$app/stores';
	import { goto } from '$app/navigation';
	import { onMount } from 'svelte';

	onMount(async () => {
		const res = await fetch(`http://localhost:3000/backend/auth/signout`, {
			method: 'POST'
		});
		const data = await res.json();
		if (data.success) {
            setTimeout(() => {
                $session.user = null;
				goto('/');
			}, 1500);
		}
	});
</script>

<svelte:head>
	<title>Sign out</title>
</svelte:head>

<div class="flex items-center justify-center">
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
			<circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" />
			<path
				class="opacity-75"
				fill="currentColor"
				d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
			/>
		</svg>
		Loging out...
	</button>
</div>
