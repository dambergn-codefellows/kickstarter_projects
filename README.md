# kickstarter_projects

kickstarter_projects

## Features

### Version 1.1.0 [Code 31: SASS/SCSS]

- [ ] Following the general guidelines of SMACSS principles, create a series of *.scss stylesheets for your application, beginning with a base.scss, vars.scss, and any other generalized stylesheets
- [ ] Within your Django app, you should also have localized *.scss stylesheets which are specific to the project_data component
- [ ] In order to process those stylesheets into *.css static files, you will be implementing thedjango-sass-processor package found HERE
 - [ ] Follow the installation instructions, and then further the setup instructions on GitHub to set up and provide a processor for your application’s stylesheets
 - [ ] Ensure that you’ve followed the instructions all the way through understanding how this package enables collection of static assets for production deployment; i.e. what you’ve been familiar with as collectstatic

# Software Install

- linux
- Install Docker on Ubuntu 18.04
 - https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04
```
sudo apt update
sudo apt install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
sudo apt update
apt-cache policy docker-ce
# Installed: (none)
sudo apt install docker-compose
sudo systemctl status docker
```
- Installation sucessful
- Setup repo and project
```
mkdir django_lender
git init
pipenv --three
pipenv shell
pipenv install -d pandas sqlalchemy

docker
```
- copy paste basic files.
- https://hub.docker.com/
- https://www.youtube.com/watch?v=pD436N0zw1Y
```
touch Dockerfile
sudo docker build -t image_name .
sudo docker image ls
sudo docker image prune
sudo docker stop $(sudo docker ps -a -q)

sudo docker rmi [OPTIONS] IMAGE [IMAGE...]
sudo docker rmi -f 0510e67a9eb7

sudo docker run -d --name container_name -t image_name
sudo docker container ls
sudo docker ps
sudo docker exec -it image_name command
sudo docker exec -it "CONTAINER ID" bash
sudo docker exec -it "CONTAINER ID" psql -U postgres
sudo docker stop my_container
```

### Django

- https://www.djangoproject.com/
```
pipenv shell
pipenv install django psycopg2-binary
django-admin startproject kickstarter_project web
./manage.py runserver
exit
pipenv shell
./manage.py runserver
sudo chmod +x entrypoint.sh
sudo docker-compose up
# To run in backgound
sudo docker-compose up --build &
# To close backgound docker
sudo docker-compose down
```

## Commands Useful after Installed (Chris Notes)

docker-compose up --build &
docker ps
docker container ls
docker exec -it "CONTAINER ID" bash
docker exec -it "CONTAINER ID" psql -U postgres
docker-compose down
docker container prune
docker image prune
docker system prune

### Load Database

- shell into web docker container and run load_db.py in container.

### CSS
- SASS
```
sudo npm install -g sass
sass --version
sass web/kickstarter_project/static/styles/main.scss ./main.css

# Django SASS Processor
# https://github.com/jrief/django-sass-processor
pip install libsass django-compressor django-sass-processor
pip freeze
```

- settings.py sass_processor

### saved
