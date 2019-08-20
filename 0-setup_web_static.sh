#!/usr/bin/env bash
#script that sets up your web servers for the deployment of web_static
sudo apt-get update
if ! command -v nginx > /dev/null; then
    sudo apt-get -y install nginx
fi
mkdir -p /data/web_static/shared
mkdir -p /data/web_static/releases/test
echo -e "
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
" | sudo tee -a /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current
chown -R ubuntu /data
chgrp -R ubuntu /data
sudo sed -i "38i\\
\tlocation = /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-enabled/default
sudo service nginx restart
