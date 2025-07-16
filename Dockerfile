FROM python:3.11-slim

RUN apt-get update && \
    pip install flask && \
    apt-get install -y cron

WORKDIR /app

RUN mkdir -p /home/www-data && \
    mkdir /app/uploads && \
    chown -R www-data:www-data /app/uploads && \
    echo "You got a user flag!" > /home/www-data/user.txt && \
    echo "You got a root flag!" > /root/root.txt && \
    chown -R www-data:www-data /home/www-data

RUN touch /var/backups/backup.sh && \
    chmod +x /var/backups/backup.sh && \
    chown www-data:www-data /var/backups/backup.sh && \
    echo "* * * * * root bash /var/backups/backup.sh" > /etc/cron.d/backup-job && \
    chmod 0644 /etc/cron.d/backup-job && \
    crontab /etc/cron.d/backup-job

COPY /scripts/start.sh /root/start.sh
RUN chmod +x /root/start.sh

COPY . /app

RUN chown -R www-data:www-data /app && \
    chown -R root:root /app/scripts

EXPOSE 5000

CMD ["/bin/bash", "/root/start.sh"]
