FROM python:3
WORKDIR /opt/calculation_service
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 6543
CMD ["python", "./app.py"]
