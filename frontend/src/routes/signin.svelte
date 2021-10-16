<script context="module">
	export async function load({ session }) {
		if (session.user) {
			return {
				status: 302,
				redirect: '/'
			};
		}
		return {};
	}
</script>

<script>
	import { session } from '$app/stores';
	import { goto } from '$app/navigation';
	import { login } from '$lib/utils.js';
	import Alert from '$lib/components/Alert.svelte';

	let username = '';
	let password = '';
	let errors = null;

	async function submit(event) {
		const response = await login(
			`http://localhost:3000/backend/auth/signin`,
			new URLSearchParams({
				username,
				password
			})
		);
		// TODO handle network errors
		errors = JSON.stringify(response.detail);
		if (response.user) {
			$session.user = response.user;
			goto('/');
		}
	}
</script>

<svelte:head>
	<title>Sign In</title>
</svelte:head>

<div class="flex flex-col text-left w-full mb-6">
	<h1 class="sm:text-3xl text-2xl font-medium title-font mb-4 text-gray-900">Sign In</h1>
</div>
<div
	class="lg:w-1/3 md:w-1/2 bg-white rounded-lg p-8 flex flex-col w-full mt-10 md:mt-0 relative z-10 shadow-md"
>
	<Alert {errors} />
	<form on:submit|preventDefault={submit}>
		<div class="relative mb-4">
			<label for="username" class="leading-7 text-sm text-gray-600">Username</label>
			<input
				type="text"
				id="username"
				name="username"
				class="w-full bg-white rounded border border-gray-300 focus:border-red-500 focus:ring-2 focus:ring-red-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out"
				bind:value={username}
				required
			/>
		</div>
		<div class="relative mb-4">
			<label for="password" class="leading-7 text-sm text-gray-600">Password</label>
			<input
				type="password"
				id="password"
				name="password"
				class="w-full bg-white rounded border border-gray-300 focus:border-red-500 focus:ring-2 focus:ring-red-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out"
				bind:value={password}
				required
			/>
		</div>
		<button
			type="submit"
			class="text-white bg-red-500 border-0 py-2 px-6 focus:outline-none hover:bg-red-600 rounded text-lg"
		>
			Sign In
		</button>
	</form>
	<p class="text-xs text-gray-500 mt-3">
		Don't have account?
		<a href="/signup" class="text-red-500"> Sign Up. </a>
	</p>
</div>
