ARG APP_NAME=lamb
ARG APP_PATH=/opt/$APP_NAME
ARG PYTHON_VERSION=3.10.8
ARG POETRY_VERSION=1.2.2

# Stage: staging
FROM python:${PYTHON_VERSION}-slim-bullseye as staging
ARG APP_NAME
ARG APP_PATH
ARG POETRY_VERSION

# Update/upgrade libraries and install helper tools
RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get install -y wget curl

# PYTHONDONTWRITEBYTECODE=1: Prevents python from writing .pyc (compiled byte) codes to disk
# PYTHONUNBUFFERED=1: Forces python outputs to be sent straight to terminal -- without buffering
ENV \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1
ENV \
    POETRY_VERSION=$POETRY_VERSION \
    POETRY_HOME="/opt/poetry" \
    PATH="$POETRY_HOME/bin:$PATH" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1
ENV \
    DOCKERIZE_VERSION="v0.6.1"

# Install dockerize to ensure availability of container dependencies
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz


# Install poetry
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python3 - \
    && cd /usr/local/bin \
    && ln -s /opt/poetry/bin/poetry

# Stage: development
FROM staging as development
ARG APP_NAME
ARG APP_PATH
WORKDIR $APP_PATH
COPY ./ ./
RUN poetry install --no-root
RUN poetry export \ 
    --without dev \
    --without hashes \
    -f requirements.txt \
    --output requirements.txt
ENTRYPOINT ["poetry", "run"]
CMD ["uvicorn", "src.infrastructure.http.server:app", "--host=0.0.0.0", "--port=8000"]

# Stage: production
FROM python:${PYTHON_VERSION}-slim-bullseye as production
ARG APP_NAME
ARG APP_PATH

ENV \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1

ENV \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

ENV PORT=8000

# Install only production dependencies and run ASGI web server
WORKDIR $APP_PATH
COPY --from=development ${APP_PATH}/src ./src
COPY --from=development ${APP_PATH}/.env ./
COPY --from=development ${APP_PATH}/requirements.txt ./
RUN pip install -r requirements.txt

COPY --from=staging /usr/local/bin/dockerize /usr/local/bin

COPY ./.docker/entrypoint.sh ./
RUN chmod +x ./entrypoint.sh
ENTRYPOINT ["dockerize", "-wait", "tcp://db:5432", "-timeout", "30s"]
CMD ["python", "-m", "uvicorn", "src.infrastructure.http.server:app", "--host=0.0.0.0", "--port=8000"]