# Microservices Deployment with Docker Compose

This project includes two microservices, a server and a client, which are deployed using Docker Compose. The server returns the square root of an integer `n` when a request is received, and the client makes a GET request to the server to retrieve the result and displays it.

## Folder Structure

The project folder structure should be organized as follows:

Assignment2/
|-- docker-compose.yml
|-- server/
| |-- Dockerfile
| |-- requirements.txt
| |-- app/
| | |-- server.py
|-- client/
| |-- Dockerfile
| |-- requirements.txt
| |-- app/
| | |-- client.py
|-- README.txt

- `docker-compose.yml`: Docker Compose file specifying the services to be built and run.
- `server/`: Folder containing the server microservice.
  - `Dockerfile`: Dockerfile specifying how the server container should be built.
  - `requirements.txt`: Requirements file specifying the Python dependencies for the server.
  - `app/`: Folder containing the server code.
    - `server.py`: Python script for the server.
- `client/`: Folder containing the client microservice.
  - `Dockerfile`: Dockerfile specifying how the client container should be built.
  - `requirements.txt`: Requirements file specifying the Python dependencies for the client.
  - `app/`: Folder containing the client code.
    - `client.py`: Python script for the client.
- `README.txt`: This readme file.

## Deployment

To deploy the microservices using Docker Compose, follow these steps:

1. Make sure Docker and Docker Compose are installed on your system.
2. Clone this repository to your local machine.
3. Navigate to the `Assignment2` folder.
4. Run the following command to build and run the client and server containers:
docker-compose up

5. The client and server containers will be built and run. The server will listen on port 5000, and the client will make a GET request to the server to retrieve the square root of `n`.
6. The client will display the result received from the server.

Note: Make sure that no other processes are running on port 5000, as it is the port used by the server in this project.

That's it! You have successfully deployed the microservices using Docker Compose.