#!/usr/bin/env bash
# Prepare your web servers

# if command not found or have some error install nginx, redirection output and err to null
if ! command -v nginx &> /dev/null; then
    sudo apt-get update -y && sudo apt-get install nginx -y
fi
# create all directory
sudo mkdir -p /data/web_static/shared /data/web_static/releases/test
sudo sh -c 'echo "Holberton School" > /data/web_static/releases/test/index.html'
if [ -L "/data/web_static/current" ]; then
    sudo rm -r /data/web_static/current
fi
# make symbolic link
sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo tee /etc/nginx/sites-available/default > /dev/null <<EOF
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html;

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }
    
    error_page 404 /404.html;
    location = /404.html {
        internal;
    }
    
    location / {
      add_header X-Served-By "$(hostname)";
      try_files \$uri \$uri/ =404;
   }

   location /hbnb_static/ {
        alias /data/web_static/current/;
        index index.html;
   }
}
EOF
sudo service nginx restart
