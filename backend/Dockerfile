
FROM python:3.9-slim

WORKDIR /code
RUN apt update && apt install gcc -y

EXPOSE 4000

CMD pip install --no-cache-dir --upgrade -r /code/requirements.txt && uvicorn app.main:app --host 0.0.0.0 --port 4000 --reload
