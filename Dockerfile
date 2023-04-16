FROM python:3.9
RUN apt update -y && apt install awscli -y
RUN python -m pip install --upgrade pip
WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt

CMD ["python", "main.py"]
