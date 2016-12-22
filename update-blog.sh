#!/bin/sh
#

GIT_PATH="/home/blog"
GIHUB_REPO="git@github.com:croef/blog_source.git"
DOCKER_PATH="/srv/docker/blog"

echo ""
echo "======== BEGIN ========"

git log --oneline --max-count=10

echo ""
echo "======== PULL SOURCE ========"
echo "$GIT_PATH"
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