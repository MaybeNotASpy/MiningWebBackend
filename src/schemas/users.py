from tortoise.contrib.pydantic import pydantic_model_creator

from src.database.models import Users

# For the creation of new users
UserInSchema = pydantic_model_creator(
    Users, name="UserIn", exclude_readonly=True
)

# For unsecured user retrieval (external requests)
# Explicitly excludes the password for security reasons
UserOutSchema = pydantic_model_creator(
    Users, name="UserOut", exclude=["password", "created_at", "modified_at"]
)

# For secured user retrieval (internal requests)
UserDatabaseSchema = pydantic_model_creator(
    Users, name="User", exclude=["created_at", "modified_at"]
)