FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt

RUN pip install scikit-learn
RUN pip install numpy
RUN pip install pandas
RUN pip install scipy
RUN pip install psycopg2

COPY . /app
COPY docker-celery-entrypoint.sh /app