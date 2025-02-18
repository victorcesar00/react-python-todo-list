# React + FastAPI To-Do List

This project is a simple To-Do List application with a **React + TypeScript frontend** and a **Python FastAPI backend**, along with a **SQLite database**. It uses Docker and Docker Compose for easy setup and deployment.

---

## Features

- **Pre-registered Users**: There are three users registered in the database:
  - `joao_bosco` / `12345`
  - `victor_cesar` / `abcde`
  - `wenderson` / `98765`

---

## Prerequisites

Before you begin, ensure you have the following installed:

- **Docker**: [Install Docker](https://docs.docker.com/get-docker/)
- **Docker Compose**: [Install Docker Compose](https://docs.docker.com/compose/install/)

---

## Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/victorcesar00/react-python-todo-list.git
   cd react-python-todo-list
   ```

2. **Build and run the project**:
   ```bash
   docker-compose up --build
   ```

   This will:
   - Build the Docker images for the backend and frontend.
   - Start the containers and link them together.

3. **Access the services**:
   - **Backend (FastAPI)**: Available at `http://localhost:8000`
   - **Frontend (React)**: Available at `http://localhost:5173`

4. **Stop the services**:
   ```bash
   docker-compose down
   ```

5. **Clean up (optional)**:
   To remove containers and volumes, run:
   ```bash
   docker-compose down -v
   ```

---

## Platform-Specific Notes

### **Windows**
- Ensure **WSL 2 (Windows Subsystem for Linux)** is installed and enabled. Docker Desktop uses WSL 2 for better performance.
- File permissions in volumes might differ. If you encounter permission issues, adjust permissions in WSL or Docker settings.
- Use **PowerShell** or **Windows Terminal** for running Docker commands.

### **Linux**
- Docker runs natively on Linux, so no additional setup is required.
- Ensure your user is added to the `docker` group to run Docker commands without `sudo`:
  ```bash
  sudo usermod -aG docker $USER
  ```
- File permissions in volumes should work as expected.

### **macOS**
- Docker runs natively on macOS, but ensure Docker Desktop is installed and running.
- File permissions in volumes should work as expected.
- Use **Terminal** or **iTerm2** for running Docker commands.

---

## Environment Variables

### Backend
- `DATABASE_URL`: The database connection URL. Defaults to `sqlite:///./todo.db`.

### Frontend
- `NODE_ENV`: The environment in which the frontend is running. Set to `development`.
- `VITE_BACKEND_BASE_URL`: The base URL for the backend API. Set to `http://backend:8000`.

---

## Volumes

- **Backend**:
  - `./backend/src:/app/src`: Maps the local `backend/src` directory to the `/app/src` directory in the container.
- **Frontend**:
  - `./frontend/src:/app/src`: Maps the local `frontend/src` directory to the `/app/src` directory in the container.

---

## Troubleshooting

- **Port Conflicts**: If ports `8000` or `5173` are already in use, update the `ports` section in `docker-compose.yml`.
- **Build Issues**: Ensure all dependencies are correctly specified in `requirements.txt` (backend) and `package.json` (frontend).
- **Permission Issues**: On Windows, ensure WSL 2 is properly configured. On Linux/macOS, ensure your user has the correct permissions.

