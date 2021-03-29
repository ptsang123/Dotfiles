#!/usr/bin/env python3

import os
import sys
import subprocess

question = os.popen('rofi -font "DejaVu Sans Mono 20" -width 30 -lines 1 -dmenu -p "Calculator: "')
TheQuestion = question.read()

#calculate = os.popen('qalc ' + TheQuestion.strip())
calculate = os.popen('echo "scale=2; ' + TheQuestion.strip()  + '" | bc')
Answer = calculate.read().strip()

os.popen('echo ' + str(Answer) + '| rofi -font "DejaVu Sans Mono 20" -width 30 -lines 1 -dmenu')
