<svelte:head>
	<title>Map example</title>
	<script src='https://api-maps.yandex.ru/2.1/?lang=ru_RU&amp;apikey=cf1b8beb-bb0c-4563-9d28-c603002dd2ad'
			type="text/javascript" on:load={() => ymaps.ready(loadMap)}>
	</script>
</svelte:head>

<script>
	import Router from "svelte-spa-router";
	import Main from "routes/Main.svelte";
	import Map from "routes/Map.svelte";
	import UserMap from "routes/UserMap.svelte";
	import {onMount} from "svelte";

	const routes = {
		'/': Main,
		'/map': Map,
		'/umap': UserMap,
	}

	export let locations = [{
		latitude: 55.75361503443606,
		longitude: 37.620883000000006,
		name: 'Test point'
	}];
	export let center = [55.75361503443606, 37.620883000000006];
	export let zoom = 17;
	let Loaded = false;
	function loadMap() {
		var myMap = new ymaps.Map("map", {
			center: center,
			zoom: zoom
		});
		// Создаем геообъект с типом геометрии "Точка".
		const points = myMap.geoObjects;
		locations.forEach(location => {
			points.add(new ymaps.Placemark(
					[location.latitude, location.longitude],
					{balloonContent: location.name},
					{
					}));
		});
		Loaded = true;
	}
	function getUserLocation() {
		var location = ymaps.geolocation.get();

		location.then(
				function(result) {
					// Добавление местоположения на карту.
					myMap.geoObjects.add(result.geoObjects)
				},
				function(err) {
					console.log('Ошибка: ' + err)
				}
		);
	}
</script>

<Router {routes}/>
<div>
	{#if Loaded === false}
		<h1>Loading...</h1>
	{/if}
</div>
<div id="map"></div>

<style>
	#map {
		width: 720px;
		height: 540px;
	}
</style>