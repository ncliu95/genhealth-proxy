# FastAPI Reverse Proxy for GenHealth API

This project provides a reverse proxy built with FastAPI to forward requests to the GenHealth API. It includes features like request validation, HTTPS support, and rate limiting to ensure secure and fair use.

## Prerequisites

- Docker and Docker Compose installed on your machine. Ensure you have the latest versions to avoid compatibility issues.

## Configuration

Create a `.env` file in the root directory of the project and add the following environment variable:

```bash
GENHEALTH_BASE_API_URL=https://api.genhealth.ai
```


This variable is essential for the application to correctly forward requests to the GenHealth API.

## Running the Application with Docker Compose

1. **Start the Application**

   Navigate to the project root directory and run:

```bash
docker-compose up -d
```

This command builds and starts the FastAPI application container in detached mode.

2. **Accessing the Application**

The application is accessible at `http://localhost:80`. You can also visit `http://localhost:80/docs` in your web browser to access the API documentation and test endpoints.

## Application Endpoint

The reverse proxy provides a single endpoint for the purpose of the assessment:

- `/v1/predict`: Forwards requests to the GenHealth API. This endpoint is rate-limited to 5 requests per minute to ensure fair usage, and requires the user to provide their GenHealth authorization token. The token will be forwarded to GenHealth's API.

    This endpoint has request body validation based entirely on GenHealth's `/predict` endpoint's request body. 

## Rate Limiting

Please note that the `/v1/predict` endpoint is rate-limited to 5 requests per minute. If the rate limit is exceeded, the service will respond with a `429 Too Many Requests` status code.

## Stopping the Application

To stop and remove the application containers, use the following command from the project root directory:

```bash
docker-compose down
```

## Additional Discussion

I have included a sample `deployment.yaml` and `service.yaml` with the intention of showing consideration for scaling. The idea is to have multiple replica containers, with a load balancer in front for highly scalable usage.

In terms of security, ideally this endpoint would be served behind Nginx with an SSL certificate. However, I do not have any valid SSL certificates currently, so I do not feel comfortable adding Nginx into the build without validating the work.

Finally, for HIPAA and security concerns in production environment, this service should be deployed in a CSP that guarantees HIPAA compliance.