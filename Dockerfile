FROM python:3.11
ENV PYTHONUNBUFFERED 1
WORKDIR /api
COPY requirements.txt /api/
COPY core/api/CodeVersusAPI/. /api/
RUN pip install --upgrade pip
RUN pip install --upgrade pip && pip install -r requirements.txt
VOLUME /core/api/