function loadTitle() {
    const UrlParams = new URLSearchParams(window.location.search);
    const id = UrlParams.get("id");

    let http = new XMLHttpRequest();
    http.onreadystatechange = function() {
        if (this.readyState === 4 && this.status === 200) {
            let json = jsonParse(this.responseText);

            let title = document.getElementsByClassName("title")[0];
            title.children[0].innerHTML = json["title"];
        }
    };
    http.open("GET", "api/papers/get?id=" + id);
    http.send(null);
}

function sendReview() {
    const UrlParams = new URLSearchParams(window.location.search);
    const id = UrlParams.get("id");

    let radioValues = document.getElementsByName("evaluation");
    let selectedValue;

    for (let i = 0; i < radioValues.length; i++) {
        if (radioValues[i].checked === true) {
            selectedValue = radioValues[i].value;
        }
    }

    let justificationText = document.getElementById("justification").value;
    let recommendationsText = document.getElementById("recommendations").value;

    let dict = { evaluation: selectedValue,
                justification: justificationText,
                recommendations: recommendationsText };

    let json = JSON.stringify(dict);

    let http = new XMLHttpRequest();
    http.open("POST", "api/review/add?id=" + id);
    http.send(json);
}

function jsonParse(text) {
    let json;
    try {
        json = JSON.parse(text);
    } catch (e) {
        return false;
    }
    return json;
}

function getReviews() {
    let http = new XMLHttpRequest();
    http.onreadystatechange = function() {
        if (this.readyState === 4 && this.status === 200) {
            let table = document.getElementsByTagName("table")[0];
            let old_tbody = document.getElementsByTagName("tbody")[0];
            let new_tbody = document.createElement('tbody');

            let json = jsonParse(this.responseText);

            for(let i = 0; i < json.length; i++) {
                let rev = json[i];
                let row = new_tbody.insertRow();
                Object.keys(rev).forEach(function (k) {
                    let text;
                    let cell = row.insertCell();
                    text = rev[k];
                    cell.appendChild(document.createTextNode(text));
                })
            }
            table.replaceChild(new_tbody, old_tbody);
        }
    };
    http.open("POST", "api/reviews/getAll");
    http.send(null);
}