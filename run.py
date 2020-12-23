#!/bin/sh

docker-compose up -d

printf "Waiting kibana entry..."
until $(curl -s -X GET localhost:5601/status -I | grep -q "200 OK"); do
	printf "#######"
	sleep 15
done
