# NerdHosting API

This is the backend API for NerdHosting, built with [FastAPI](https://fastapi.tiangolo.com/) and [SQLModel](https://sqlmodel.tiangolo.com/).

## Features

- **FastAPI**: High-performance web framework.
- **SQLModel**: Database interaction using Python type hints (SQLAlchemy + Pydantic).
- **MySQL**: Relational database storage.
- **WebSockets**: Real-time communication support.

## Prerequisites

- Python 3.10+
- MySQL Server
- [uv](https://github.com/astral-sh/uv) (Recommended for dependency management)

## Installation

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd nerdhosting-api
   ```

2. **Install dependencies:**

   Since this project uses `uv`, you can sync the environment directly:

   ```bash
   uv sync
   ```

## Configuration

Create a `.env` file in the root directory to configure the database connection. The application expects the following variables:

```env
MYSQL_USER=root
MYSQL_PASSWORD=secret
MYSQL_URL=localhost
MYSQL_PORT=3306
MYSQL_DATABASE=nerdhosting
```

## Running the Application

Start the development server:

```bash
fastapi dev main.py
```

The API will be available at `http://127.0.0.1:8000`.

## Project Structure

- `main.py`: Application entry point and lifespan management.
- `utils/database.py`: Database engine configuration and session dependency.
- `routers/`: Contains API route definitions (e.g., websockets).
- `dependencies.py`: Custom API dependencies (e.g., token verification).
