FROM  python:3.9-alpine
ENV PYTHONBUFFERED=1
COPY requirements.txt /code/
WORKDIR /code/
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
