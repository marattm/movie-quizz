# quizz-webproject

## Refactoring Roadmap
[ Refactoring application to micro services ]

### Roadmap
* [ ] Environment setup
    - [x] Flask set up
    - [x] Docker set up
    - [x] DB set up
    - [ ] Testing
    - [ ] Deployment
    - [ ] Code Coverage & Quality
    - [ ] Continuous Integration
* [ ] Backend
    - [ ] Blueprints
    - [ ] RESTful Routes
* [ ] Frontend
    - [ ] Jinja
    - [ ] ReactJs
    - [ ] Docker
    - [ ] Testing
    - [ ] Routing
    

### Quick Start

1. Simple Service
```
cd services/quizz
python manage.py run
```

Go to http://127.0.0.1:5000/quizz/ping

2. Container
```
docker-compose -f docker-compose-dev.yml build
docker-compose -f docker-compose-dev.yml up -d --build
```

Go to http://127.0.0.1:5001/quizz/ping

3. Other command line
    - Recreate DB
```
docker-compose -f docker-compose-dev.yml run quizz python manage.py recreate_db 
```


## Previous Roadmap

Quizz game based on cinematograhic questions

1st step : frontend html/css/js
- home page
- quizz page
- contact page

2nd step : backend apache & peewee/flask + mySQL
- setting of server
- setting of APIs
- creating DB for quizz

3rd step : API
- API for quizz page
