function loadTitle() {
    // Function used by multiple modules

    console.log("loadTitle --- entered");

    const UrlParams = new URLSearchParams(window.location.search);
    const id = UrlParams.get("id");

    console.log(id);

    let http = new XMLHttpRequest();
    http.onreadystatechange = function () {
        if (this.readyState === 4 && this.status === 200) {
            let json = jsonParse(this.responseText);

            let title = document.getElementsByClassName("title")[0];
            title.children[0].innerHTML = json["title"];
        }
    };
    http.open("GET", "api/papers/get?id=" + id, true);
    http.send(null);
}

function jsonParse(text) {
    // Function used by multiple modules
    let json;
    try {
        json = JSON.parse(text);
    } catch (e) {
        return false;
    }
    return json;
}

function getUserType() {
    // Function (potentially?) used by multiple modules
    let http = new XMLHttpRequest();
    http.open("GET", "api/user/getUserType", false);
    http.send(null);

    let response = http.responseText;
    let json = jsonParse(response);

    return json["type"];
}