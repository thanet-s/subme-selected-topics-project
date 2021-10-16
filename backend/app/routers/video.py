from fastapi import Depends, APIRouter, HTTPException, status, Response, File, Form, UploadFile
from ..pydatic_models import User_Pydantic, Video_Pydantic, VideoCard_Pydantic
from ..models import Users, Video
from ..jwt import get_current_user, get_current_active_user
from typing import List

router = APIRouter(
    prefix="/video",
    tags=["video"]
)

@router.get("/home", response_model=List[VideoCard_Pydantic])
async def home_video():
    return await VideoCard_Pydantic.from_queryset(Video.all().order_by('-created_at'))


@router.get("/public", response_model=List[VideoCard_Pydantic])
async def public_video():
    return await VideoCard_Pydantic.from_queryset(Video.filter(is_private=False).order_by('-created_at'))


@router.get("/get-{id}", response_model=Video_Pydantic)
async def get_video(id: int):
    return await Video_Pydantic.from_queryset_single(Video.get(id=id))


@router.get("/search-{word}", response_model=List[VideoCard_Pydantic])
async def search_video(word: str):
    return await VideoCard_Pydantic.from_queryset(Video.filter(title__icontains=word).order_by('-created_at'))