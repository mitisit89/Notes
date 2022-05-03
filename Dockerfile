FROM python:3.10-alpine3.15
RUN mkdir -p tmp/Notes 
WORKDIR   /tmp/Notes/ 
COPY . /tmp/Notes/
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8080
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV TZ EUROPE/MOSCOW 
CMD ["python", "core/manage.py", "runserver", "0.0.0.0:8080"] 

