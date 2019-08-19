## Introduction

This is a [Flask](http://flask.pocoo.org/) application running behind uwsgi server which is being loadbalanced by nginx, which is dockerized. Awesome!!

## How to run

1. Clone the repo `git clone https://github.com/codeasashu/python-nginx-docker.git`
2. `cd` into the repo directory. `cd python-nginx-docker`
3. Create environment file from env-example file. `cp env-example .env`
4. Run `docker-compose build` and then `docker-compose up -d`
5. Enjoy the python app.

## Making changes

The code lives in `app` directory, which have this file called `server.py` - a simple flask application. Make changes there and see if it works

## TODO
1. SSL support
2. Live code reloads
3. Basic frontend to demonstrate static content loading via nginx
