#!/bin/bash

cd ~/
title=$(rofi -font "DejaVu Sans Mono 15" -dmenu -p "xterm title")
xterm -T $title
