
=================================================
GITHUB + UBUNTU VPS HOSTING GUIDE
=================================================

1. CREATE GITHUB REPOSITORY
----------------------------------
- Create a new repository on GitHub
- Name it: revolutionsa-proposals

2. PROJECT FILES
----------------------------------
Place these files inside:

/index.html
/logo.png

3. PUSH TO GITHUB
----------------------------------
Open terminal:

git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin YOUR_GITHUB_REPO
git push -u origin main

4. INSTALL NGINX ON UBUNTU VPS
----------------------------------
ssh root@your-vps-ip

sudo apt update
sudo apt install nginx -y

5. CLONE YOUR APP
----------------------------------
cd /var/www/

sudo git clone YOUR_GITHUB_REPO revolutionsa

6. CONFIGURE NGINX
----------------------------------
Create config:

sudo nano /etc/nginx/sites-available/revolutionsa

Paste:

server {
    listen 80;
    server_name yourdomain.com;

    root /var/www/revolutionsa;
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }
}

Enable:

sudo ln -s /etc/nginx/sites-available/revolutionsa /etc/nginx/sites-enabled/

sudo nginx -t
sudo systemctl restart nginx

7. SSL HTTPS
----------------------------------
Install Certbot:

sudo apt install certbot python3-certbot-nginx -y

sudo certbot --nginx -d yourdomain.com

DONE.

Your app will now be live.
=================================================
-->
