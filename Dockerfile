FROM python:alpine3.7
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip; apk add build-base;
RUN pip install -r requirements.txt # Write Flask in this file
EXPOSE 5001
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]