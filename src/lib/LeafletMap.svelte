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

			leaflet
				.polygon([
					[-25.2518, -57.6033],
					[-25.2528, -57.6018],
					[-25.2543, -57.6014],
					[-25.2536, -57.5978],
					[-25.2525, -57.5984],
					[-25.2487, -57.5995],
					[-25.2497, -57.6025],
					[-25.2507, -57.604]
				])
				.addTo(map);
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
