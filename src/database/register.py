from typing import Optional

from tortoise import Tortoise

# Used for automatically initializing and closing tortoise and its models
# To be called in main.py
def register_tortoise(
    app,                                # FastAPI app object
    config: Optional[dict] = None,      # Desired tortoise configuration
    generate_schemas: bool = False,     # Whether to generate schemas in DB. You'll usually want this to be False.
) -> None:
    @app.on_event("startup")
    async def init_orm():
        await Tortoise.init(config=config)
        if generate_schemas:
            await Tortoise.generate_schemas()

    @app.on_event("shutdown")
    async def close_orm():
        await Tortoise.close_connections()