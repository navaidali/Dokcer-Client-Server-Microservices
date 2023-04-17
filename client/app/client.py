import requests

# Send GET request to server
response = requests.get("http://localhost:5000")

# Check if the request was successful
if response.status_code == 200:
    # Print the response message
    print("Message received from server:", response.text)
else:
    # Print an error message
    print("Failed to receive message from server:", response.status_code)
