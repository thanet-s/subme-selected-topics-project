<script>
	import { session } from '$app/stores';
</script>

<div class="md:w-1/3 lg:w-2/12 bg-white shadow-md">
	<nav class="flex flex-col overflow-x-hidden overflow-y-auto">
		<ul class="flex flex-col">
			<li>
				<a
					href="/"
					class="flex flex-row items-center h-12 transform shadow-sm hover:translate-x-2 transition-transform ease-in duration-200 text-gray-500 hover:text-gray-800 hover:bg-red-100"
				>
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
								d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"
							/>
						</svg>
					</span>
					<span class="text-sm font-medium">Home</span>
				</a>
			</li>
			<li>
				<a
					href="/public"
					class="flex flex-row items-center h-12 transform shadow-sm hover:translate-x-2 transition-transform ease-in duration-200 text-gray-500 hover:text-gray-800 hover:bg-red-100"
				>
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
								d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
							/>
						</svg>
					</span>
					<span class="text-sm font-medium">Public Videos</span>
				</a>
			</li>
			{#if $session.user}
				<li>
					<a
						href="/me/following"
						class="flex flex-row items-center h-12 transform shadow-sm hover:translate-x-2 transition-transform ease-in duration-200 text-gray-500 hover:text-gray-800 hover:bg-red-100"
					>
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
									d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"
								/>
							</svg>
						</span>
						<span class="text-sm font-medium">Following</span>
					</a>
				</li>
				<li>
					<a
						href="/me"
						class="flex flex-row items-center h-12 transform shadow-sm hover:translate-x-2 transition-transform ease-in duration-200 text-gray-500 hover:text-gray-800 hover:bg-red-100"
					>
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
									stroke-width="2"
									d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"
								/>
							</svg>
						</span>
						<span class="text-sm font-medium">My Videos</span>
					</a>
				</li>
				<li>
					<a
						href="/me/upload"
						class="flex flex-row items-center h-12 transform shadow-sm hover:translate-x-2 transition-transform ease-in duration-200 text-gray-500 hover:text-gray-800 hover:bg-red-100"
					>
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
									d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"
								/>
							</svg>
						</span>
						<span class="text-sm font-medium">Upload</span>
					</a>
				</li>
				<li>
					<a
						href="/me/signout"
						class="flex flex-row items-center h-12 transform shadow-sm hover:translate-x-2 transition-transform ease-in duration-200 text-gray-500 hover:text-gray-800 hover:bg-red-100"
					>
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
									d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"
								/>
							</svg>
						</span>
						<span class="text-sm font-medium">Sign out</span>
					</a>
				</li>
			{:else}
				<li>
					<a
						href="/signup"
						class="flex flex-row items-center h-12 transform shadow-sm hover:translate-x-2 transition-transform ease-in duration-200 text-gray-500 hover:text-gray-800 hover:bg-red-100"
					>
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
									d="M18 9v3m0 0v3m0-3h3m-3 0h-3m-2-5a4 4 0 11-8 0 4 4 0 018 0zM3 20a6 6 0 0112 0v1H3v-1z"
								/>
							</svg>
						</span>
						<span class="text-sm font-medium">Sign Up</span>
					</a>
				</li>
			{/if}
		</ul>
	</nav>
</div>
