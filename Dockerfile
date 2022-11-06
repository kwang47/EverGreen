FROM python:3.9

COPY . .

EXPOSE 5000

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.2.1/wait /wait

RUN chmod +x /wait

RUN pip install -r requirements.txt

CMD /wait && python3 Server.py
