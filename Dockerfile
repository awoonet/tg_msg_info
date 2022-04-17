FROM python:slim-buster
WORKDIR /app/
COPY ./pyrogram.txt ./
RUN ["pip3", "install", "-r", "pyrogram.txt"]
COPY . .
CMD ["python3", "app.py"]
