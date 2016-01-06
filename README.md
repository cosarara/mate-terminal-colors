Mate Terminal is awesome because It Works (TM), does True Color, and doesn't get in my way.
It stores it's config in dconf though, which is painful.
So I made this to help me load palettes.

How to use
==========

first get a base profile:

    $ dconf dump /org/mate/terminal/profiles/default/ > base.conf

then get the conf file you want to import (eg from http://dotshare.it/ ) -> example.conf

then write the conf with a name (like lmao) onto a new dconf entry (profile3):

    $ python read.py base.conf example.conf lmao | dconf load /org/mate/terminal/profiles/profile3/

then put your new entry on the list:

    $ dconf write /org/mate/terminal/global/profile-list "['default', 'profile0', 'profile1', 'profile2', 'profile3']"
    
and that should be it.
