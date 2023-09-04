FROM python:3.10
WORKDIR /ModelToProduction
COPY pyproject.toml poetry.lock* ./
RUN pip install poetry
RUN poetry install
COPY . /ModelToProduction
# Change port if needed
EXPOSE 5000 
CMD ["python", "server/main.py"]