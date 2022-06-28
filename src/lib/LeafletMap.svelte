<script>
	import { onMount } from 'svelte';
	import { browser } from '$app/env';

	function getUserLocation() {
		return new Promise((resolve, reject) => {
			try {
				navigator.geolocation.getCurrentPosition((result) => {
					let userLocation = [result.coords.latitude, result.coords.longitude];
					resolve(userLocation);
				});
			} catch (error) {
				resolve('Error getting user location');
			}
		});
	}

	function getZones() {
		return [
			{
				name: 'Tablada Nueva',
				polygons: [
					[-25.2518, -57.6033],
					[-25.2528, -57.6018],
					[-25.2543, -57.6014],
					[-25.2536, -57.5978],
					[-25.2525, -57.5984],
					[-25.2487, -57.5995],
					[-25.2497, -57.6025],
					[-25.2507, -57.604]
				]
			},
			{
				name: 'Camino Mbigua',
				polygons: [
					[-25.2649, -57.6077],
					[-25.2664, -57.608],
					[-25.2671, -57.6075],
					[-25.2679, -57.6069],
					[-25.2691, -57.6069],
					[-25.2696, -57.6061],
					[-25.2652, -57.6014],
					[-25.2655, -57.6027],
					[-25.2648, -57.6045],
					[-25.2656, -57.6045],
					[-25.2632, -57.607]
				]
			},
			{
				name: 'Bañado Tacumbu',
				polygons: [
					[-25.3016, -57.6628],
					[-25.3015, -57.6658],
					[-25.3031, -57.6673],
					[-25.3037, -57.6673],
					[-25.3076, -57.6693],
					[-25.3127, -57.6708],
					[-25.3172, -57.6701],
					[-25.3172, -57.6616],
					[-25.3138, -57.6621],
					[-25.3111, -57.6637],
					[-25.3082, -57.6637],
					[-25.3055, -57.6642],
					[-25.3037, -57.664]
				]
			},
			{
				name: 'Bañado Santa Ana',
				polygons: [
					[-25.3161, -57.6607],
					[-25.3196, -57.6571],
					[-25.3221, -57.6587],
					[-25.3239, -57.6587],
					[-25.326, -57.6581],
					[-25.3274, -57.6548],
					[-25.3265, -57.6503],
					[-25.3283, -57.6486],
					[-25.3255, -57.6443],
					[-25.3233, -57.6449],
					[-25.3208, -57.6479],
					[-25.3166, -57.6487],
					[-25.3149, -57.6512],
					[-25.3128, -57.6541]
				]
			},
			{
				name: 'Cateura',
				polygons: [
					[-25.3326, -57.6448],
					[-25.3345, -57.6458],
					[-25.3365, -57.6468],
					[-25.338, -57.6457],
					[-25.3398, -57.6441],
					[-25.338, -57.6386],
					[-25.3365, -57.6398],
					[-25.3347, -57.6408],
					[-25.3312, -57.6413],
					[-25.3309, -57.6443]
				]
			}
		];
	}

	onMount(async () => {
		if (browser) {
			const leaflet = await import('leaflet');
			const markercluster = await import('leaflet.markercluster');
			let markers = new markercluster.MarkerClusterGroup();
			console.log(markers);
			const userLocation = await getUserLocation();

			const map = leaflet.map('map').setView(userLocation, 12.5);

			leaflet
				.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
					attribution:
						'&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
				})
				.addTo(map);

			leaflet
				.marker(userLocation)
				.addTo(map)
				.bindPopup('Usted se encuentra aquí.<br> Haga click para registrar su ubicación.')
				.openPopup();

			const zones = getZones();

			zones.forEach((zone) => {
				leaflet
					.polygon(zone.polygons, {
						color: 'red',
						fillColor: '#f03',
						fillOpacity: 0.3,
						name: zone.name
					})
					.addTo(map)
					.bindPopup(zone.name);
			});

			// leaflet
			// 	.polygon(
			// 		zones.polygons,
			// 		{
			// 			color: 'red',
			// 			fillColor: '#f03',
			// 			fillOpacity: 0.3,
			// 			name: zones.name
			// 		}
			// 	)
			// 	.addTo(map);

			// leaflet
			// 	.polygon(

			// 		{
			// 			color: 'red',
			// 			fillColor: '#f03',
			// 			fillOpacity: 0.3
			// 		}
			// 	)
			// 	.addTo(map);

			// leaflet
			// 	.polygon(
			// 		[
			// 			[-25.3016, -57.6628],
			// 			[-25.3015, -57.6658],
			// 			[-25.3031, -57.6673],
			// 			[-25.3037, -57.6673],
			// 			[-25.3076, -57.6693],
			// 			[-25.3127, -57.6708],
			// 			[-25.3172, -57.6701],
			// 			[-25.3172, -57.6616],
			// 			[-25.3138, -57.6621],
			// 			[-25.3111, -57.6637],
			// 			[-25.3082, -57.6637],
			// 			[-25.3055, -57.6642],
			// 			[-25.3037, -57.664]
			// 		],
			// 		{
			// 			color: 'red',
			// 			fillColor: '#f03',
			// 			fillOpacity: 0.3
			// 		}
			// 	)
			// 	.addTo(map);

			// leaflet
			// 	.polygon(
			// 		[
			// 			[-25.3161, -57.6607],
			// 			[-25.3196, -57.6571],
			// 			[-25.3221, -57.6587],
			// 			[-25.3239, -57.6587],
			// 			[-25.326, -57.6581],
			// 			[-25.3274, -57.6548],
			// 			[-25.3265, -57.6503],
			// 			[-25.3283, -57.6486],
			// 			[-25.3255, -57.6443],
			// 			[-25.3233, -57.6449],
			// 			[-25.3208, -57.6479],
			// 			[-25.3166, -57.6487],
			// 			[-25.3149, -57.6512],
			// 			[-25.3128, -57.6541]
			// 		],
			// 		{
			// 			color: 'red',
			// 			fillColor: '#f03',
			// 			fillOpacity: 0.3
			// 		}
			// 	)
			// 	.addTo(map);

			// leaflet
			// 	.polygon(
			// 		[
			// 			[-25.3326, -57.6448],
			// 			[-25.3345, -57.6458],
			// 			[-25.3365, -57.6468],
			// 			[-25.338, -57.6457],
			// 			[-25.3398, -57.6441],
			// 			[-25.338, -57.6386],
			// 			[-25.3365, -57.6398],
			// 			[-25.3347, -57.6408],
			// 			[-25.3312, -57.6413],
			// 			[-25.3309, -57.6443]
			// 		],
			// 		{
			// 			color: 'red',
			// 			fillColor: '#f03',
			// 			fillOpacity: 0.3
			// 		}
			// 	)
			// 	.addTo(map);
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
