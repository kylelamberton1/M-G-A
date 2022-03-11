#!/bin/bash

echo "Build deploy"



ssh jenkins@jenkins-development docker stack deploy --compose-file docker-compose.yaml m-g-a