<svelte:head>
    <title>Map example</title>
    <script src='https://api-maps.yandex.ru/2.1/?lang=ru_RU&amp;apikey=cf1b8beb-bb0c-4563-9d28-c603002dd2ad'
            type="text/javascript">
    </script>
</svelte:head>

<script>
    import axios from "axios";

    let url = "http://web:8000/id/"
    //export let markings;
    const fractions = [
        {
            "id": 1,
            "material": "Пластик",
        },
        {
            "id": 2,
            "material": "Металл",
        },
        {
            "id": 3,
            "material": "Бумага",
        },
        {
            "id": 4,
            "material": "Стекло",
        },
        {
            "id": 5,
            "material": "Одежда",
        },
        {
            "id": 6,
            "material": "Батарейки",
        },
        {
            "id": 7,
            "material": "Лампочки",
        },
        {
            "id": 8,
            "material": "Техника",
        },
        {
            "id": 9,
            "material": "Крышечки",
        },
        {
            "id": 10,
            "material": "Шины",
        },
        {
            "id": 11,
            "material": "Зубные щётки",
        },{
            "id": 12,
            "material": "Градусники",
        },
        {
            "id": 13,
            "material": "Иное",
        }
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
            <label for="exampleFormControlSelect1">Выберите материал</label>
            <select bind:value={id} on:change={get_coords} class="form-control" id="exampleFormControlSelect1">
                {#each fractions as fraction}
                    <option value={fraction.id}>{fraction.material}</option>
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