# React + FastAPI To-Do List

This project is a monorepo containing a frontend built with React + TypeScript and a backend built with Python FastAPI. The application uses SQLite as the database, which is located in the `backend/` folder. The application can be run locally for development using Docker Compose, and it can be deployed to production using AWS Copilot.

## Table of Contents
- [Local Development](#local-development)
- [Production Deployment](#production-deployment)

## Local Development

To run the application locally for development, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/victorcesar00/react-python-todo-list
   cd react-python-todo-list
   ```

2. **Build and run the containers**:
   The application uses Docker Compose to manage the development environment. Run the following command to start the frontend and backend services:
   ```bash
   docker-compose up --build
   ```

3. **Access the application**:
   - The frontend will be available at `http://localhost:5173`.
   - The backend API will be available at `http://localhost:8000`.

4. **Development workflow**:
   - The frontend and backend code is mounted as volumes, so any changes you make to the code will be reflected in the running containers without needing to rebuild them.
   - The frontend uses Vite for hot module replacement (HMR), so changes to the frontend code will automatically reload the browser.

5. **Stopping the containers**:
   To stop the containers, run:
   ```bash
   docker-compose down
   ```

## Production Deployment

To deploy the application to production using AWS Copilot, follow these steps:

1. **Install AWS Copilot**:
   If you haven't already installed AWS Copilot, you can do so by following the [official installation guide](https://aws.github.io/copilot-cli/docs/getting-started/install/).

2. **Initialize the application**:
   Run the following command to initialize the application in AWS Copilot:
   ```bash
   copilot app init todo-list
   ```

3. **Deploy the backend service**:
   Deploy the backend service using the following command:
   ```bash
   copilot deploy --name backend
   ```

4. **Deploy the frontend service**:
   Deploy the frontend service using the following command:
   ```bash
   copilot deploy --name frontend
   ```

5. **Access the deployed application**:
   - The frontend will be accessible via the public load balancer URL provided by AWS Copilot.
   - The backend will be accessible internally via the DNS `http://backend.prod.todo-list.internal`.

6. **Remove the backend load balancer rule**:
   By default, AWS Copilot sets a rule on the backend load balancer that only allows requests from the same DNS (`http://backend.prod.todo-list.internal`). To allow the frontend to communicate with the backend, you need to remove this rule in the AWS Management Console.

7. **Scaling and monitoring**:
   - The backend and frontend services are configured to scale based on CPU and memory usage.
   - You can monitor the services using AWS CloudWatch.

## Environment Variables

### Backend
The backend service uses the following environment variables, which are defined in `backend/.env`:
- `DATABASE_URL`: The URL for the SQLite database.
- `HASHING_SECRET_KEY`: The secret key used for hashing.
- `HASHING_ALGORITHM`: The algorithm used for hashing.

### Frontend
The frontend service uses the following environment variable:
- `VITE_BACKEND_BASE_URL`: The base URL for the backend API during development. This is set to `http://backend:8000`.

## Dockerfiles

### Backend
- `Dockerfile.debug`: Used for local development. It includes hot-reloading for faster development.
- `Dockerfile.prod`: Used for production. It optimizes the build for performance and security.

### Frontend
- `Dockerfile.debug`: Used for local development. It includes hot-reloading for faster development.
- `Dockerfile.prod`: Used for production. It builds the React application and serves it using Nginx.

## Nginx Configuration
The frontend uses an Nginx configuration (`frontend/nginx.conf`) to serve the built React application and proxy requests to the backend API.

## Vite Configuration
The frontend uses Vite for development, with a proxy configuration to route API requests to the backend during development.

## AWS Copilot Manifests
The `copilot/` folder contains the manifests for deploying the application to AWS ECS using Copilot:
- `environments/prod/manifest.yml`: Defines the production environment.
- `backend/manifest.yml`: Defines the backend service.
- `frontend/manifest.yml`: Defines the frontend service.

## Conclusion
This application is designed to be easily run locally for development and deployed to production using AWS Copilot. The Docker Compose setup allows for a seamless development experience, while the AWS Copilot setup ensures a smooth deployment process to a production environment.
