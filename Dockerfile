FROM python:3.12.1

WORKDIR /Forum

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "Forum/manage.py", "runserver", "0.0.0.0:8000"]