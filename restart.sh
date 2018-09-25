#!/bin/bash

echo "--- stopping docker ---"
sudo docker-compose down

sudo docker ps
sudo docker image prune -y

echo "--- starting docker ---"
sudo docker-compose up --build &

sudo docker ps