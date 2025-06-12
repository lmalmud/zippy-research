FROM python:3.11

# System setup
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Poetry
RUN pip install poetry

# Project setup
WORKDIR /app
COPY . /app
RUN poetry install --no-dev

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root"]