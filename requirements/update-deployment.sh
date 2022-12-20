docker container rm -f $(docker container ls -aq)
docker rmi $(docker images -q)
git pull origin main
docker-compose build
docker-compose up -d

