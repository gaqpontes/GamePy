window.addEventListener('DOMContentLoaded', function () {
    // Set random placeholder text for the input field
    const input = this.document.getElementById('helper_text');
    if (input) {
        input.placeholder = placeholders[Math.floor(Math.random() * placeholders.length)];
    }

    // Set up event listeners for image upload 
    const pictureInput = this.document.getElementById('picture');
    if (pictureInput) {
        pictureInput.addEventListener('change',filePreview);
    }
});

function filePreview(event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function (e) {
            const label = document.querySelector('label[for="picture"]');
            if (label) {
                label.innerHTML = `<div class="gamepy-icon-container gamepy-image-preview rounded-circle"><img src="${e.target.result}" alt="Preview" class="img-fluid"></div>`;
            }
        };
        reader.readAsDataURL(file);
    } else {
        console.error('No file selected or file is invalid.');
    }
}

function handleButton(element, event) {
    console.log('Hello from GamePy.js!');
}

function handleCheckbox(element, event) {
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
        .then(data => {
            console.log('Success:', data);
        })
}

function handleCreate(element, event) {
    event.preventDefault();
    const form = document.getElementById('activity-form');
    const formData = new FormData(form);
    const url = form.action;

    if(formData.get('picture').name == '' || formData.get('helper_text')  == '') {
        alert('Por favor, preencha todos os campos obrigatórios.');
        return;
    }

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

function showSpinner() {
    const spinner = document.getElementById('global-spinner');
    if (spinner) {
        spinner.style.visibility = 'visible';
    }
}

function hideSpinner() {
    const spinner = document.getElementById('global-spinner');
    if (spinner) {
        spinner.style.visibility = 'hidden';
    }
}

const placeholders = [
    'Como arrumo essa bagunça?',
    'Como aprender determinante de matrizes?',
    'Como faço para aprender a tocar violão?',
    'Como faço para aprender a cozinhar?',
    'Como faço para aprender a programar?',
    'Como faço para aprender a desenhar?']