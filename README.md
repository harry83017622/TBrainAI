# **TBrainAI**

## **Description**
---  
This project is the API-server side source code for TBrainAI competition for hand-writing recognition in Chinese-tradition language.


## **Getting Start**
---  
#### **Folder Structure**

```
TBrainAI   
├── data/  
│   ├── image            # test image path  
│   │   └── ... 
│   └── json 
├── script/              # environment set-up and test shell script
├── src/  
│   ├── utils            # test image path  
│   │   ├── tools.py     # model and preprocessing function
│   │   └── ... 
│   └── api.py
└── ...  
```

#### **Prerequisites**

* Windows 10, Linux, and Docker
* python3.9 (maybe >=3.6 is fine).
* sudo privilege
* pip or conda

#### **Installation**

    # if you have already have sudo, skip this.
    apt-get update
    apt-get -y install sudo

    sudo apt-get install tesseract-ocr-chi-tra
    pip install numpy
    pip install pytesseract
    pip install pillow


#### **Usage**

Check out https://pypi.org/project/pytesseract/

## **To Do**
---  
* Image Processing
* Test baseline model performance

  

## Test command
---
#### by curl command
curl -X POST -H "content-type: application/json" --data "@data/json/test1.json" "http://35.194.172.36:8080/inference"

#### by inference-client.sh
bash script/inference-client.sh "35.194.172.36:8080" "data/image/wo.jpg"

## Connect to GCP
ssh -i ~/.ssh/id_gmail pittwu@35.194.172.36

## Deploy TBrainAI service on to GCE
1. In your mac / linux, go to parent directory of TBrainAI
2. Execute command: bash TBrainAI/script/deploy.sh

