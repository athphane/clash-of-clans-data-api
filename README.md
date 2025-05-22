# FastAPI Clash of Clans Data API

This project is a FastAPI application that provides an endpoint to fetch and return bomb statistics from the Clash of Clans wiki in CSV format.

## Project Structure

```
fastapi-clash-of-clans
├── app
│   └── main.py          # FastAPI application code
├── Dockerfile            # Dockerfile for building the application image
├── docker-compose.yml    # Docker Compose configuration
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd fastapi-clash-of-clans
   ```

2. **Build the Docker image:**
   ```bash
   docker build -t fastapi-clash-of-clans .
   ```

3. **Run the application using Docker Compose:**
   ```bash
   docker-compose up
   ```

## Usage

Once the application is running, you can access the endpoint to get bomb statistics in CSV format:

```
GET http://localhost:8000/bomb-stats
```

## Dependencies

This project requires the following Python packages:

- FastAPI
- httpx
- lxml

These dependencies are listed in the `requirements.txt` file and will be installed automatically when building the Docker image.

## License

This project is licensed under the MIT License.