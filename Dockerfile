FROM python:3.12-slim AS builder


WORKDIR /app


COPY /app /app
COPY requirements.txt /app


RUN pip install --upgrade pip
RUN pip install -r requirements.txt




EXPOSE 8000

CMD ["python", "main.py"]