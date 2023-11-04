# FastAPI To-Do App

This is a FastAPI application that provides a simple To-Do list API using SQL Server as the database backend. It allows you to create, read, update, and delete tasks.

## Prerequisites

- Ubuntu Server (or a similar Linux distribution)
- Python 3.x
- pip (Python package manager)
- ODBC Driver 18 for SQL Server

## Installation

1. Install Python and pip if not already installed:

   ```shell
   sudo apt update
   sudo apt install python3 python3-pip
   ```

2. Install ODBC Driver 18 for SQL Server:

   Follow the official documentation to install the ODBC Driver for SQL Server on your Ubuntu server: [ODBC Driver on Linux](https://docs.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server)

3. Clone the repository:

   ```shell
   git clone <repository_url>
   cd <repository_directory>
   ```

4. Install the required Python packages:

   ```shell
   pip install -r requirements.txt
   ```

## Configuration

Edit the `main.py` file and set your SQL Server connection string in the `connection_string` variable:

```python
connection_string = "Driver={ODBC Driver 18 for SQL Server};Server=tcp:devopsinsidersdbs.database.windows.net,1433;Database=todoapp;UID=devopsadmin;PWD=P@ssw01rd@123;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30"
```

Make sure to replace the connection string with your SQL Server details.

## Usage

Run the FastAPI application:

   ```shell
   uvicorn app:app --host 0.0.0.0 --port 8000
   ```

The API will be available at `http://your_server_ip:8000`.

## API Endpoints

- `GET /tasks`: List all tasks.
- `GET /tasks/{task_id}`: Retrieve a single task by ID.
- `POST /tasks`: Create a new task.
- `PUT /tasks/{task_id}`: Update an existing task by ID.
- `DELETE /tasks/{task_id}`: Delete a task by ID.

## CORS Configuration

By default, the application is configured to allow all origins. In a production environment, you should specify the allowed origins explicitly in the CORS middleware configuration in the `main.py` file.

