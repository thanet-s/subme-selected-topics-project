<script>
	import { Button, Modal } from 'sveltestrap/src';
	let isOpen = false;
	const toggle = () => (isOpen = !isOpen);
</script>

<svelte:head>
	<title>Subme</title>
</svelte:head>

<Button color="primary" on:click={toggle}>Hello World!</Button>
<Modal body {isOpen} {toggle} header="Hello World!">
	<p>There's a song that we're singing. Come on</p>
	<img
		src="https://i.ytimg.com/vi/NUJIRujygvY/hqdefault.jpg"
		alt="Come on Get Happy"
		class="img-fluid"
	/>
</Modal>
