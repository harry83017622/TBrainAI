#!/bin/bash

newBuildDir="/home/pittwu/workspace/server/new-build"
prodBuildDir="/home/pittwu/workspace/server/prod"

if [ -d "$newBuildDir/src" ]; then
  # kill service
  ps aux | grep 'api.py' | grep -v 'grep' | awk '{print $2;}' | xargs sudo kill -9

  # remove old files
  rm -rf $prodBuildDir

  # move new build to prod
  mv $newBuildDir $prodBuildDir

  # start service
  cd "$prodBuildDir/src"
  nohup python3 api.py > nohup.out 2>&1 &
  echo 'complete to restart service by new build'
else
  echo "New build directory: $newBuildDir doesn't exit. Exit withoue doing anything"; exit 1;
fi




