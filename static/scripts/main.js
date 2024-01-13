var selectedPosters = [];

function handlePosterClick(poster, movieName) {
    if (!poster.classList.contains('selected') && selectedPosters.length < 3) {
        poster.classList.add('selected');
        selectedPosters.push({ poster, movieName });
    } else if (poster.classList.contains('selected')) {
        poster.classList.remove('selected');
        selectedPosters = selectedPosters.filter(p => p.poster !== poster);
    }
}
async function calculateResults() {
    console.log(selectedPosters);

    if (selectedPosters.length === 3) {
        try {
            const response = await fetch('/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ selectedPosters }),
            });

            if (response.ok) {
                const result = await response.json();
                // Handle the result as needed
                console.log(result);
                // Display the result in a popup
                alert(result.message);
            } else {
                console.error('Server response not okay');
            }
        } catch (error) {
            console.error('Error while fetching data:', error);
        }
    } else {
        console.log('Please select exactly 3 posters.');
    }

    return false;
}
