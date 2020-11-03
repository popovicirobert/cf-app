#!/bin/bash

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

wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
chmod +x chromedriver
sudo mv chromedriver //usr/bin
rm chromedriver*


chmod +x checker.sh
chmod +x make_main.sh
chmod +x cf-app.sh
chmod +x cf-app.py

echo "export PATH=$PATH:$PWD" >> ~/.bashrc

sudo ln -s $PWD/cf-app.sh /usr/local/bin/cf-app
