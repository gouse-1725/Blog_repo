// You can add any global JavaScript functions here
// For example, to handle API calls that are used across multiple pages

// Function to format date
function formatDate(dateString) {
    const options = { year: 'numeric', month: 'long', day: 'numeric' };
    return new Date(dateString).toLocaleDateString(undefined, options);
}

// Function to handle errors
function handleApiError(error) {
    console.error('API Error:', error);
    alert('An error occurred. Please try again.');
}