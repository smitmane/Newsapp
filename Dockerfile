FROM python:3.11

RUN apt-get update
RUN apt-get install -y supervisor

COPY ./src/ /home/src/
WORKDIR /home/src/

RUN pip3 install -r requirements.txt

# celery -A celery_worker worker --loglevel=info
# celery -A celery_worker beat --loglevel=info
# uvicorn app:app --reload
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
RUN mkdir -p /var/log/supervisor
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
