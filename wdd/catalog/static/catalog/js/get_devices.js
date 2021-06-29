function createTbodyRow(tbody, data) {
    let keys = ['name', 'device_type', 'radius', 'coordinates'];
    let newRow = tbody.insertRow();
    for (let key of keys) {
        let newCell = newRow.insertCell();
        let newText = document.createTextNode(data[key]);
        newCell.appendChild(newText);
    };
};

function createFilterUrl(formData) {
    const url = '/api/devices/';
    let urlElements = [];
    let deviceType = formData.get('device_type');
    if (deviceType) {
        urlElements.push('device_type='+ deviceType);
    };

    let maxRadius = formData.get('max_radius');
    if (maxRadius) {
        urlElements.push('radius__lte=' + maxRadius);
    };
    let minRadius = formData.get('min_radius');
    if (minRadius) {
        urlElements.push('radius__gte=' + minRadius);
    };
    let result = url + '?' + urlElements.join('&');
    return result
}

function clearTbody(tbody) {
    tbody.innerHTML = null;
};

function showPDeviceCount(count) {
    let p = document.getElementById('total-count');
    p.textContent = `Total Device count: ${count}`;
}

// function configNavLinks(next, prev) {
//     let nextLink = document.getElementById('link-next');
//     let prevLink = document.getElementById('link-prev');
//     if (next) {
//         nextLink.addEventListener('click', makeTableContent, false);
//     };

// };

async function nextLinkHandler(enent, url) {
    clearTbody(tableBody);
    let nextresponse = await fetch(url);
    let nextjson = await nextresponse.json();
    for (let device of nextjson.results) {
        createTbodyRow(tableBody, device);
    };
    let nexturl2 = nextjson.next;

};

async function makeTableContent(evnt) {
    evnt.preventDefault();
    clearTbody(tableBody);
    let formData = new FormData(form);
    let url = createFilterUrl(formData);

    let response = await fetch(url);
    let json = await response.json();
    showPDeviceCount(json.count);

    for (let device of json.results) {
        createTbodyRow(tableBody, device);
    };
    if (json.previous) {
        let prevLink = document.getElementById('link-prev');
        prevLink.classList.remove('link-isabled');
    };
    let nextUrl = json.next;
    if (nextUrl) {
        let linkHandler = async (enent, url) => {
            clearTbody(tableBody);
            let nextresponse = await fetch(url);
            let nextjson = await nextresponse.json();
            for (let device of nextjson.results) {
                createTbodyRow(tableBody, device);
            };
            let nxtUrl = nextjson.next;
            let nextLink = document.getElementById('link-next');
            nextLink.onclick = (envt) => linkHandler(envt, nxtUrl);
        };
        let nextLink = document.getElementById('link-next');
        nextLink.classList.remove('link-isabled');
        nextLink.onclick = (envt) => linkHandler(envt, nextUrl);
    } else {
        nextLink.classList.add('link-isabled');
    };

};

let form = document.forms.filter_form;
let tableBody = document.querySelector('.table-body');

form.onsubmit = makeTableContent;

// let prevLink = document.getElementById('link-prev');
// prevLink.classList.remove('link-isabled');
// prevLink.onclick = () => {
//     alert('click!!!');
// };