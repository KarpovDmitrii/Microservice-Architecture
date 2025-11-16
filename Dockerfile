FROM python:3.13-slim

WORKDIR /Microservice-Architecture

COPY requirements.txt /Microservice-Architecture/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /Microservice-Architecture

ENV PYTHONPATH=/Microservice-Architecture

EXPOSE 8000

CMD ["sh", "-c", "alembic upgrade head && uvicorn src.main:app --host 0.0.0.0 --port 8000"]