# Chess Moves API

This is a Dockerized Django application that provides an API endpoint for determining the valid moves of a given chess piece on a chessboard.

## Features

- Exposes an API endpoint to retrieve valid moves for a given chess piece.
- Accepts input positions of chess pieces in JSON format.
- Dockerized for easy deployment and portability.

## Prerequisites

- Docker Desktop installed on your Windows machine.
- Python 3.10 or higher installed on your system.

## Installation

1. **Clone the repository** to your local machine:

    ```bash
    git clone https://github.com/ravihere/Chess_Moves.git
    ```

2. **Navigate to the project directory**:

    ```bash
    cd Chess_Moves\chess_moves_api
    ```

3. **Build the Docker image**:

    ```bash
    docker build -t chess_api .
    ```

4. **Run the Docker container**:

    ```bash
    docker run -p 8001:8001 chess_api
    ```

    This command will start the Docker container and map port 8001 of the container to port 8001 on your host machine.

## Usage or Testing in Postman

- Make HTTP POST requests to the API endpoint with the slug representing the chess piece and the position of the chess piece in JSON format.
- Example API endpoint format: `http://0.0.0.0:8001/chess/<slug>`
- Hit `http://0.0.0.0:8001/chess/Rook`
- Example input JSON:

    ```json
    input_data = {
        "positions": {
            "Queen": "A5",
            "Bishop": "G8",
            "Rook": "H5",
            "Knight": "G4"
        }
    }
    ```

- Example output JSON:

    ```json
    {
        "valid_moves": [
            "h8",
            "h1",
            "h3",
            "a5",
            "h4"
        ]
    }
    ```

    The output contains a list of valid moves for the chess piece at the given position.

## Troubleshooting

- If you encounter any issues with Docker or running the application, please refer to the Docker documentation or Docker Desktop troubleshooting resources.
- For any issues specific to the application, check the logs of the Docker container by running `docker logs <container_id_or_name>`.

With the API up and running, you can now integrate it into your chess-related applications or use it for testing and experimentation. Enjoy exploring the world of chess moves with this API!
