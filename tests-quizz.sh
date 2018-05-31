#!/bin/bash

# run

docker-compose -f docker-compose-dev.yml \
  run quizz python manage.py test