FROM python:3.10
WORKDIR /app
COPY app.py /app
RUN pip install flask requests prometheus_client
CMD ["python", "app.py"]
