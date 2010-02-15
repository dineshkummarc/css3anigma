#!/bin/bash

level="${QUERY_STRING}"
if [ -z "${level}" ] ; then
    level=1
fi

log=`cat`
if [ -z "${log}" ] ; then
  level=$level;
else 
  mkdir logs/$level;
  file=`date +%m%d%y_%H_%M_%s`;
  let lastlevel=$level - 1;
  echo "${log}" > logs/$lastlevel/$file;
fi

level=`determinelevel.cgi $level`

echo "Status: 200";
echo "Content-type: text/html";
echo "";
cat ../levels/${level}.level;

#printenv
