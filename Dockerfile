FROM python:3.8
WORKDIR /app
COPY . /app
EXPOSE 8443
RUN pip install -r requirements.txt
CMD ["python", "main.py"]