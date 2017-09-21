#!/bin/bash
path=/root/PycharmProjects/docker/vulhub
read=README.md
function getdir(){
    for element in `ls $1`
    do  
        dir_or_file=$1"/"$element
        if [ -d $dir_or_file ]
        then 
            getdir $dir_or_file
        else
            result=$(echo $dir_or_file | grep "${read}")
	    if [[ "$result" != "" ]]
	    then
  		 dirs=`dirname "$dir_or_file"`
	         `cd "$dirs" ;docker-compose build`

	    fi
	fi  
    done
}
getdir $path

