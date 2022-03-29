#!/usr/bin/bash

case $1 in
        up)
                pactl set-sink-volume @DEFAULT_SINK@ +2% 
                dunstify -r 1020 "Volume set to $(pactl get-sink-volume @DEFAULT_SINK@ | awk 'NR==1 {print $5}')"

        ;;

        down)
                pactl set-sink-volume @DEFAULT_SINK@ -2% 
                dunstify -r 1020 "Volume set to $(pactl get-sink-volume @DEFAULT_SINK@ | awk 'NR==1 {print $5}')"
        ;;

        mute)
                pactl set-sink-mute @DEFAULT_SINK@ toggle
                dunstify -r 1020 "Muted: $(pactl get-sink-mute @DEFAULT_SINK@ | awk 'NR==1 {print $2}')"
        ;;

esac
