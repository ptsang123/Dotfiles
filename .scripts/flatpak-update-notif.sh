#!/usr/bin/bash

if [[ $(flatpak --user update) = *Nothing* ]]; then
	dunstify "no updates"

else
	dunstify "Flatpak package(s) has an update"
fi
