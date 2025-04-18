# api_on_cloud_run_template

# Demo Status API

A simple FastAPI app with CI/CD pipeline to Google Cloud Run.

## Features
- `/health` GET endpoint
- `/echo` POST endpoint
- Dockerized
- GitHub Actions CI/CD
- Pre-commit checks
- Unit tests with `pytest`

## Run Locally
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Run with Docker
```bash
docker build -t demo-status-api .
docker run -p 8080:8080 demo-status-api
```

## Run Tests
```bash
pytest
```

## Setup Pre-commit
```bash
pip install pre-commit
pre-commit install
```

## CI/CD Setup
### GitHub Secrets
Add these in your repo:
- `GCP_SA_KEY`: Service Account JSON (as a single line)
- `GCP_PROJECT_ID`: Your GCP project ID

On every push to `main`, the pipeline:
- Runs formatting/lint checks
- Runs tests
- Builds & pushes Docker image
- Deploys to Cloud Run

## Endpoints
- `GET /health`
- `POST /echo`


gcloud projects describe tenacious-camp-357012 --format="value(projectNumber)"
