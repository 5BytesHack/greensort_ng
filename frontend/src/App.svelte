<script>
	import Router from "svelte-spa-router";
	import Map from "./routes/Map.svelte";
	import UserMap from "./routes/UserMap.svelte";

	export let fractions;
	export let markings;
	const routes = {
		'/map': Map,
		'/umap': UserMap,
	}
</script>


<main>
	<nav class="navbar navbar-expand-lg navbar-light" style="background-color: #e3f2fd;">
		<div class="collapse navbar-collapse" id="navbarNav">
			<ul class="navbar-nav">
				<li class="nav-item">
					<a class="nav-link" href="/#/map">По материалу</a>
				</li>
				<li class="nav-item">
					<a class="nav-link" href="/#/umap">По маркировке</a>
				</li>
			</ul>
		</div>
	</nav>
	<h1>Веб приложение для поиска точки сбора определённых отходов</h1>
	<Router {routes}/>
</main>



<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}
	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}
	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>