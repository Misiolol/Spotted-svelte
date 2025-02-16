<script>
	import '../app.css';
	import { theme } from "../stores";
	let { children } = $props();
	
	function toggleTheme(){
        theme.set(!$theme);
    }
</script>

<div class="header" class:light-header={!$theme} class:dark-header={$theme}>
	<div class="darkmode-toggle">
		<label class="inline-flex items-center cursor-pointer">
			<div class="toggle-wrapper" class:light-tgwrapper={!$theme} class:dark-tgwrapper={$theme}> <!-- New wrapper for the toggle button -->
				<input 
					type="checkbox" 
					value={theme}
					class="sr-only peer" 
					onclick={toggleTheme}
				/>
				<div class="relative w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-blue-300 dark:peer-focus:ring-blue-800 rounded-full peer dark:bg-gray-700 peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-blue-600 dark:peer-checked:bg-blue-600"></div>
			</div>
		</label>
	</div>
</div>

{@render children()}

<style>
	.header {
		display: flex;
		align-items: center; /* Centers the toggle vertically */
		justify-content: flex-end; /* Align the toggler to the right */
		height: 40px; /* Make header taller */
		padding: 0 20px; /* Padding for spacing */
		transition: all .2s ease-in-out;
	}
	.dark-header{
		background:#040F16;
	}
	.light-header{
		background:white;
	}
	.darkmode-toggle {
		display: flex;
		align-items: center;
	}

	/* Styling for the rectangle behind the toggle */
	.toggle-wrapper {
		transition: all .2s ease-in-out;
		display: flex;
		align-items: center; 
		border-radius: 8px;
		padding: 6px 12px; /* Increased padding for more space around the toggle */
	}
	.dark-tgwrapper {
		background: white;
	}

	.light-tgwrapper {
		background: black;
	}

</style>
