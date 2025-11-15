import pyodbc
import uvicorn
import os
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# connection_string = os.getenv("CONNECTION_STRING")
connection_string = "UPDATE CONNECTION STRING HERE"

app = FastAPI()

# Configure CORSMiddleware to allow all origins (disable CORS for development)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # This allows all origins (use '*' for development only)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the Task model
class Task(BaseModel):
    title: str
    description: str

# Create a table for tasks (You can run this once outside of the app)
@app.get("/api")
def create_tasks_table():
    try:
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE Tasks (
                ID int NOT NULL PRIMARY KEY IDENTITY,
                Title varchar(255),
                Description text
            );
        """)
        conn.commit()        
    except Exception as e:
        print(e)
    return "Table Created... Tasks API Ready"

# List all tasks
@app.get("/api/tasks")
def get_tasks():
    tasks = []
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Tasks")
        for row in cursor.fetchall():
            task = {
                "ID": row.ID,
                "Title": row.Title,
                "Description": row.Description
            }
            tasks.append(task)
    return tasks

# Retrieve a single task by ID
@app.get("/api/tasks/{task_id}")
def get_task(task_id: int):
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Tasks WHERE ID = ?", task_id)
        row = cursor.fetchone()
        if row:
            task = {
                "ID": row.ID,
                "Title": row.Title,
                "Description": row.Description
            }
            return task
        return {"message": "Task not found"}

# Create a new task
@app.post("/api/tasks")
def create_task(task: Task):
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Tasks (Title, Description) VALUES (?, ?)", task.title, task.description)
        conn.commit()
    return task

# Update an existing task by ID
@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE Tasks SET Title = ?, Description = ? WHERE ID = ?", updated_task.title, updated_task.description, task_id)
        conn.commit()
        return {"message": "Task updated"}

# Delete a task by ID
@app.delete("/api/tasks/{task_id}")
def delete_task(task_id: int):
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Tasks WHERE ID = ?", task_id)
        conn.commit()
        return {"message": "Task deleted"}

if __name__ == "__main__":
    create_tasks_table()
    uvicorn.run(app, host="0.0.0.0", port=8000)
