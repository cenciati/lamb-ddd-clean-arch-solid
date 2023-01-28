ARG APP_NAME=lamb
ARG APP_PATH=/opt/$APP_NAME
ARG PYTHON_VERSION=3.10.8
ARG POETRY_VERSION=1.2.2

# Stage: staging
FROM python:${PYTHON_VERSION}-slim as staging
ARG APP_NAME
ARG APP_PATH
ARG POETRY_VERSION

# PYTHONDONTWRITEBYTECODE=1: Prevents python from writing .pyc (compiled byte) codes to disk
# PYTHONUNBUFFERED=1: Forces python outputs to be sent straight to terminal -- without buffering
ENV \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1
ENV \
    POETRY_VERSION=$POETRY_VERSION \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1

# Update libraries and install necessary tools
RUN apt-get update \
    && apt-get install -y wget curl

# Install poetry
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python3 - \
    && cd /usr/local/bin \
    && ln -s /opt/poetry/bin/poetry
ENV PATH="$POETRY_HOME/bin:$PATH"

# Install dockerize to ensure availability of container dependencies
ENV DOCKERIZE_VERSION="v0.6.1"
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

# Import project source code and dependency files
WORKDIR $APP_PATH
COPY ./poetry.lock ./
COPY ./pyproject.toml ./
COPY ./.env ./
COPY ./src ./src

# Stage: development
FROM staging as development
ARG APP_NAME
ARG APP_PATH
WORKDIR $APP_PATH
RUN poetry install
ENTRYPOINT ["poetry", "run"]
CMD ["tail", "-f", "/dev/null"]

# Stage: production
FROM python:$PYTHON_VERSION as production
ARG APP_NAME
ARG APP_PATH

ENV \
    PYTHONDONTWRITEBYTECODE=1 \
    POETRY_HOME="/opt/poetry" \
    PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1

ENV \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

ENV PORT=8000

# Install poetry
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python3 - \
    && cd /usr/local/bin \
    && ln -s /opt/poetry/bin/poetry
ENV PATH="$POETRY_HOME/bin:$PATH"

# Install only production dependencies and run ASGI web server
WORKDIR $APP_PATH
COPY ./poetry.lock ./
COPY ./pyproject.toml ./
COPY ./.env ./
COPY ./src ./src
RUN poetry install --without dev

COPY ./entrypoint.sh ./entrypoint.sh
RUN chmod +x ./entrypoint.sh
ENTRYPOINT ["entrypoint.sh"]
CMD ["poetry", "run", "uvicorn", "src.infrastructure.http.server:app", "--host=0.0.0.0", "--port=$PORT"]