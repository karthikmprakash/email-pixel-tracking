# Email Pixel Tracking

This project is an email pixel tracking application built with FastAPI. It tracks email opens using a 1x1 transparent pixel and stores the tracking data in an SQLite database.

## Features

- Track email opens using a 1x1 transparent pixel
- Store tracking data in an SQLite database
- Fetch tracking counts for each email ID
- Docker support for easy deployment

## Requirements

- Python 3.10
- FastAPI
- SQLAlchemy
- Uvicorn

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/email-pixel-tracking.git
    cd email-pixel-tracking
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file with the following content:
    ```env
    SMTP_EMAIL="your_email@example.com"
    SMTP_SERVER="smtp.example.com"
    SMTP_PASSWORD="your_smtp_password"
    RECEIVER_EMAIL="receiver_email@example.com"
    ```

5. Run the FastAPI application:
    ```bash
    uvicorn app.main:app --reload
    ```

6. Send a test email:
    ```bash
    python tests/test_email_client.py
    ```

## Running with Docker

1. Build the Docker image:
    ```bash
    docker build -t email-pixel-tracking .
    ```

2. Run the Docker container:
    ```bash
    docker run -d -p 8000:8000 email-pixel-tracking
    ```

## Endpoints

- `GET /track/{email_id}`: Track email opens by email ID.
- `GET /track_counts`: Fetch tracking counts for each email ID.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## Contact

For any inquiries, please contact [Karthik M Prakash](mailto:karthik@akaiketech.com).