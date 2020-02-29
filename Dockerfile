FROM python:3.7.3-slim
COPY . /sample-app
WORKDIR /sample-app
RUN apt-get update && apt-get install -y python-pip
RUN pip install --upgrade pip flask
EXPOSE 5000
ENTRYPOINT ["python","/sample-app/app.py"]

