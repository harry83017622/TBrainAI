#!/bin/bash

cmdExample='Command example: bash TBrainAI/script/deploy.sh "~/.ssh/id_tbrain" "tbrain" "35.201.197.216"'

if [ -z "$1" ]; then
  echo "[Error] no ssh key path"; echo $cmdExample; exit 1;
else
  sshKeyPath="$1"
  echo "ssh key path: $sshKeyPath"
fi

if [ -z "$2" ]; then
  echo "[Error] no user name for remote ssh machine"; echo $cmdExample; exit 1;
else
  userName="$2"
  echo "user name: $userName"
fi

if [ -z "$3" ]; then
  echo "[Error] no host parameter"; echo $cmdExample; exit 1;
else
  host="$3"
  echo "host: $host"
fi

set -x # enable debug

#baseDir="/home/$userName/tmp/server-test"
baseDir="/home/$userName/workspace/server"
newBuildDirName="new-build"
newBuildDirPath="$baseDir/$newBuildDirName"

ssh -i "$sshKeyPath" "$userName@$host" rm -rf "$newBuildDirPath"

ssh -i "$sshKeyPath" "$userName@$host" "[ -d $baseDir ] || mkdir -p $baseDir"

scp -i "$sshKeyPath" -r TBrainAI "$userName@$host:$newBuildDirPath"

#ssh -i "$sshKeyPath" "$userName@$host" bash "$newBuildDirPath/script/restart-server.sh $baseDir"
ssh -i "$sshKeyPath" "$userName@$host" bash "$newBuildDirPath/script/apply-new-build.sh $baseDir"

set +x # disable debug

