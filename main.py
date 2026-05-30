from fastapi import  FastAPI
from fastapi import HTTPException
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()
Instrumentator().instrument(app).expose(app)

client = AsyncIOMotorClient("mongodb://mongo:27017")
db = client.taskdb
collection = db.tasks

class Task(BaseModel):
    title: str
    done: bool = False

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/tasks")
async def create_task(task: Task):
    task_dict = task.model_dump()
    result = await collection.insert_one(task_dict)
    task_dict["_id"] = str (result.inserted_id)
    return task_dict

@app.get("/tasks")
async def get_tasks():
    tasks_list = []
    async for task in collection.find():
        task["_id"] = str(task["_id"])
        tasks_list.append(task)
    return {"tasks": tasks_list}

@app.get("/tasks/{task_id}")
async def get_task(task_id: str):
    task = await collection.find_one({"_id": ObjectId(task_id)})
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    task["_id"] = str(task["_id"])
    return task


@app.put("/tasks/{task_id}")
async def update_task(task_id: str):
    result = await collection.update_one(
    {"_id": ObjectId(task_id)},
    {"$set": {"done": True}}
    )
    task = await collection.find_one({"_id": ObjectId(task_id)})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Task not found")
    task["_id"] = str(task["_id"])
    return task


@app.delete("/tasks/{task_id}")
async def delete_task(task_id: str):
    task = await collection.delete_one({"_id": ObjectId(task_id)})
    if task.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted"}

