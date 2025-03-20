
#!/usr/bin/bash

sudo systemctl daemon-reload
sudo rm -f /etc/nginx/sites-enabled/default

sudo cp /home/ubuntu/project/nginx/nginx.conf /etc/nginx/sites-available/book_shop
sudo ln -s /etc/nginx/sites-available/book_shop /etc/nginx/sites-enabled/
#sudo ln -s /etc/nginx/sites-available/book_shop /etc/nginx/sites-enabled
#sudo nginx -t
sudo gpasswd -a www-data ubuntu
sudo systemctl restart nginx

