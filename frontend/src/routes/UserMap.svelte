<svelte:head>
    <title>Map example</title>
    <script src='https://api-maps.yandex.ru/2.1/?lang=ru_RU&amp;apikey=cf1b8beb-bb0c-4563-9d28-c603002dd2ad'
            type="text/javascript">
    </script>
</svelte:head>

<script>
    import axios from "axios";

    let url = "http://localhost:8000/id/"
    //export let markings;
    const fractions = [
        {'id': 1, 'type': 'PET 01'},
        {'id': 1, 'type': 'PET 1'},
        {'id': 1, 'type': 'PET'},
        {'id': 1, 'type': '01'},
        {'id': 1, 'type': '1'},
        {'id': 1, 'type': 'HDPE 02'},
        {'id': 1, 'type': 'HDPE 2'},
        {'id': 1, 'type': 'HDPE'},
        {'id': 1, 'type': '02'},
        {'id': 1, 'type': '2'},
        {'id': 1, 'type': 'LDPE 04'},
        {'id': 1, 'type': 'LDPE 4'},
        {'id': 1, 'type': 'LDPE'},
        {'id': 1, 'type': '04'},
        {'id': 1, 'type': '4'},
        {'id': 1, 'type': 'PP 05'},
        {'id': 1, 'type': 'PP 5'},
        {'id': 1, 'type': 'PP'},
        {'id': 1, 'type': '05'},
        {'id': 1, 'type': '5'},
        {'id': 1, 'type': 'PS 06'},
        {'id': 1, 'type': 'PS 6'},
        {'id': 1, 'type': 'PS'},
        {'id': 1, 'type': '06'},
        {'id': 1, 'type': '6'},
        {'id': 2, 'type': 'FE 40'},
        {'id': 2, 'type': 'FE'},
        {'id': 2, 'type': '40'},
        {'id': 2, 'type': 'ALU 41'},
        {'id': 2, 'type': 'ALU'},
        {'id': 2, 'type': '41'},
        {'id': 3, 'type': 'PAP 20'},
        {'id': 3, 'type': 'PAP'},
        {'id': 3, 'type': '20'},
        {'id': 3, 'type': 'PAP 21'},
        {'id': 3, 'type': '21'},
        {'id': 3, 'type': 'PAP 22'},
        {'id': 3, 'type': '22'},
        {'id': 4, 'type': 'GL 70'},
        {'id': 4, 'type': 'GL'},
        {'id': 4, 'type': '70'},
        {'id': 4, 'type': 'GL 71'},
        {'id': 4, 'type': '71'},
        {'id': 4, 'type': 'GL 72'},
        {'id': 4, 'type': '72'},
        {'id': 4, 'type': 'GLS 73'},
        {'id': 4, 'type': 'GLS'},
        {'id': 4, 'type': '73'},
        {'id': 4, 'type': 'GLS 74'},
        {'id': 4, 'type': '74'},
        {'id': 14, 'type': 'PVC 03'},
        {'id': 14, 'type': 'PVC 3'},
        {'id': 14, 'type': 'PVC'},
        {'id': 14, 'type': '03'},
        {'id': 14, 'type': '3'},
        {'id': 14, 'type': 'OTHER 07'},
        {'id': 14, 'type': 'OTHER 7'},
        {'id': 14, 'type': 'OTHER'},
        {'id': 14, 'type': '07'},
        {'id': 14, 'type': '7'},
        {'id': 14, 'type': 'C/PP'},
        {'id': 14, 'type': 'C/LDPE'}
    ];
    export let locations = [];
    let id;
    async function get_coords() {
        let c = await axios.get(url, {
            "params": {
                "id": id
            }
        })
        for (let i = 0; i < c.data.trashers.length; i++) {
            let coords = c.data.trashers[i].coords.split(",");
            locations.push({
                latitude: coords[0],
                longitude: coords[1],
                name: c.data.trashers[i].address
            })
        }
    }
    export let center = [45.0448, 38.976];
    export let zoom = 13;
    let Loaded = false;
    function loadMap() {
        var myMap = new ymaps.Map("map", {
            center: center,
            zoom: zoom
        });
        // Создаем геообъект с типом геометрии "Точка".
        // const points = myMap.geoObjects;
        const cl = []
        locations.forEach(location => {
            cl.push(new ymaps.Placemark(
                [location.latitude, location.longitude],
                {balloonContent: location.name},
                {
                }))
            // points.add(new ymaps.Placemark(
            //     [location.latitude, location.longitude],
            //     {balloonContent: location.name},
            //     {
            //     }));
        });
        var myClusterer = new ymaps.Clusterer();
        myClusterer.add(cl);
        myMap.geoObjects.add(myClusterer);
        Loaded = true;
    }
</script>
<main>
    <form>
        <div class="form-group">
            <label for="exampleFormControlSelect1">Выберите маркировку</label>
            <select bind:value={id} on:change={get_coords} class="form-control" id="exampleFormControlSelect1">
                {#each fractions as fraction}
                    <option value={fraction.id}>{fraction.type}</option>
                {/each}
            </select>
        </div>
    </form>
    <button type="button" class="btn btn-success" on:click={loadMap}>Получить пункты сортировки</button>
    <div id="map"></div>
</main>

<style>
    #map {
        width: 720px;
        height: 540px;
    }
</style>