export DEBIAN_FRONTEND=noninteractive
sudo apt update && sudo apt-get -yq upgrade
# mkdir -p ~/workspace/info
sudo -H pip3 install flask
sudo -H pip3 install opencv-python-headless
sudo -H pip3 install numpy

