# TBrainAI

## Test command

#### by curl command
curl -X POST -H "content-type: application/json" --data "@data/json/test1.json" "http://35.194.172.36:8080/inference"

#### by inference-client.sh
bash script/inference-client.sh "35.194.172.36:8080" "data/image/wo.jpg"

## Connect to GCP
ssh -i ~/.ssh/id_gmail pittwu@35.194.172.36

## Start services
nohup python3 api.py &  
ctrl + c  
jobs -l  

## Stop services
ps aux | grep python3  
kill -9 $our_service_process_id
