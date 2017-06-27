#!/bin/sh
#

cd $(dirname $0)
DIR_PATH=$(pwd)

POST_DIR="$DIR_PATH/source/_posts"

post_name=$1
if [[ ! -n $post_name ]]; then
	echo ""
	echo "ERROR!!"
	echo ""
	echo "post_name null"
	echo ""
	exit 1
fi
echo "post name: $post_name"

post_time="$(date +%Y)-$(date +%m)-$(date +%d)"
echo "create new post: '$post_time-$post_name.md'"

cp "$DIR_PATH"/yyyy-mm-dd-name.md "$POST_DIR"/$post_time-$post_name.md
echo 'create done!'

echo "create time at >> '$(date +%Y)-$(date +%m)-$(date +%d) $(date +%H):$(date +%M):$(date +%S)'"
echo 'you might copy it'

i=0
while [ $i -lt 5 ]
do
	printf "\rwait $((3-i))s and open file."
	((i++))
	sleep 1
done
printf "\rcreate success: $POST_DIR"/$post_time-$post_name.md
echo ""
open "$POST_DIR"/$post_time-$post_name.md