#!/bin/bash

export DEBIAN_FRONTEND=noninteractive
sudo apt update && sudo apt-get -yq upgrade
sudo apt install tesseract-ocr-chi-tra

# mkdir -p ~/workspace/info
sudo -H pip3 install flask
sudo -H pip3 install opencv-python-headless
sudo -H pip3 install numpy
sudo -H pip3 install pytesseract
sudo -H pip3 install flask-executor

