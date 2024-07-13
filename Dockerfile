FROM python:3.12

RUN apt-get update \
    && apt-get install -y \
    libcurl4-openssl-dev \
    libssl-dev \
    curl \
    nano \
    python3-dev \
    tzdata

ENV TZ=America/Sao_Paulo

WORKDIR /code

RUN pip install poetry pycurl

COPY pyproject.toml poetry.lock /code/

RUN poetry install --no-root --no-interaction

COPY . /code

CMD ["poetry", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
