#!/bin/sh
#

GIT_PATH="/home/blog"

DOCKER_PATH="/srv/docker/blog"

echo ""
echo "======== BEGIN ========"
cd $GIT_PATH
echo "$GIT_PATH"

git log --oneline --max-count=10

echo ""
echo "======== PULL SOURCE ========"
git pull

echo ""
echo "======== HEXO GENERATE ========"
docker run -it --rm -v "$DOCKER_PATH":/root/blog croef/hexo generate
