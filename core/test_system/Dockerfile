# Используем базовый образ Python
FROM python:3.11

COPY requirements.txt /app/

# Устанавливаем зависимости
RUN pip install --upgrade pip
RUN pip install --upgrade pip && pip install -r /app/requirements.txt

# Копируем файлы проекта в контейнер
COPY . /app/
WORKDIR /app


# Экспортируем порты для внешнего доступа
EXPOSE 9090 9091

# Запускаем RPC сервер после запуска nameserver
CMD [ "python", "rpc_server.py" ]