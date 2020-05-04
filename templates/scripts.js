function loadTitle() {
    // Function used by multiple modules
    const UrlParams = new URLSearchParams(window.location.search);
    const id = UrlParams.get("id");

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


function sendReviewer() {
    let combobox = document.getElementsByTagName("select");

    let result = [];

    for (let i = 0; i < combobox.length; i++) {
        let id = combobox[i].id.substring(16);
        let choice = combobox[i].value;
        // let reviewerId = choice.split()

        let dict = {
            id: id,
            choice: choice
        };

        result.push(dict);
    }

    let json = JSON.stringify(result);

    let http = new XMLHttpRequest();
    http.open("POST", "api/paper/sendReviewer", true); //fixme
    http.send(json);
}