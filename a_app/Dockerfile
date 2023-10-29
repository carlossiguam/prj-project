FROM python:3.11-alpine
WORKDIR /a_app
COPY src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/ src/
CMD ["python", "src/app/main.py"]