FROM python:alpine3.7 
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5001
ENTRYPOINT [ "python3" ] 
CMD [ "receive.py" ] 
