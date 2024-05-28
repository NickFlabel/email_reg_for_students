# Базовый образ, от которого идет строительство (ОС, ЯП)
FROM python:3.11.9-slim-bullseye

# Копируем файлы откуда куда
COPY ./ ./

COPY ./requirements.txt ./requirements.txt

# Какая команда запускается при строительстве образа
RUN pip install -r requirements.txt

# Открыть порт 8000
EXPOSE 8000

# Команда при запуске контейнера
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

# docker build -t <название образа> <путь к папке с Dockerfile относительно терминала> - построить образ
