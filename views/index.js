const get_distance = (deaTo, user_lat, user_long) => {
    c1 = (user_lat - deaTo["direccion_coordenada_x"])**2
    c2 = (user_long - deaTo["direccion_coordenada_x"])**2
    ala = (c1+c2)**0.5
    return ala
}
window.navigator.geolocation.getCurrentPosition((position) => {
    
    console.log(position.coords)
    lat = position.coords.latitude
    long = position.coords.longitude
    // console.log(lat,long)
    fetch("https://raw.githubusercontent.com/vgenov-py/projects/master/deas/deas_latlon.json")
    .then((res) => res.json())
    .then((data) => {
        console.log(data["data"][-1])
        const find_one = (dataset, user_lat, user_long) => {
            Hipo= 450000
            const result = [1]
            for (dea of dataset["data"]) {
                const distance = get_distance(dea, user_lat, user_long)
                if (distance <= Hipo) {
                    result.push(dea)
                    result.shift()
                    Hipo=distance
                }
            }
            console.log(result)
            return result
        }
        test = find_one(data, lat, long)
        console.log(test)
        li = document.createElement("li")
        li.innerText = test["direccion_via_nombre"]
        const ul = document.querySelector("#deas")
        ul.append(li)
        for (dea of data["data"]){
            li = document.createElement("li")
            li.innerText = dea["direccion_coordenada_x"]
            // ul.append(li)
        }
    })

})

