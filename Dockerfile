FROM python:3-alpine

ENV APP_HOME=/app DEVELOPER="Fernando Gonzalez"
WORKDIR ${APP_HOME}

ADD . /app

RUN pip install -r requirements.txt

CMD [ "./soup.py" ]
ENTRYPOINT [ "python" ]