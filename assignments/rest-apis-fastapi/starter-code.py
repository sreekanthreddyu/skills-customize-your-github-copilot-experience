# REST APIs with FastAPI - Starter Code
# Assignment: Building REST APIs with FastAPI
#
# Instructions:
# 1. Install dependencies: pip install fastapi uvicorn
# 2. Complete each section marked with TODO
# 3. Run the server with: uvicorn starter-code:app --reload

from fastapi import FastAPI, HTTPException

# TODO: Import BaseModel from pydantic


# TODO: Define a Pydantic model for an Item
# It should have fields: name (str), description (str), price (float)


# Create the FastAPI app instance
app = FastAPI()

# In-memory data store
items = {}
next_id = 1


# TODO: Define a GET / route that returns a welcome message as JSON
# Example response: {"message": "Welcome to the Items API!"}


# TODO: Define a GET /items route that returns all items


# TODO: Define a GET /items/{item_id} route that returns a single item by ID
# - If the item does not exist, raise an HTTPException with status code 404


# TODO: Define a POST /items route that accepts an Item body and adds it to the store
# - Assign a unique integer ID to each new item
# - Return the created item along with its assigned ID
