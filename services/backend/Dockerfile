FROM python:3.11-buster

RUN mkdir app
WORKDIR /app

ENV PATH="${PATH}:/root/.local/bin"
ENV PYTHONPATH=.
ENV DATABASE_URL=postgres://postgres:ogneogne@db:5432/postgres

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# for migrations
COPY migrations .
COPY pyproject.toml .

COPY src src

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "5000"]
