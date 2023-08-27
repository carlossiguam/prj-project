FROM python:3.12-rc-alpine3.17
WORKDIR /a_app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/ .
CMD ["python", "main.py"]