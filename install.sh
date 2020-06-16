#!/bin/bash

git clone https://github.com/popovicirobert/cf-app.git

sudo apt-get install -y python3
sudo apt-get install -y python3-pip
pip3 install --upgrade setuptools
pip3 install requests
pip3 install selenium
sudo apt-get install -y xsel xclip
pip3 install clipboard 
sudo apt-get install -y python3-pyvirtualdisplay

wget https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz
tar -xvzf geckodriver*
chmod +x geckodriver
sudo mv geckodriver //usr/bin
rm geckodriver*

cd cf-app
chmod +x cf-app.sh
chmod +x checker.sh
chmod +x make_main.sh

sudo ln -s $PWD/cf-app.sh //usr/local/bin/cf-app
cd ..
