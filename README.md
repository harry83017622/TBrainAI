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

## Machine Information with GPU
* OS : Debian 10 buster
* GPU : Tesla K80 (GeForce 400)
* CPU : 4
* Memory : 15 G
* Tensorflow : 2.4
* Cuda : 11.2
* IP: 35.201.197.216

# GPU Information
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 460.73.01    Driver Version: 460.73.01    CUDA Version: 11.2     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  Tesla K80           Off  | 00000000:00:04.0 Off |                    0 |
| N/A   33C    P8    26W / 149W |      3MiB / 11441MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+

## Test command
---
#### by curl command
curl -X POST -H "content-type: application/json" --data "@data/json/test1.json" "http://35.194.172.36:8080/inference"
curl -X POST -H "content-type: application/json" --data "@data/json/test1.json" "http://35.201.197.216:8080/inference"

#### by inference-client.sh
bash script/inference-client.sh "35.194.172.36:8080" "data/image/wo.jpg"
bash script/inference-client.sh "35.201.197.216:8080" "data/image/wo.jpg"

## Connect to GCP
ssh -i ~/.ssh/id_gmail pittwu@35.194.172.36
ssh -i ~/.ssh/id_tbrain tbrain@35.201.197.216

## Deploy TBrainAI service on to GCE
1. In your mac / linux, go to parent directory of TBrainAI
2. Execute command:
 bash TBrainAI/script/deploy.sh
 bash TBrainAI/script/deploy.sh "~/.ssh/id_tbrain" "tbrain" "35.201.197.216"

