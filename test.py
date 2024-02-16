import requests

def get_balances_from_flask_api():
    # Define the URL of the Flask API endpoint
    url = 'http://127.0.0.1:5000/balances'  # Update this URL if your Flask app is hosted elsewhere

    # Make a GET request to the Flask API endpoint
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Return the JSON response content
        return response.json()
    else:
        # Print an error message if the request was not successful
        print(f"Error: {response.status_code}, {response.text}")
        return None

# Call the function to get balances from the Flask API
balances = get_balances_from_flask_api()

# Print the balances if they are available
if balances:
    print("Available Balance:", balances.get('available_balance'))
