FROM python

WORKDIR /app

COPY server.py .

RUN mkdir /serverdata

VOLUME ["/serverdata"]

EXPOSE 8080

CMD ["sh", "-c", "python server.py 8080 && exec sh"]
