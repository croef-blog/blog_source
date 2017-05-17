#!/bin/sh
#

cd $(dirname $0)
DIR_PATH=$(pwd)

DOCKER__DATA_PATH="/home/srv/blog"
DOCKER_COMPOSE_PATH="/home/docker"

echo ""
echo "======== BEGIN ========"
cd $DIR_PATH
echo "$DIR_PATH"

git log --oneline --max-count=10

echo ""
echo "======== PULL SOURCE ========"
git pull

echo ""
echo "======== PREPARE DATA ========"
cd $DOCKER__DATA_PATH
rm -rf source
cp -r $DIR_PATH/source/ .

echo ""
echo "======== HEXO GENERATE ========"
cd $DOCKER_COMPOSE_PATH
docker-compose run --rm hexo generate
docker-compose restart hexo