FROM mattwiley/selenium:python3.9-slim

COPY python /app

WORKDIR /app
COPY includes/entrypoint.sh /entrypoint.sh

RUN pip install -r requirements.txt

RUN \
    chmod +x /entrypoint.sh && \
    chmod +x main.py

ENTRYPOINT [ "/entrypoint.sh" ]



