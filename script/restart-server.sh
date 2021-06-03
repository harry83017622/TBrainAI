#!/bin/bash

set -x

currentDir=$(dirname "$0")
# echo "current dir: $currentDir"
prodBuildDir=$(dirname "$currentDir")
# echo "prod build dir: $prodBuildDir"
prodSrcDir="$prodBuildDir/src"
# echo "prod src dir: $prodSrcDir"

# newBuildDir="$baseDir/new-build"
# prodBuildDir="$baseDir/prod"

if [ -d "$prodSrcDir" ]; then
  # kill service
  ps aux | grep 'api.py' | grep -v 'grep' | awk '{print $2;}' | xargs sudo kill -9

  # start service
  source /home/tbrain/venv-tbrain/bin/activate
  cd "$prodSrcDir"
  nohup python3 api.py > nohup.out 2>&1 &
  echo "complete to restart service on path $prodSrcDir"
else
  echo "New build directory: $prodSrcDir does not exit. Exit withoue doing anything"; exit 1;
fi

set +x


