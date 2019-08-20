#!/usr/bin/env bash
# Prepare your web servers.
sudo apt-get -y update
sudo apt-get -y install --no upgrade nginx
mkdir -p /data/web_static/shared
mkdir -p /data/web_static/releases/test
touch /data/web_static/releases/test/index.html
echo -e "
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
" | sudo tee -a /data/web_static/releases/test/index.html
ln -fs /data/web_static/releases/test /data/web_static/current
chown -R ubuntu /data
chgrp -R ubuntu /data
sed -i "33i\ \n\tlocation /hbnb_static/\n\t{\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default
sudo service nginx restart
