<header class="text-gray-50 body-font bg-gray-800">
	<div class="mx-auto flex flex-wrap px-5 py-3 flex-col md:flex-row items-center">
		<a
			href="/"
			class="md:mr-auto flex title-font font-medium items-center text-gray-50 mb-4 md:mb-0 hover:text-red-600"
		>
			<svg
				xmlns="http://www.w3.org/2000/svg"
				class="w-10 h-10 text-white p-1 bg-red-600 rounded-full hover:bg-red-700"
				fill="none"
				viewBox="0 0 24 24"
				stroke="currentColor"
			>
				<path
					stroke-linecap="round"
					stroke-linejoin="round"
					stroke-width="2"
					d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z"
				/>
				<path
					stroke-linecap="round"
					stroke-linejoin="round"
					stroke-width="2"
					d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
				/>
			</svg>
			<span class="ml-3 text-xl">Subme</span>
		</a>
		<div class="relative text-black">
			<form action="GET">
				<div class="absolute top-4 left-3">
					<svg
						xmlns="http://www.w3.org/2000/svg"
						class="h-6 w-6 text-gray-400 z-20 hover:text-gray-500"
						fill="none"
						viewBox="0 0 24 24"
						stroke="currentColor"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2"
							d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
						/>
					</svg>
				</div>
				<input
					type="text"
					class="h-14 w-full md:w-96 pl-10 pr-20 rounded-lg z-0 focus:ring-2 focus:ring-red-600"
					placeholder="Search anything..."
				/>
				<div class="absolute top-0 right-0">
					<button
						type="submit"
						class="h-14 w-20 text-white rounded-r-lg bg-red-500 hover:bg-red-600"
					>
						Search
					</button>
				</div>
			</form>
		</div>
		<nav class="md:ml-auto flex flex-wrap items-center text-base justify-center">
			<a href="/signin" class="flex flex-row items-center md:mr-5 hover:text-red-600">
				<span class="inline-flex items-center justify-center h-12 w-12 text-lg text-gray-400">
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
							d="M11 16l-4-4m0 0l4-4m-4 4h14m-5 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h7a3 3 0 013 3v1"
						/>
					</svg>
				</span>
				<span class="text-sm font-medium">Sign In</span></a
			>
		</nav>
	</div>
</header>
