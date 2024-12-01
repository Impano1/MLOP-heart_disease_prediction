document.getElementById('prediction-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const data = Object.fromEntries(formData.entries());
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        document.getElementById('prediction-result').innerText = `Prediction: ${result.prediction}`;
    });
});

document.getElementById('retrain-button').addEventListener('click', function() {
    fetch('/retrain', {
        method: 'POST'
    })
    .then(response => response.json())
    .then(result => {
        alert(result.message);
    });
});