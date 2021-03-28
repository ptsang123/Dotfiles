#!/bin/sh
pkexec sysctl -w abi.vsyscall32=0
$HOME/.scripts/League/lol_launch_helper.sh &
lutris lutris:rungameid/3
