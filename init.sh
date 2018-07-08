sudo unlink /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart

cd /home/box/web/ask
gunicorn -c /home/box/web/etc/ask.py ask.wsgi
cd /home/box/web
gunicorn -c /home/box/web/etc/hello.py hello:app

