#!/bin/bash

cmdExample='Command example: bash script/inference-client.sh "35.194.172.36:8080" "data/image/wo.jpg"'

if [ -z "$1" ]; then
  echo "[Error] no host parameter"; echo $cmdExample; exit 1;
else
  host="$1"
fi

if [ -z "$2" ]; then
  echo "[Error] no image path parameter"; echo $cmdExample; exit 1;
else
  imgPath="$2"
fi

if ! hash jq 2>/dev/null; then
  echo "[Error] please install command jq before you run the script";
  echo "[Installation command on Mac]: brew install jq"
  exit 1;
fi

imgBase64=`cat $imgPath | base64`

apiPath="/inference"
method="POST"
expectedStatusCode=200
body='{"esun_uuid":"399d69f7-8199-454e-bd79-c0c9571bc98b","esun_timestamp":1590493849,"image":"'$imgBase64'","retry":2}'
curlCmd="curl -X POST -H 'content-type: application/json' -d '$body' '$host$apiPath'"

printf "\ncurl command: %s\n\n\n" "$curlCmd"
result=$(eval $curlCmd)
printf "\nResponse:\n%s\n" "$result"
answer=$(echo $result | jq '.answer')

if [ $? -eq 0 ]; then
  printf "\n[OK] answer = %s\n\n" "$answer";
else
  printf "\n[ERROR] got error as above response\n\n";
fi