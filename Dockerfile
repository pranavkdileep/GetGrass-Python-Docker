FROM python:3.9

WORKDIR /app
COPY . /app

RUN pip install  -r requirements.txt

EXPOSE 7860 7860 80


CMD ["python", "main.py"]