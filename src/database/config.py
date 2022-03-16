import os


TORTOISE_ORM = {
    # Get the database connection using the set environment variable
    "connections": {"default": os.environ.get("DATABASE_URL")},
    # Registers all models in models.py and aerich's database migration metadata
    "apps": {
        "models": {
            "models": [
                "src.database.models", "aerich.models"
            ],
            "default_connection": "default"
        }
    }
}