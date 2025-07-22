function handleButton(element, event){
    console.log('Hello from GamePy.js!');
}

function handleCreate(element, event){
    event.preventDefault();
    const form = document.getElementById('activity-form');
    const formData = new FormData(form);
    const url = form.action;
    
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
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}