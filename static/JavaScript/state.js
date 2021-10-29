let user_state_select = document.getElementById('user_state');
async function getStates() {
    const jsondata = await fetch('https://cdn-api.co-vin.in/api/v2/admin/location/states');
    const jsdata = await jsondata.json();
    jsdata.states.forEach(elem => {
        let option_to_create = document.createElement('option');
        let state = elem['state_name'];
        option_to_create.setAttribute('value', state);
        option_to_create.innerHTML = state;
        user_state_select.appendChild(option_to_create);
    });
}

getStates();