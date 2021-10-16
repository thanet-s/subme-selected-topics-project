from fastapi import Depends, APIRouter, HTTPException, status, Response
from fastapi.security import OAuth2PasswordRequestForm
from ..jwt import authenticate_user, create_access_token, get_password_hash, get_current_user
from ..models import Users
from ..pydatic_models import User_Pydantic
from datetime import timedelta
import os
from pydantic import BaseModel


router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ['ACCESS_TOKEN_EXPIRE_MINUTES'])


@router.post("/signin")
async def login_for_access_token(response: Response, form_data: OAuth2PasswordRequestForm = Depends()):

    user = await authenticate_user(form_data.username, form_data.password)

    if not user:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )
    jwt = create_access_token(
        data={"sub": user.username},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    response.set_cookie(key="jwt", value=f"Bearer {jwt}", httponly=True)
    return {"success": True, "message": f"Login to {user.username} success", "user": (await User_Pydantic.from_tortoise_orm(user)).dict()}


class Signup_form(BaseModel):
    username: str
    password: str
    cpassword: str

@router.post("/signup")
async def create_user(response: Response, form: Signup_form):
    if form.password != form.cpassword:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect password"
        )
    user_obj = await Users.create(username=form.username, password_hash=get_password_hash(form.password))
    jwt = create_access_token(
        data={"sub": user_obj.username},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    response.set_cookie(key="jwt", value=f"Bearer {jwt}", httponly=True)
    return {"success": True, "message": f"Signup {user_obj.username} success", "user": (await User_Pydantic.from_tortoise_orm(user_obj)).dict()}


@router.post("/signout")
async def signout(response: Response, current_user: Users = Depends(get_current_user)):
    response.delete_cookie(key="jwt")
    return {"success": True, "message": f"Signout {current_user.username} success"}