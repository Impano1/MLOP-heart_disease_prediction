document.getElementById('prediction-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const data = Object.fromEntries(formData.entries());
    console.log('Form Data:', data); 
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        console.log('Prediction Result:', result); 
        document.getElementById('prediction-result').innerText = `Prediction: ${result.prediction}`;
    })
    .catch(error => console.error('Error:', error)); 
});

document.getElementById('retrain-button').addEventListener('click', function() {
    console.log('Retrain button clicked'); 
    fetch('/retrain', {
        method: 'POST'
    })
    .then(response => response.json())
    .then(result => {
        console.log('Retrain Result:', result); 
        alert(result.message);
    })
    .catch(error => console.error('Error:', error)); 
});