#!/bin/bash

echo "--- stopping docker ---"
sudo docker-compose down

sudo docker rmi -f kickstarterprojects_web
# sudo docker rmi -f postgres
sudo docker image prune -f
sudo docker container prune -f
sudo docker system prune -f

echo "--- starting docker ---"
sudo docker-compose up --build &
