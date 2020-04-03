#!/usr/bin/env python3
#! python3
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.


import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard.
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)

# TODO: Get address from clipboard.
#target is https://www.google.com/maps/place/Mariscal+Antonio+José+de+Sucre+2545,+Buenos+Aires/
    