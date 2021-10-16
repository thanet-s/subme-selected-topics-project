from tortoise import fields, models

class Users(models.Model):
    """
    The User model
    """

    id = fields.IntField(pk=True)
    #: This is a username
    username = fields.CharField(max_length=20, unique=True)
    password_hash = fields.CharField(max_length=128, null=True)
    active = fields.BooleanField(default=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)

    def __str__(self) -> str:
        return self.username



class Video(models.Model):
    """
    Video model
    """

    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=100)
    is_private = fields.BooleanField(default=False)
    user = fields.ForeignKeyField(
        "models.Users",
        related_name="Uploader"
    )
    created_at = fields.DatetimeField(auto_now_add=True)
    description = fields.TextField(null=True)

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    """
    Comment model
    """

    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField(
        "models.Users",
        related_name="commentator"
    )
    video = fields.ForeignKeyField(
        "models.Video",
        related_name="video"
    )
    created_at = fields.DatetimeField(auto_now_add=True)
    comment = fields.TextField(null=False)

    def __str__(self) -> str:
        return self.id


class Follow(models.Model):
    """
    Follow model
    """

    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField(
        "models.Users",
        related_name="following"
    )
    follow = fields.ForeignKeyField(
        "models.Users",
        related_name="follower"
    )

    def __str__(self) -> str:
        return f"{self.user} -> {self.follow}"
