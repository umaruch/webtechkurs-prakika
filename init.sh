sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
gunicorn -b '0.0.0.0:8080' -D hello:app
gunicorn -c /home/box/web/etc/django_config.py -D ask.wsgi:application
