#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static

sudo apt-get update
sudo install nginx
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo -e "hello world \n" >> /data/web_static/releases/test/index.html
ln -sf /data/web_static/current /data/web_static/releases/test/
chown --recursive ubuntu:ubuntu /data/
sed -i 's|^\tlocation / {|\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n\n\tlocation / {|' /etc/nginx/sites-available/default
service nginx restart
