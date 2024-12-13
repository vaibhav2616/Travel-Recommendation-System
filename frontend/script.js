const API_KEY = "YOUR_GOOGLE_API_KEY"; // Replace with your actual Google Maps API key

// Function to fetch coordinates for the start and end locations
async function fetchCoordinates(location) {
    const url = `https://maps.googleapis.com/maps/api/geocode/json?address=${encodeURIComponent(location)}&key=${API_KEY}`;
    const response = await fetch(url);
    const data = await response.json();
    if (data.status === "OK") {
        return data.results[0].geometry.location;
    } else {
        throw new Error("Location not found.");
    }
}

// Function to process the user's trip details
async function generatePlan(event) {
    event.preventDefault(); // Prevent page refresh on form submit

    const startLocation = document.getElementById("startLocation").value;
    const endLocation = document.getElementById("endLocation").value;
    const startDate = document.getElementById("startDate").value;
    const endDate = document.getElementById("endDate").value;
    const days = document.getElementById("days").value;

    if (!startLocation || !endLocation || !startDate || !endDate || !days) {
        alert("Please fill in all fields.");
        return;
    }

    try {
        const startCoords = await fetchCoordinates(startLocation);
        const endCoords = await fetchCoordinates(endLocation);

        // Output the user's trip details
        const output = document.getElementById("output");
        output.innerHTML = `
            <h2>Your Trip Plan</h2>
            <p><strong>Start Location:</strong> ${startLocation} (Lat: ${startCoords.lat}, Lng: ${startCoords.lng})</p>
            <p><strong>End Location:</strong> ${endLocation} (Lat: ${endCoords.lat}, Lng: ${endCoords.lng})</p>
            <p><strong>Start Date:</strong> ${startDate}</p>
            <p><strong>End Date:</strong> ${endDate}</p>
            <p><strong>Number of Days:</strong> ${days}</p>
        `;

        // Add additional features like routes, weather, hotels, restaurants based on the input here
        // Example: you could fetch weather data, nearby hotels, etc. based on coordinates

    } catch (error) {
        alert("Error: " + error.message);
    }
}

// Add event listener to form
document.getElementById("travelForm").addEventListener("submit", generatePlan);
