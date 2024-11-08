// Import axios for making HTTP requests
const axios = require('axios');

// The URL of the API (for this case, we'll use the ReqRes API)
const url = 'https://reqres.in/api/users/2'; // Example endpoint that returns user data

// Function to test the API
async function testApi() {
    try {
        // Make a GET request to the URL
        const response = await axios.get(url);
        
        // Log the status code to the console
        console.log('Response Status Code:', response.status);
        
        // Validate if the status code is 200
        if (response.status === 200) {
            console.log('Test Passed: Status code is 200');
        } else {
            console.log('Test Failed: Status code is not 200');
        }
    } catch (error) {
        // Handle any error that occurs during the request
        console.log('Error occurred:', error.message);
    }
}

// Call the function to run the test
testApi();
