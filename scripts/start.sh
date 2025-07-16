#!/bin/bash
service cron start
exec su -s /bin/bash www-data -c "python3 /app/app.py"