# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a simple REST API using the FastAPI framework. You will learn how to define routes, handle HTTP methods, work with request and response data, and run a local API server.

## 📝 Tasks

### 🛠️ Set Up a FastAPI Application

#### Description
Install FastAPI and create a basic application with a root endpoint that returns a welcome message.

#### Requirements
Completed program should:

- Install `fastapi` and `uvicorn` using pip
- Create a FastAPI app instance
- Define a `GET /` route that returns a JSON welcome message
- Run the server locally using `uvicorn`

### 🛠️ Build a Items API

#### Description
Add endpoints to create, read, and list items using an in-memory data store (a Python dictionary or list).

#### Requirements
Completed program should:

- Define a `GET /items` route that returns all items
- Define a `GET /items/{item_id}` route that returns a single item by ID
- Define a `POST /items` route that accepts JSON data and adds a new item
- Return appropriate HTTP status codes (e.g., 404 when an item is not found)

### 🛠️ Add Input Validation with Pydantic

#### Description
Use Pydantic models to validate and structure the data coming into your API.

#### Requirements
Completed program should:

- Define a Pydantic `BaseModel` for the item data (e.g., name, description, price)
- Use the model as the request body type for the `POST /items` route
- Return a meaningful error response when required fields are missing or invalid
