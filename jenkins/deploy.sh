#!/bin/bash

echo "Build deploy"



ssh jenkins@swarm-deployment docker stack deploy --compose-file docker-compose.yaml m-g-a