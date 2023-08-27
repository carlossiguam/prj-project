FROM python:3.11-alpine
WORKDIR /a_app
COPY requirements.txt /a_app/
RUN pip install --no-cache-dir -r requirements.txt
COPY src/ /a_app/src
CMD ["python", "src/main.py"]