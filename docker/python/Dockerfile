FROM python:3.12

WORKDIR /chatbot_be

RUN apt-get update && \
  apt-get install -y --no-install-recommends tzdata && \
  rm -rf /var/lib/apt/lists/*

RUN pip install poetry

RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root --only main

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

