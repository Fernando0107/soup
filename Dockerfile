FROM python:3-alpine

ENV APP_HOME=/app DEVELOPER="Fernando Gonzalez"
WORKDIR ${APP_HOME}

RUN pip install -r requirements.txt

COPY soup.py requirements.txt ./

CMD [ "./soup.py" ]
ENTRYPOINT [ "python" ]