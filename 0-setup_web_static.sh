#!/usr/bin/env bash
# Prepare your web servers
sudo apt-get -y update
sudo apt-get -y install nginx
mkdir -p /data/web_static/shared/
mkidr -p /data/web_static/releases/test/
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
ln -fs /data/web_static/releases/test/ /data/web_static/current
chown -R /data
chgrp -R /data
sed -i "38i//\n\tlocation /hbnb_static/\n\t{\n\t\talias /data/web_static/current/;\n\t}\n"
sudo service nginx restart
