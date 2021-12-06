# activate compositor
picom --config ~/.config/picom/picom.conf &

# activate autoclicker
$HOME/.scripts/poe/autoclicker.sh &

# launch poe
steam steam://rungameid/238960

# activate poe awakener macro
awakened-poe-trade

# kill compositor
killall picom

# kill autoclicker
kill -9 `ps -aux | grep autoclicker`
