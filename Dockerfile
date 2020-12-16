FROM  python:3
ENV PYTHONBUFFERED=1
COPY requirements.txt /code/
WORKDIR /code/
RUN pip install -r requirements.txt