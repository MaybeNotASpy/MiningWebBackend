from typing import List

from fastapi import APIRouter, Depends, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError
from tortoise.exceptions import DoesNotExist

import src.crud.images as crud
from src.auth.jwthandler import get_current_user
from src.schemas.images import ImageOutSchema, ImageInSchema, UpdateImage
from src.schemas.token import Status
from src.schemas.users import UserOutSchema


router = APIRouter()


@router.get(
    "/images",
    response_model=List[ImageOutSchema],
    dependencies=[Depends(get_current_user)],
)
async def get_images():
    return await crud.get_images()


@router.get(
    "/image/{image_id}",
    response_model=ImageOutSchema,
    dependencies=[Depends(get_current_user)],
)
async def get_image(image_id: int) -> ImageOutSchema:
    try:
        return await crud.get_image(image_id)
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail="Image does not exist",
        )


@router.post(
    "/images", response_model=ImageOutSchema, dependencies=[Depends(get_current_user)]
)
async def create_image(
    image: ImageInSchema, current_user: UserOutSchema = Depends(get_current_user)
) -> ImageOutSchema:
    return await crud.create_image(image, current_user)


@router.patch(
    "/image/{image_id}",
    dependencies=[Depends(get_current_user)],
    response_model=ImageOutSchema,
    responses={404: {"model": HTTPNotFoundError}},
)
async def update_image(
    image_id: int,
    image: UpdateImage,
    current_user: UserOutSchema = Depends(get_current_user),
) -> ImageOutSchema:
    return await crud.update_image(image_id, image, current_user)


@router.delete(
    "/image/{image_id}",
    response_model=Status,
    responses={404: {"model": HTTPNotFoundError}},
    dependencies=[Depends(get_current_user)],
)
async def delete_image(
    image_id: int, current_user: UserOutSchema = Depends(get_current_user)
):
    return await crud.delete_image(image_id, current_user)