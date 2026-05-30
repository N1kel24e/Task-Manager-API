# Task-Manager-API

A lightweight REST API for managing tasks, built to demonstrate backend development skills with FastAPI and MongoDB. Supports full CRUD operations with persistent storage. Can be used as a backend template for any resource management system — tasks, tickets, orders, or any other entity.

## Stack

- **FastAPI** — web framework
- **MongoDB** — database
- **Motor** — async MongoDB driver
- **Docker / Docker Compose** — containerization
- **Uvicorn** — ASGI server
- **Prometheus** — metrics collection
- **Grafana** — metrics visualization
- **AWS EC2** — deployment

## Run locally

Start all services (API + MongoDB + Prometheus + Grafana):

```bash
docker-compose up --build
```

| Service    | URL                          |
|------------|------------------------------|
| API        | http://localhost:8000        |
| API Docs   | http://localhost:8000/docs   |
| Metrics    | http://localhost:8000/metrics|
| Prometheus | http://localhost:9090        |
| Grafana    | http://localhost:3000        |

## Endpoints

| Method | URL            | Description       |
|--------|----------------|-------------------|
| GET    | /tasks         | Get all tasks     |
| POST   | /tasks         | Create a task     |
| GET    | /tasks/{id}    | Get task by ID    |
| PUT    | /tasks/{id}    | Mark task as done |
| DELETE | /tasks/{id}    | Delete task       |

## Deployment

Deployed on AWS EC2 with systemd for automatic startup on server boot. MongoDB runs in a Docker container alongside the API.

## Notes

This is a demo project without authentication. Not intended for production use.
