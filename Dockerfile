FROM python:3.7.9

ENV APP_SETTINGS="config.ProductionConfig"
ENV DATABASE_URL=""

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "manage.py", "runserver", "--host", "0.0.0.0" ]