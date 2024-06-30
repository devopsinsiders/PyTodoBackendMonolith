# Running the Python Application on Azure VM

This guide will walk you through the process running a Python application using FastAPI, which interacts with a Microsoft SQL Server database using PyODBC.

## Prerequisites

Before getting started, make sure you have the following prerequisites installed on your system:
-  source_image_reference = {
      publisher = "Canonical"
      offer     = "0001-com-ubuntu-server-focal"
      sku       = "20_04-lts"
      version   = "latest"
    }
- Python
- pip

## Step 1: Clone the Repository

Clone the application's source code from your version control system or download it as a zip archive and extract it to your local machine.

```bash
git clone <repository_url>
cd <repository_directory>
```

## Step 2: Update Connection String

Edit the `app.py` file to update the `connection_string` variable with the appropriate connection details for your SQL Server database. Update ODBC Version to 17

## Step 3: Run Below Commands to make the application running

To Run the Application, open a terminal, navigate to the project directory, and run the following command:

```bash

sudo su
apt-get update && apt-get install -y unixodbc unixodbc-dev
curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list
apt-get update
ACCEPT_EULA=Y apt-get install -y msodbcsql17
pip install -r requirements.txt
uvicorn app:app --host 0.0.0.0 --port 8000
```

## Step 4: Access the Application

Your Python application is now running. You can access it by opening a web browser or sending HTTP requests to `http://localhost:8000` or by using VM's Public IP.

## API Endpoints

- `/api/tasks`: List all tasks (GET)
- `/api/tasks/{task_id}`: Retrieve a single task by ID (GET)
- `/api/tasks`: Create a new task (POST)
- `/api/tasks/{task_id}`: Update an existing task by ID (PUT)
- `/api/tasks/{task_id}`: Delete a task by ID (DELETE)

## Conclusion

You've successfully run a Python application. Feel free to make changes to the application and deploy it to your preferred environment.
