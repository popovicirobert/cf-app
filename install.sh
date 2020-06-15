#!/bin/bash

git clone https://github.com/popovicirobert/cf-app.git

apt-get install python3
apt-get install python3-pip
pip install requests
pip install selenium
pip install clipboard
pip install pyvirtualdisplay

cd cf-app
chmod +x cf-app.sh
chmod +x checker.sh
chmod +x make_main.sh

ln -s $PWD/cf-app.sh //usr/local/bin/cf-app


