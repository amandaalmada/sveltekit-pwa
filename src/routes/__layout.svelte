<script>
	import '../app.css';
	import { onMount } from 'svelte';
	import { browser } from '$app/env';

	onMount(async () => {
		if (browser) {
			const notifications = await import('$lib/messaging');
			await notifications.requireNotificationsPermission();
		}
	});
</script>

<slot />
