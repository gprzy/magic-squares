FROM python:slim
COPY . /app
WORKDIR /app
RUN pip install numpy