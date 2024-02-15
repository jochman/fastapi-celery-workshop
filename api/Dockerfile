FROM python:3.12.2-slim

ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1

WORKDIR /code

ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.4.0

RUN apt-get update && apt-get install -y gcc libffi-dev g++

# RUN curl -sSL https://install.python-poetry.org | python3 -
RUN pip install "poetry==$POETRY_VERSION"


COPY . .

RUN poetry config virtualenvs.create false && \
    poetry install --only=main --no-root && \
    poetry build

CMD ["uvicorn", "api.app:app"]