#!/bin/bash

################################################
# new env setup flow since 2021-06-03
################################################
# 1. install gpu driver
#   a. https://www.tensorflow.org/install/gpu
#   b. https://wiki.debian.org/NvidiaGraphicsDrivers#Debian_10_.22Buster.22-1

# 2. install python and relevant packages
export DEBIAN_FRONTEND=noninteractive
sudo apt update && sudo apt-get -yq upgrade
sudo apt install python3-pip
sudo apt install tesseract-ocr-chi-tra

python3 -m venv --system-site-packages /home/tbrain/venv-tbrain
pip3 install --upgrade pip
pip3 install numpy
pip3 install opencv-python-headless
pip3 install pytesseract
pip3 install flask-executor
pip3 install tensorflow-gpu==2.4

################################################
# deprecated env setup flow before 2021-06-03
################################################
# export DEBIAN_FRONTEND=noninteractive
# sudo apt update && sudo apt-get -yq upgrade
# sudo apt install python3-pip
# sudo apt install tesseract-ocr-chi-tra

# sudo -H pip3 install flask
# sudo -H pip3 install numpy
# sudo -H pip3 install opencv-python-headless
# sudo -H pip3 install pytesseract
# sudo -H pip3 install flask-executor
# sudo -H pip3 install tensorflow-gpu==2.4


