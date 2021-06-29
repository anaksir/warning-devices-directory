
function clearTbody(tbody) {
    tbody.innerHTML = null;
};

function createTbodyRow(tbody, data) {
    let keys = ['id', 'name', 'device_type', 'radius', 'coordinates', 'address'];
    let newRow = tbody.insertRow();
    for (let key of keys) {
        let newCell = newRow.insertCell();
        let newText = document.createTextNode(data[key]);
        newCell.appendChild(newText);
    };
};

function convertCoordinates(upperLeftCorner, bottomRightCorner) {
    let upperLeftArr = upperLeftCorner.split(',');
    let bottomRightArr = bottomRightCorner.split(',');
    let coordinateFilterString = 'latitude__lte=' + parseFloat(upperLeftArr[0])
        + '&latitude__gte=' + parseFloat(bottomRightArr[0])
        + '&longitude__gte=' + parseFloat(upperLeftArr[1])
        + '&longitude__lte=' + parseFloat(bottomRightArr[1]);
    return coordinateFilterString
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

    let upperLeftCorner = formData.get('upper_left_corner');
    let bottomRightCorner = formData.get('bottom_right_corner');
    if (upperLeftCorner && bottomRightCorner) {
        let coordinateString = convertCoordinates(upperLeftCorner, bottomRightCorner);
        if (coordinateString) {
            urlElements.push(coordinateString);
        }
    };

    let searchText  = formData.get('search');
    if (searchText) {
        urlElements.push('search=' + searchText);
    };

    let result = url + '?' + urlElements.join('&');
    return result
};

function configNavLink(url, link) {
    if (url) {
        link.classList.remove('link-disabled');
        link.onclick = (event) => {
            event.preventDefault();
            makeTableContent(url);
        };
    } else {
        link.classList.add('link-disabled');
        link.onclick = (event) => {
            Void(0);
        };
    };
};

async function makeTableContent(url) {
    const tableBody = document.querySelector('.table-body');

    clearTbody(tableBody);

    let response = await fetch(url);
    let json = await response.json();

    for (let device of json.results) {
        createTbodyRow(tableBody, device);
    };

    let count = json.count;
    let counterDiv = document.getElementById('devices-counter');
    counterDiv.textContent = `Devices found: ${count}`;

    let nextUrl = json.next;
    let prevUrl = json.previous;
    let nextLink = document.getElementById('link-next');
    let PrevLink = document.getElementById('link-prev');

    configNavLink(nextUrl, nextLink);
    configNavLink(prevUrl, PrevLink);
};

const form = document.forms.filter_form;

form.onsubmit = (event) => {
    event.preventDefault();
    let formData = new FormData(form);
    let url = createFilterUrl(formData);
    makeTableContent(url);
};