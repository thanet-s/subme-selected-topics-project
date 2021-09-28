<svelte:head>
	<title>สวัสดีชาวโลก</title>
</svelte:head>

<script>
    let count = 0;
    const buttonHandle = () => {
      count = count+1  
    };
</script>

<h1>สวัสดีชาวโลก!</h1>

<button on:click={buttonHandle}>click to increate</button>

<p>Count is {count}</p>