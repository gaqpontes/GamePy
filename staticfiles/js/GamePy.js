function handleButton(element, event){
    console.log('Hello from GamePy.js!');
}

function handleCheckbox(element, event){
    fetch('/objectives/' + element.dataset.uuid, 
        {
            headers: {
            'X-CSRFToken': window.csrftoken
            },
            method: 'POST',
            body: JSON.stringify({
                'completed': element.checked
            }),
        })
        .then(response => response.json())
        .then( data => {
            console.log('Success:', data);
    })
}

function handleCreate(element, event){
    event.preventDefault();
    const form = document.getElementById('activity-form');
    const formData = new FormData(form);
    const url = form.action;
    showSpinner();
    fetch(url, {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': window.csrftoken
        }
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        form.reset();
        window.location.reload();
    })
    .catch((error) => {
        console.error('Error:', error);
    })
    .finally(() => {
        hideSpinner()
    });
}

function showSpinner(){
    const spinner = document.getElementById('global-spinner');
    if (spinner) {
        spinner.style.visibility = 'visible';
    }
}
function hideSpinner(){
    const spinner = document.getElementById('global-spinner');
    if (spinner) {
        spinner.style.visibility = 'hidden';
    }
}