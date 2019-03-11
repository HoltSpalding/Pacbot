#!/bin/bash

screen -dmS "screen-name-1" ./server.py
screen -dmS "screen-name-2" ./gameEngine.py
screen -dmS "screen-name-3" ./visualize.py


