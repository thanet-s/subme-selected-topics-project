from .models import Users, Video, Comment, Follow
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise import Tortoise

Tortoise.init_models(["app.models"], "models")


User_Pydantic = pydantic_model_creator(
    Users,
    name="User",
    exclude=["password_hash"]
)
UserIn_Pydantic = pydantic_model_creator(
    Users,
    name="UserIn"
)


VideoCard_Pydantic = pydantic_model_creator(
    Video,
    name="VideoCard",
    exclude=["user.password_hash", "user.id", "user.modified_at", "user.created_at",
             "user.follower", "user.following", "user.commentator", "description", "video"]
)
Video_Pydantic = pydantic_model_creator(
    Video,
    name="Video",
    exclude=["user.password_hash", "user.id", "user.modified_at",
             "user.created_at", "user.follower", "user.following", "user.commentator"]
)


Comment_Pydantic = pydantic_model_creator(
    Comment,
    name="Comment"
)


Follow_Pydantic = pydantic_model_creator(
    Follow,
    name="Follow"
)
