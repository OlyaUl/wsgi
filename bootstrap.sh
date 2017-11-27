#!/bin/bash

apt-get update
apt-get install python3-pip -y
pip3 install werkzeug
pip3 install -r /vagrant/reqiurements.txt
python3 /vagrant/rout.py
