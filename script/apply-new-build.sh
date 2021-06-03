#!/bin/bash

cmdExample='Command example: bash /home/tbrain/workspace/server'

if [ -z "$1" ]; then
  echo "[Error] no base dir"; echo $cmdExample; exit 1;
else
  baseDir="$1"
  echo "base dir: $baseDir"
fi


#newBuildDir="/home/pittwu/workspace/server/new-build"
#prodBuildDir="/home/pittwu/workspace/server/prod"

newBuildDir="$baseDir/new-build"
prodBuildDir="$baseDir/prod"

if [ -d "$newBuildDir/src" ]; then
  # kill service
  ps aux | grep 'api.py' | grep -v 'grep' | awk '{print $2;}' | xargs sudo kill -9

  # remove old files
  rm -rf $prodBuildDir

  # move new build to prod
  mv $newBuildDir $prodBuildDir

  # start service
  source /home/tbrain/venv-tbrain/bin/activate
  cd "$prodBuildDir/src"
  nohup python3 api.py > nohup.out 2>&1 &
  echo 'complete to restart service by new build'
else
  echo "New build directory: $newBuildDir doesn't exit. Exit withoue doing anything"; exit 1;
fi




