#!/usr/bin/env python3

# how to use
# ==========

# first get a base profile:
# $ dconf dump /org/mate/terminal/profiles/default/ > base.conf
# then get the conf file you want to import (eg from http://dotshare.it/ ) -> example.conf
# then write the conf with a name (like lmao) onto a new dconf entry (profile3):
# $ python read.py base.conf example.conf lmao | dconf load /org/mate/terminal/profiles/profile3/
# then put your new entry on the list:
# $ dconf write /org/mate/terminal/global/profile-list "['default', 'profile0', 'profile1', 'profile2', 'profile3']"

import sys
import io
import configparser

# read a base mate config, (arg1), a normal config (arg2), and produce a new mate config (stdout)

with open(sys.argv[1]) as f:
    base_conf = f.read()

with open(sys.argv[2]) as f:
    new_conf = f.read()

try:
    name = sys.argv[3]
except IndexError:
    name = "converted"

base_config = configparser.ConfigParser()
base_config.read_string(base_conf)
new_config = configparser.ConfigParser()
new_config.read_string(new_conf)

def dup(color):
    color = color[1:]
    return "#" + "".join([color[n*2:n*2+2]*2 for n in range(len(color)//2)])

c = new_config["colors"]
foreground = dup(c["foreground"])
background = dup(c["background"])

palette = ":".join([dup(c["color"+str(n)]) for n in range(16)])

#print(foreground, background, palette)

base_config['/']['palette'] = "'"+palette+"'"
base_config['/']['foreground-color'] = "'"+foreground+"'"
base_config['/']['background-color'] = "'"+background+"'"
base_config['/']['visible-name'] = "'"+name+"'"

output = io.StringIO()
base_config.write(output, space_around_delimiters=False)
print(output.getvalue().strip())
