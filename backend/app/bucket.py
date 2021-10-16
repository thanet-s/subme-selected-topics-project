from minio import Minio
import os

minio_client = Minio(
    os.environ['MINIO_HOST'],
    access_key=os.environ['MINIO_ROOT_USER'],
    secret_key=os.environ['MINIO_ROOT_PASSWORD'],
    secure=False
)