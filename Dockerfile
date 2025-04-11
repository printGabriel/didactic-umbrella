FROM python:3

WORKDIR /code

COPY requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . .


EXPOSE 80
COPY . .
CMD [ "fastapi", "run", "main.py", "--port", "80" ]
