# Task-Manager-API

A lightweight REST API for managing tasks, built to demonstrate backend development skills with FastAPI and MongoDB. Supports full CRUD operations with persistent storage. Can be used as a backend template for any resource management system — tasks, tickets, orders, or any other entity.

## Stack

- **FastAPI** — web framework
- **MongoDB** — database
- **Motor** — async MongoDB driver
- **Docker** — containerization
- **Uvicorn** — ASGI server
- **AWS EC2** — deployment

## Run locally

**1. Start MongoDB:**
```bash
docker-compose up -d
```

**2. Install dependencies:**
```bash
pip install -r requirements.txt
```

**3. Start the server:**
```bash
uvicorn main:app --reload
```

API available at `http://127.0.0.1:8000`

Interactive docs: `http://127.0.0.1:8000/docs`

## Endpoints

| Method | URL | Description |
|--------|-----|-------------|
| GET | /tasks | Get all tasks |
| POST | /tasks | Create a task |
| GET | /tasks/{id} | Get task by ID |
| PUT | /tasks/{id} | Mark task as done |
| DELETE | /tasks/{id} | Delete task |

## Deployment

Deployed on AWS EC2 with systemd for automatic startup on server boot. MongoDB runs in a Docker container alongside the API.

## Notes

This is a demo project without authentication. Not intended for production use.
