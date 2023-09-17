FROM python:3.10

# Install Poetry globally
ENV POETRY_VERSION=1.5.1
RUN pip install -U pip setuptools poetry==${POETRY_VERSION}

WORKDIR /ModelToProduction
ENV PYTHONPATH /ModelToProduction

# Install dependencies
COPY pyproject.toml poetry.lock* ./
RUN poetry config virtualenvs.create false \
&& poetry install $(test "$YOUR_ENV" == production && echo "--no-dev") --no-interaction --no-ansi

# Run
COPY . /ModelToProduction

# Change port if needed
EXPOSE 8080

CMD ["python", "server/main.py"]