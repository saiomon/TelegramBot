#!/bin/sh
ps ax | newBot.py
pkill -f newBot.py
git pull
nohup python3 -u newBot.py >outti.log &
