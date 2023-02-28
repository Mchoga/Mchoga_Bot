FROM python:3.8
WORKDIR /app
COPY . /app
EXPOSE 8081
RUN pip install -r requirements.txt
CMD ["python", "main.py"]