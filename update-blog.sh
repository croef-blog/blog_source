#!/bin/sh
#

GIT_PATH="/home/blog"
GIHUB_REPO="git@github.com:croef/blog_source.git"
DOCKER_PATH="/srv/docker/blog"

echo "======== PULL SOURCE ========"
cd $GIT_PATH
git pull origin

echo ""
echo "======== CHECK GITHUB REPO ========"
git remote
g=$(git remote | grep github)

if [ "$g" = "github" ]
then
	echo "HAS GITHUB"
else
	echo "ADD REMOTE GITHUB"
	git remote add github "$GIHUB_REPO"
fi
echo "======== PUSH GITHUB ========"
git push github

echo ""
echo "======== HEXO GENERATE ========"
docker run -it --rm -v "$DOCKER_PATH":/root/blog croef/hexo generate