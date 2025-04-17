#!/bin/sh
sudo docker container remove lab4-flaskapp-1
sudo docker container remove lab4-rpc-1

sudo docker image remove lab4-flaskapp
sudo docker image remove lab4-rpc

sudo docker compose up

