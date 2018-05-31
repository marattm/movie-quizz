#!/bin/bash

# Production Deploy

docker-machine create --driver amazonec2 --amazonec2-open-port 80 --amazonec2-region us-west-2 quizz-prod
docker-machine env quizz-prod
eval $(docker-machine env quizz-prod)
URL1='http://ec2-'
URL0='http://'
URL2=".us-west-2.compute.amazonaws.com"
# export REACT_APP_USERS_SERVICE_URL=$URL1$(docker-machine ip quizz-prod)$URL2
# export REACT_APP_USERS_SERVICE_URL=$URL0$(docker-machine ip quizz-prod)
docker-compose -f docker-compose-prod.yml up -d --build
# docker-compose -f docker-compose-prod.yml \
#   run quizz python manage.py recreate_db