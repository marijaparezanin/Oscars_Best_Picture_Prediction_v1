// Example: Fetch data from CSV with a different file path
const fetchMovieData = async () => {
    const response = await fetch('/static/files/oscardata.csv'); // Update the file path here

    const data = await response.text();
    return data;
};

// Example: Load posters when the page is ready with a different CSV file
document.addEventListener('DOMContentLoaded', async () => {
    const csvData = await fetchMovieData();
    const movies = parseCSV(csvData);
    populatePosters(movies);
});
