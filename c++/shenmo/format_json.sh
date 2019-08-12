#!/bin/bash
path=../image
for i in `ls $path/*.json`
do
	cat $i | json_reformat >.1.json
    mv -f .1.json $i
done

