console.log("script!");

const url = '/api/devices/';

let tableBody = document.querySelector('.table-body');

function configNavLinks(data) {
    let linkNext = document.getElementById('link-next');
    let linkPrev = document.getElementById('link-prev');
    let urlPrev = data.previous 
    if (urlPrev === null) {
        linkPrev.style.display = 'none';
    } else {
        linkPrev.onclick = function(event) {
            event.preventDefault();
            getDevices(urlPrev).then(data => {
                for (let deviceData of data.results){
                    createTableContent(tableBody, deviceData);
                }
            });
        };
    };
    let urlNext = data.next;
    if (urlNext === null) {
        linkPrev.style.display = 'none'
    } else {
        linkNext.onclick = function(event) {
            event.preventDefault();
            getDevices(urlNext).then(data => {
                for (let deviceData of data.results){
                    createTableContent(tableBody, deviceData);
                }
            });
        };
    };
};

function createTbodyRow(tbody, data) {
    let keys = ['name', 'device_type', 'radius'];
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
    console.log(result);
    return result
}

function clearTbody(tbody) {
    tbody.innerHTML = null;
};

function showPDeviceCount(count) {
    let p = document.getElementById('total-count');
    p.textContent = `Total Device count: ${count}`;
}

let form = document.forms.filter_form;

form.onsubmit = async (evnt) => {
    evnt.preventDefault();
    clearTbody(tableBody);
    let formData = new FormData(form)
    let url = createFilterUrl(formData)
    let response = await fetch(url);
    let json = await response.json();
    showPDeviceCount(json.count);
    for (let device of json.results) {
        createTbodyRow(tableBody, device);
    };
};