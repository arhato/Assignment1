FROM python

WORKDIR /app

COPY client.py .

RUN mkdir /clientdata

VOLUME ["/clientdata"]

ENTRYPOINT ["sh", "-c", "python client.py \"$1\" \"$2\"; exec sh", "--"]
