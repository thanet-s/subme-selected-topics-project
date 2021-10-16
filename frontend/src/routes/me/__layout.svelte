<script context="module">
	export async function load({ session }) {
		if (!session.user) {
			return {
				status: 302,
				redirect: '/signin'
			};
		}
		return {};
	}
</script>

<slot />
