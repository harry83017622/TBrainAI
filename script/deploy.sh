#!/bin/bash

newBuildDir="/home/pittwu/workspace/server/new-build"

ssh -i ~/.ssh/id_gmail pittwu@35.194.172.36 rm -rf "$newBuildDir"

scp -i ~/.ssh/id_gmail -r TBrainAI "pittwu@35.194.172.36:$newBuildDir"

ssh -i ~/.ssh/id_gmail pittwu@35.194.172.36 bash "$newBuildDir/script/restart-server.sh"



