from fastapi import Depends, APIRouter, HTTPException, status, Response, File, Form, UploadFile
from ..pydatic_models import User_Pydantic, Video_Pydantic
from ..models import Users, Video
from ..jwt import get_current_user, get_current_active_user
from ..bucket import minio_client
from datetime import timedelta
import json
from pydantic import BaseModel
import os

router = APIRouter(
    prefix="/user",
    tags=["user"]
)


@router.get("/me", response_model=User_Pydantic)
async def read_users_me(current_user: Users = Depends(get_current_user)):
    return await User_Pydantic.from_tortoise_orm(current_user)


# class Upload_data(BaseModel):
#     title: str
#     is_private: bool
#     description: str

@router.post("/upload")
async def upload(
        title: str = Form(...),
        is_private: bool = Form(...),
        description: str = Form(...),
        videofile: UploadFile = File(...),
        coverfile: UploadFile = File(...),
        current_user: Users = Depends(get_current_active_user)
):
    video = await Video.create(title=title, description=description, is_private=is_private, user=current_user)

    print(videofile.file.fileno())

    check_cover = minio_client.bucket_exists("cover")
    if not check_cover:
        minio_client.make_bucket("cover")

        # Example anonymous read-only bucket policy.
        policy = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {"AWS": "*"},
                    "Action": ["s3:GetBucketLocation"],
                    "Resource": "arn:aws:s3:::cover",
                },
                {
                    "Effect": "Allow",
                    "Principal": {"AWS": "*"},
                    "Action": "s3:GetObject",
                    "Resource": "arn:aws:s3:::cover/*",
                },
            ],
        }
        minio_client.set_bucket_policy("cover", json.dumps(policy))
    cover_result = minio_client.put_object(
        "cover", str(video.id), coverfile.file, length=-1, part_size=10*1024*1024,
        content_type=coverfile.content_type,
    )

    if cover_result: pass


    check_video = minio_client.bucket_exists("video")
    if not check_video:
        minio_client.make_bucket("video")

        # Example anonymous read-only bucket policy.
        policy = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {"AWS": "*"},
                    "Action": ["s3:GetBucketLocation"],
                    "Resource": "arn:aws:s3:::video",
                },
                {
                    "Effect": "Allow",
                    "Principal": {"AWS": "*"},
                    "Action": "s3:GetObject",
                    "Resource": "arn:aws:s3:::video/*",
                },
            ],
        }
        minio_client.set_bucket_policy("video", json.dumps(policy))
    video_result = minio_client.put_object(
        "video", str(video.id), data=videofile.file, length=-1, part_size=10*1024*1024,
        content_type=videofile.content_type,
    )

    if video_result: pass

    return {
        "success": True,
        "video": (await Video_Pydantic.from_tortoise_orm(video)).dict()
    }
