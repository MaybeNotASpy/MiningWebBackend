from tortoise import Tortoise
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.database.register import register_tortoise
from src.database.config import TORTOISE_ORM 

"""
Global Setups
"""
Tortoise.init_models(      # Allows serializers to read model relationships
    [
        "src.database.models"
    ], 
    "models")

app = FastAPI()             # Initialize FastAPI

app.add_middleware(         # Necessary for cross-origin requests
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


"""
Router Setup
"""
# This MUST come after Tortoise.init_models since this triggers pydantic setup.
# Tortoise-ORM must be initialized before pydantic.
from src.routes import users, images

app.include_router(users.router)        # Setup HTTP requests involving users
app.include_router(images.router)       # '' '' for images


"""
Event Registrations
"""
# Handles the tortoise-orm models and database connection
register_tortoise(app, config=TORTOISE_ORM, generate_schemas=False)


"""
GET paths
"""
@app.get("/")
def home():
    return "Hello, World!"