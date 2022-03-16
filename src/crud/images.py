from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist

from src.database.models import Images
from src.schemas.token import Status
from src.schemas.images import ImageOutSchema

"""
Create
"""
# Creates an image entry in the DB and returns a pydantic image model.
async def create_image(image, current_user) -> ImageOutSchema:
    # Decompose the image object into a dictionary
    image_dict = image.dict(exclude_unset=True)
    # Set the author to be the current user
    image_dict["author_id"] = current_user.id
    # Asynchronously creates a new tortoise Images object from the dictionary
    # and registers it in the DB.
    image_obj = await Images.create(**image_dict)
    # Returns a pydantic object from the created tortoise object
    return await ImageOutSchema.from_tortoise_orm(image_obj)


"""
Retrieve
"""
# Retrieves all images from the DB.
async def get_notes() -> ImageOutSchema:
    return await ImageOutSchema.from_queryset(Images.all())

# Retrieves a specific image from the DB.
async def get_note(image_id: int) -> ImageOutSchema:
    return await ImageOutSchema.from_queryset_single(Images.get(id=image_id))


"""
Update
"""
# Updates an image in the DB IF the current user created it.
async def update_image(image_id: int, image, current_user) -> ImageOutSchema:
    try:
        db_image = await ImageOutSchema.from_queryset_single(Images.get(id=image_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Image {image_id} not found")

    if db_image.author.id == current_user.id:
        await Images.filter(id=image_id).update(**image.dict(exclude_unset=True))
        return await ImageOutSchema.from_queryset_single(Images.get(id=image_id))

    raise HTTPException(status_code=403, detail=f"Not authorized to update")


"""
Delete
"""
# Deletes an image in the DB IF it exists AND the current user created it.
async def delete_image(image_id: int, current_user) -> Status:
    try:
        db_image = await ImageOutSchema.from_queryset_single(Images.get(id=image_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Image {image_id} not found")

    if db_image.author.id == current_user.id:
        deleted_count = await Images.filter(id=image_id).delete()
        if not deleted_count:
            raise HTTPException(status_code=404, detail=f"Image {image_id} not found")
        return Status(message=f"Deleted image {image_id}")

    raise HTTPException(status_code=403, detail=f"Not authorized to delete")