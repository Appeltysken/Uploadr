FROM php:8.1-apache

RUN apt-get update && \
    apt-get install -y python3 python3-pip bash && \
    pip3 install flask --break-system-packages && \
    apt-get clean

RUN mkdir -p /home/www-data && \
    mkdir /var/www/html/uploads && \
    chown -R www-data:www-data /var/www/html/uploads && \
    echo "You got a user flag!" > /home/www-data/user.txt && \
    chown -R www-data:www-data /home/www-data
    
RUN a2enmod rewrite

COPY . /var/www/html

WORKDIR /var/www/html/

EXPOSE 8080

USER www-data

CMD service apache2 start && python3 app.py