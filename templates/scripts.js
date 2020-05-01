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
    http.open("GET", "api/papers/get?id=" + id, true);
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
    http.open("POST", "api/review/add?id=" + id, true);
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
                let review = json[i];
                let row = new_tbody.insertRow();
                Object.keys(review).forEach(function (k) {
                    let text;
                    let cell = row.insertCell();
                    text = review[k];
                    cell.appendChild(document.createTextNode(text));
                })
            }
            table.replaceChild(new_tbody, old_tbody);
        }
    };
    http.open("POST", "api/reviews/getAll", true);
    http.send(null);
}

function getPapers() {
    let http = new XMLHttpRequest();
    http.onreadystatechange = function() {
        if (this.readyState === 4 && this.status === 200) {
            let table = document.getElementsByTagName("table")[0];
            let old_tbody = document.getElementsByTagName("tbody")[0];
            let new_tbody = document.createElement('tbody');

            let json = jsonParse(this.responseText);

            for(let i = 0; i < json.length; i++) {
                let paper = json[i];

                let row = new_tbody.insertRow();
                let cell = row.insertCell();
                cell.appendChild(document.createTextNode(paper["title"]));
                cell = row.insertCell();
                cell.appendChild(document.createTextNode(paper["abstract"]));

                cell = row.insertCell();
                let select = document.createElement("select");
                select.id = "select-" + paper["id"];

                let option1 = document.createElement("option");
                option1.text = "Indifferent";
                let option2 = document.createElement("option");
                option2.text = "Review";
                let option3 = document.createElement("option");
                option3.text = "Do not review";

                select.add(option1);
                select.add(option2);
                select.add(option3);

                cell.appendChild(select);
            }
            table.replaceChild(new_tbody, old_tbody);
        }
    };
    http.open("GET", "api/papers/getAll", true);
    http.send(null);
}

function sendBidding() {
    let combobox = document.getElementsByTagName("select");

    let result = [];

    for(let i = 0; i < combobox.length; i++) {
        let id = combobox[i].id.substring(7);
        let choice = combobox[i].value;

        let dict = { id: id,
                    choice: choice};

        result.push(dict);
    }

    let json = JSON.stringify(result);

    let http = new XMLHttpRequest();
    http.open("POST", "api/review/sendBidding", true);
    http.send(json);
}

function getConferences() {
    let http = new XMLHttpRequest();
    http.onreadystatechange = function() {
        if (this.readyState === 4 && this.status === 200) {
            let table = document.getElementsByTagName("table")[0];
            let old_tbody = document.getElementsByTagName("tbody")[0];
            let new_tbody = document.createElement('tbody');

            let json = jsonParse(this.responseText);

            for(let i = 0; i < json.length; i++) {
                let conference = json[i];

                let row = new_tbody.insertRow();
                let cell = row.insertCell();
                cell.appendChild(document.createTextNode(conference["title"]));
                cell = row.insertCell();
                cell.appendChild(document.createTextNode(conference["description"]));
                cell = row.insertCell();
                cell.appendChild(document.createTextNode(conference["deadline-signup"]));
                cell = row.insertCell();
                cell.appendChild(document.createTextNode(conference["price"]));

                let userType = getUserType();

                let button = document.createElement("a");
                button.classList.add("button-link");
                button.innerHTML = "Register";

                switch (userType) {
                    case "listener":
                        button.setAttribute("href", "listener-register.html"); //fixme
                        break;
                    case "speaker":
                        button.setAttribute("href", "speaker-register.html"); //fixme
                        break;
                    case "chair":
                        button.setAttribute("href", "chair-register.html"); //fixme
                        break;
                    default:
                        console.log("Invalid user type");
                }

                cell = row.insertCell();
                cell.appendChild(button);
            }
            table.replaceChild(new_tbody, old_tbody);
        }
    };
    http.open("GET", "api/conference/getAll", true);
    http.send(null);
}

function showAddConferenceButton() {
    let userType = getUserType();

    if(userType === "chair") {
        let button = document.createElement("a");
        button.setAttribute("href", "add-conference.html"); //fixme
        button.classList.add("button-link");
        button.innerHTML = "Add conference";
        button.setAttribute("style", "margin-left: auto; margin-right: auto; margin-top: 25px");

        let container = document.getElementsByClassName("center-container")[0];
        container.appendChild(button);
    }
}

function getUserType() {
    let http = new XMLHttpRequest();
    http.open("GET", "api/user/getUserType", false);
    http.send(null);

    let response = http.responseText;
    let json = jsonParse(response);

    return json["type"];
}