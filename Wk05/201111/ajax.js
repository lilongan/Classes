const ajax = (url, callback, method = "GET") => {
    if (!url) return console.error("Request Required");
    if (!callback) return console.error("Callback Required");
    const request = new XMLHttpRequest();
    request.addEventListener("readystatechange", (evt) => {
        let req = evt.target;
        if (req.readyState !== 4) return;
        if (req.status === 200) return callback(req.response);
        callback("");
        });
    request.open(method, url);
    request.send();
    };

    let button = document.querySelector("button")
    button.addEventListener("click", () => {
        let lon = document.querySelector("#lon").value;
        let lat = document.querySelector("#lat").value;
        //Only if you have your own cors-anywhere
        ajax("http://localhost:5432/" + `https://www.metaweather.com/api/location/search/?lattlong=${lat}, ${lon}`, (r) => {
            let people = JSON.parse(r);
            console.log(r);
        })
    })
    src="data.json"

    ajax("data.json", (r)=>{
        console.log(JSON.parse(r))
    })
