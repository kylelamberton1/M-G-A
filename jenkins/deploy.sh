
#!/bin/bash

echo "Build deploy"

scp docker-compose.yaml jenkins@swarm-deployment:/home/jenkins/docker-compose.yaml

ssh jenkins@swarm-deployment docker stack deploy --compose-file docker-compose.yaml m-g-a
