FROM python:3.8

RUN pip install responder
RUN pip install typesystem==0.2.5

WORKDIR /var/lib/app

COPY arith/ ./arith/
COPY static/ ./static/
COPY templates/ ./templates/
COPY *.py ./

EXPOSE 5042

CMD ["python", "web.py"]

