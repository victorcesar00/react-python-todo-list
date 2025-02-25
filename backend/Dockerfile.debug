FROM python:3.13-alpine

WORKDIR /app

COPY requirements.txt .

RUN python3 -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["/venv/bin/uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
