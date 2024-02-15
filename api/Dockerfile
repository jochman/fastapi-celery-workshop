FROM python:3.12.2-slim as base

ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1

WORKDIR /code

FROM base as builder

ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.4.0

RUN apt-get update && apt-get install -y gcc libffi-dev g++

# RUN curl -sSL https://install.python-poetry.org | python3 -
RUN pip install "poetry==$POETRY_VERSION"


# if your project is stored in src, uncomment line below
COPY . .
# or this if your file is stored in $PROJECT_NAME, assuming `myproject`
# COPY myproject ./myproject
RUN poetry config virtualenvs.in-project true && \
    poetry install --only=main --no-root && \
    poetry build

FROM base as final

COPY --from=builder /code/.venv ./.venv
COPY --from=builder /code/dist .

RUN pip install *.whl && find . -name "*.whl" -type f -delete && find . -name "*.tar.gz" -type f -delete

CMD ["uvicorn", "api.app:app"]