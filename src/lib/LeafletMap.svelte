<script>
	import { onMount } from 'svelte';
	import { browser } from '$app/env';

	onMount(async () => {
		if (browser) {
			const leaflet = await import('leaflet');

			const map = leaflet.map('map').setView([-25.302241662664127, -57.58034997736135], 13);

			leaflet
				.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
					attribution:
						'&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
				})
				.addTo(map);

			leaflet
				.marker([-25.302241662664127, -57.58034997736135])
				.addTo(map)
				.bindPopup('Usted se encuentra aquí.<br> Haga click derecho para guardar.')
				.openPopup();
		}
	});
</script>

<main>
	<div id="map" />
</main>

<style>
	@import 'https://unpkg.com/leaflet@1.7.1/dist/leaflet.css';
	main #map {
		height: 800px;
	}
</style>
