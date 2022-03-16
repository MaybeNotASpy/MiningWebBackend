from typing import Optional

from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from src.database.models import Images

# For creating new images
ImageInSchema = pydantic_model_creator(
    Images, name="NoteIn", exclude=["author_id"], exclude_readonly=True)

# For retrieving images
ImageOutSchema = pydantic_model_creator(
    Images, name="Note", exclude =[
      "modified_at", "author.password", "author.created_at", "author.modified_at"
    ]
)

# For updating images
class UpdateImage(BaseModel):
    title: Optional[str]
    content: Optional[str]